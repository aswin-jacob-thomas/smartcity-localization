import numpy as np
from sklearn.cluster import MeanShift
import utm
from sklearn.cluster import MeanShift
import statistics 
from statistics import mode 
import json
import requests
import time
import os
import geocoder

def lambda_handler(event, context):
    url = 'http://backend.digitaltwincities.info'
    response = requests.get(url).json()
    json_data = response
    data = json_data['data']
    array = []
    # Creating image array which contains all the images
    data_array = []
    # Creating a cordinate array which contains all the coordinates
    cordinate_array = []

    zone_array = []

    for d in data:
        ut_cordinates = utm.from_latlon(d['latitude'], d['longitude'])
        t_list = [ut_cordinates[0],ut_cordinates[1],d['compass']]
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
    for cluster in range(len(cluster_centers)):
        current_cluster_result = {}
        indices_of_cluster = np.where(array[:,3] == cluster)
        # Here we take all the elements that belong to the current cluster and the indices are stored as indices_of cluster
       
        cluster_array = array[indices_of_cluster]  
        compass_array = cluster_array[:,[2]]
        a = np.tan(np.radians(90-compass_array))
        b = np.ones(np.shape(compass_array))
        c = np.multiply(a,cluster_array[:,[0]]) - cluster_array[:,[1]]
        eq_coeff_cluster = np.hstack((a, -b ,c))
        # we take the value of p as 300 just for analysing the time taken to run this
        # Creating lines from the compass and the current point
        p = 100
        len_of_cluster = len(cluster_array)

        # Initializing the intersection of lines numpy array
        intersections_of_lines = np.empty([p,2]) 
        for i in range(p):
            idx = np.random.randint(len_of_cluster, size=2)
            lines = eq_coeff_cluster[idx, :]
            
            A = lines[:, [0,1]]
            Y = lines[:, [2]]

            X = np.matmul(np.linalg.pinv(A),  Y)
            X = np.concatenate(X)
            
            intersections_of_lines[i,:] = X

        # Performing mean shift clustering and finding the cluster with the maximum number of points
        # This center point is taken as the estimated center of the object
        if len_of_cluster < 2:
            continue
        ms = MeanShift(bandwidth=100)  
        labels = (ms.fit_predict(intersections_of_lines)).tolist()
        cluster_centers = ms.cluster_centers_
        
        mode_of_labels = max(set(labels), key=labels.count)
        current_cluster_result['cluster_id'] = cluster
        current_cluster_result['cluster_item_count'] = len_of_cluster
        cordinate_list = (cordinate_array[indices_of_cluster]).tolist()
        cordinate = max(set(cordinate_list), key=cordinate_list.count)

        zone_list = (zone_array[indices_of_cluster]).tolist()
        zone = max(set(zone_list), key=zone_list.count)
        lat_long = utm.to_latlon(cluster_centers[mode_of_labels][0], cluster_centers[mode_of_labels][1], cordinate, zone)
        current_cluster_result['cluster_latitude'] = lat_long[0]
        current_cluster_result['cluster_longitude'] = lat_long[1]
        g = geocoder.arcgis([lat_long[0], lat_long[1]], method='reverse')
        current_cluster_result['cluster_address'] = g.json['address']
        current_cluster_result['cluster_objects'] = (data_array[indices_of_cluster]).tolist()
        
        return_value.append(current_cluster_result)
    
    return {
        "statusCode": 200,
        "body": json.dumps({'objects': return_value})
    }

print(lambda_handler({},{})['body'])

# Uncomment the following line if the code is run in local machine

# with open('result_localization.json','w') as f:
#     f.writelines(lambda_handler({},{})['body'])

# print("Copy and paste the following line in firefox browser")
# print(os.getcwd()+'/result_localization.json')