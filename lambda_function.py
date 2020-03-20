import numpy as np
from sklearn.cluster import MeanShift
import utm
from sklearn.cluster import MeanShift
from sklearn.metrics.pairwise import haversine_distances
import json
import urllib.request
import time
import os
from multiprocessing import Process, Pipe

def parallel(cluster_id, cluster_array,cordinate_array, zone_array, data_array, conn):
    current_cluster_result = {}
    
    len_of_cluster = len(cluster_array)
    compass_array = cluster_array[:,[2]]
    a = np.tan(np.radians(90-compass_array))
    b = np.ones(np.shape(compass_array))
    c = np.multiply(a,cluster_array[:,[0]]) - cluster_array[:,[1]]
    eq_coeff_cluster = np.hstack((a, -b ,c))
    # we take the value of p as 300 just for analysing the time taken to run this
    # Creating lines from the compass and the current point
    p = 100

    # Initializing the intersection of lines numpy array
    pairwise_indices = np.random.randint(0, len_of_cluster , (p,2))
    pairs = eq_coeff_cluster[pairwise_indices]

    A = pairs[:,:,:-1]
    Y = pairs[:,:,-1:]
    intersections_of_lines = np.squeeze(np.matmul(np.linalg.pinv(A),  Y))
    ms = MeanShift(bandwidth=150)  
    labels = (ms.fit_predict(intersections_of_lines)).tolist()
    cluster_centers = ms.cluster_centers_
    end = time.time()

    mode_of_labels = max(set(labels), key=labels.count)
    current_cluster_result['cluster_id'] = cluster_id
    current_cluster_result['cluster_item_count'] = len_of_cluster       
    
    cordinate_list = (cordinate_array).tolist()
    cordinate = max(set(cordinate_list), key=cordinate_list.count)

    zone_list = (zone_array).tolist()
    zone = max(set(zone_list), key=zone_list.count)
    lat_long = utm.to_latlon(cluster_centers[mode_of_labels][0], cluster_centers[mode_of_labels][1], cordinate, zone)

    current_cluster_result['cluster_latitude'] = lat_long[0]
    current_cluster_result['cluster_longitude'] = lat_long[1]
    current_cluster_result['cluster_objects'] = (data_array).tolist()
    conn.send(current_cluster_result)

def read_remote_url(url, conn):
    response = urllib.request.urlopen(url).read()
    json_data = json.loads(response)
    data = json_data['data']
    conn.send(data)

def lambda_handler(event, context):
    processes = []
    parent_connections = []
    
    parent1, child1 = Pipe()
    parent2, child2 = Pipe()
    
    parent_connections.append(parent1)
    parent_connections.append(parent2)
    
    p1 = Process(target=read_remote_url, args=('http://backend.digitaltwincities.info', child1))
    p2 = Process(target=read_remote_url, args=('http://backend.digitaltwincities.info/poles', child2))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()

    data = parent1.recv()
    poles_data = parent2.recv()
    array = []
    # Creating image array which contains all the images
    data_array = []
    # Creating a cordinate array which contains all the coordinates
    cordinate_array = []

    zone_array = []

    for d in data:
        ut_cordinates = utm.from_latlon(d['latitude'], d['longitude'])
        t_list = [ut_cordinates[0],ut_cordinates[1],d['compass']+2.28]
        data_array.append(d)
        cordinate_array.append(ut_cordinates[2])
        zone_array.append(ut_cordinates[3])
        array.append(t_list)
    array = np.array(array)
    data_array = np.array(data_array)
    cordinate_array = np.array(cordinate_array)
    zone_array = np.array(zone_array)

    # Now the array will have latitude, longitude and compass as its columns
    X = array[:,[0,1]]
    # Now X will have only latitude and longitude values. Performing mean shift algorithm on the latitude and longitudes
    ms = MeanShift(bandwidth=50)
    labels = ms.fit_predict(X)
    cluster_centers = ms.cluster_centers_
    labels = np.vstack(labels)
    
    array = np.hstack((array,labels))
    # Stacking the labels next to array. Now array contains latitude, longitude, compass, label
    
    return_value = []
    processes = []
    parent_connections = []
    
    for cluster in range(len(cluster_centers)):
        
        indices_of_cluster = np.where(array[:,3] == cluster)
        cluster_array = array[indices_of_cluster]  
        len_of_cluster = len(cluster_array)
        if len_of_cluster < 2:
            continue
        parent_conn, child_conn = Pipe()
        parent_connections.append(parent_conn)
        
        process = Process(target=parallel, args=(cluster, cluster_array, cordinate_array[indices_of_cluster], 
                    zone_array[indices_of_cluster], data_array[indices_of_cluster], child_conn,))
        
        processes.append(process)
        
    for process in processes:
        process.start()
    
    for process in processes:
        process.join()
    
    only_cluster_centers = []
    for parent_connection in parent_connections:
        cluster = parent_connection.recv()
        return_value.append(cluster) #[0]
        only_cluster_centers.append([cluster['cluster_latitude'], cluster['cluster_longitude']])

    # get all the cluster center locations and all the pole locations
    # get the closest pole for each of the cluster
    # update the pole number in each of the cluster as a new closest_pole_number attribute
    poles = []
    
    for d in poles_data:
        poles.append([d['latitude'], d['longitude']])
    
    poles = np.array(poles)
    
    only_cluster_centers = np.array(only_cluster_centers)

    result = haversine_distances(np.radians(only_cluster_centers), np.radians(poles))
    nearest_pole_manual_id = (result.argmin(axis=1, ) + 1).tolist()
    

    for index, cluster in enumerate(return_value):
        cluster['nearest_pole'] = nearest_pole_manual_id[index]


    return {
        "statusCode": 200,
        "body": json.dumps({'objects': return_value})
    }

