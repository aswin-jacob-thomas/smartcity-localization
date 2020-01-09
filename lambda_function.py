import numpy as np
from sklearn.cluster import MeanShift
import utm
from sklearn.cluster import MeanShift
import statistics 
from statistics import mode 
import json
import requests

def lambda_handler(event, context):
    print("Invoked the function lambda")
    url = 'http://18.236.117.181:8081/'
    response = requests.get(url).json()
    print("Coming in here")
    # print(response)
    json_data = {"data": [{"latitude": 29.7604166666667, "longitude": 95.3556666666667, "compass": 3185.0, "image": "random.jpeg"}, {"latitude": 29.7604333333333, "longitude": 95.3555333333333, "compass": 3565.0, "image": "random.jpeg"}, {"latitude": 29.7604333333333, "longitude": 95.3554, "compass": 3901.0, "image": "random.jpeg"}, {"latitude": 29.7603666666667, "longitude": 95.3553, "compass": 4215.0, "image": "random.jpeg"}, {"latitude": 29.7602666666667, "longitude": 95.3552166666667, "compass": 4508.0, "image": "random.jpeg"}, {"latitude": 29.7601666666667, "longitude": 95.3551333333333, "compass": 4670.0, "image": "random.jpeg"}, {"latitude": 29.76005, "longitude": 95.3551, "compass": 4856.0, "image": "random.jpeg"}, {"latitude": 29.7598833333333, "longitude": 95.3551333333333, "compass": 5180.0, "image": "random.jpeg"}, {"latitude": 29.7597166666667, "longitude": 95.3553166666667, "compass": 5795.0, "image": "random.jpeg"}, {"latitude": 29.7597, "longitude": 95.3554666666667, "compass": 6098.0, "image": "random.jpeg"}, {"latitude": 29.7597833333333, "longitude": 95.3556, "compass": 6215.0, "image": "random.jpeg"}, {"latitude": 29.7599, "longitude": 95.3556833333333, "compass": 143.0, "image": "random.jpeg"}, {"latitude": 29.7598833333333, "longitude": 95.3557, "compass": 499.0, "image": "random.jpeg"}, {"latitude": 29.7599166666667, "longitude": 95.35585, "compass": 704.0, "image": "random.jpeg"}, {"latitude": 29.7600166666667, "longitude": 95.35595, "compass": 1174.0, "image": "random.jpeg"}, {"latitude": 29.7601, "longitude": 95.3559333333334, "compass": 1223.0, "image": "random.jpeg"}, {"latitude": 29.7602666666667, "longitude": 95.3559666666667, "compass": 2244.0, "image": "random.jpeg"}, {"latitude": 29.7603166666667, "longitude": 95.3558, "compass": 2556.0, "image": "random.jpeg"}, {"latitude": 29.76035, "longitude": 95.35575, "compass": 2809.0, "image": "random.jpeg"}, {"latitude": 29.7604166666667, "longitude": 95.35565, "compass": 3135.0, "image": "random.jpeg"}, {"latitude": 29.7592333333333, "longitude": 95.3555666666667, "compass": 3274.0, "image": "random.jpeg"}, {"latitude": 29.7592, "longitude": 95.3554, "compass": 3456.0, "image": "random.jpeg"}, {"latitude": 29.7590833333333, "longitude": 95.3553666666667, "compass": 4188.0, "image": "random.jpeg"}, {"latitude": 29.75905, "longitude": 95.35535, "compass": 4603.0, "image": "random.jpeg"}, {"latitude": 29.75895, "longitude": 95.3551333333333, "compass": 4873.0, "image": "random.jpeg"}, {"latitude": 29.7589666666667, "longitude": 95.3552333333333, "compass": 5285.0, "image": "random.jpeg"}, {"latitude": 29.75885, "longitude": 95.3553, "compass": 5437.0, "image": "random.jpeg"}, {"latitude": 29.7587166666667, "longitude": 95.3553833333333, "compass": 5826.0, "image": "random.jpeg"}, {"latitude": 29.75875, "longitude": 95.3556166666667, "compass": 198.0, "image": "random.jpeg"}, {"latitude": 29.7588166666667, "longitude": 95.3556666666667, "compass": 428.0, "image": "random.jpeg"}, {"latitude": 29.7588666666667, "longitude": 95.3557166666667, "compass": 704.0, "image": "random.jpeg"}, {"latitude": 29.75885, "longitude": 95.3558166666667, "compass": 969.0, "image": "random.jpeg"}, {"latitude": 29.7589, "longitude": 95.3558666666667, "compass": 1418.0, "image": "random.jpeg"}, {"latitude": 29.75905, "longitude": 95.3557333333333, "compass": 1787.0, "image": "random.jpeg"}, {"latitude": 29.7591, "longitude": 95.3557333333333, "compass": 2544.0, "image": "random.jpeg"}, {"latitude": 29.7591666666667, "longitude": 95.3557166666667, "compass": 2740.0, "image": "random.jpeg"}, {"latitude": 29.7468, "longitude": 95.3776833333333, "compass": 5557.0, "image": "random.jpeg"}, {"latitude": 29.7467833333333, "longitude": 95.3777666666667, "compass": 124.0, "image": "random.jpeg"}, {"latitude": 29.7470166666667, "longitude": 95.3776666666667, "compass": 4128.0, "image": "random.jpeg"}, {"latitude": 29.7472333333333, "longitude": 95.3778166666667, "compass": 3351.0, "image": "random.jpeg"}, {"latitude": 29.7472333333333, "longitude": 95.3778333333333, "compass": 2926.0, "image": "random.jpeg"}, {"latitude": 29.7470833333333, "longitude": 95.37785, "compass": 2656.0, "image": "random.jpeg"}, {"latitude": 29.7470333333333, "longitude": 95.3780333333333, "compass": 2260.0, "image": "random.jpeg"}, {"latitude": 29.74695, "longitude": 95.37805, "compass": 1815.0, "image": "random.jpeg"}, {"latitude": 29.74675, "longitude": 95.3781833333333, "compass": 1189.0, "image": "random.jpeg"}, {"latitude": 29.7654666666667, "longitude": 95.3772166666667, "compass": 1195.0, "image": "random.jpeg"}, {"latitude": 29.7655166666667, "longitude": 95.3772333333333, "compass": 1675.0, "image": "random.jpeg"}, {"latitude": 29.7657, "longitude": 95.37715, "compass": 2328.0, "image": "random.jpeg"}, {"latitude": 29.7656666666667, "longitude": 95.3771333333333, "compass": 2983.0, "image": "random.jpeg"}, {"latitude": 29.76525, "longitude": 95.3772166666667, "compass": 634.0, "image": "random.jpeg"}, {"latitude": 29.7654166666667, "longitude": 95.3770166666667, "compass": 301.0, "image": "random.jpeg"}, {"latitude": 29.7654666666667, "longitude": 95.37685, "compass": 5474.0, "image": "random.jpeg"}, {"latitude": 29.7654333333333, "longitude": 95.3767333333333, "compass": 4994.0, "image": "random.jpeg"}, {"latitude": 29.7655833333333, "longitude": 95.3768333333333, "compass": 4411.0, "image": "random.jpeg"}, {"latitude": 29.7593666666667, "longitude": 95.3543666666667, "compass": 1428.0, "image": "random.jpeg"}, {"latitude": 29.7592833333333, "longitude": 95.3543, "compass": 1616.0, "image": "random.jpeg"}, {"latitude": 29.75925, "longitude": 95.35425, "compass": 930.0, "image": "random.jpeg"}, {"latitude": 29.7591833333333, "longitude": 95.3541333333333, "compass": 370.0, "image": "random.jpeg"}, {"latitude": 29.7593166666667, "longitude": 95.3540333333333, "compass": 108.0, "image": "random.jpeg"}, {"latitude": 29.75925, "longitude": 95.3536666666667, "compass": 5283.0, "image": "random.jpeg"}, {"latitude": 29.7593166666667, "longitude": 95.3536, "compass": 5034.0, "image": "random.jpeg"}, {"latitude": 29.7594166666667, "longitude": 95.3535833333333, "compass": 4821.0, "image": "random.jpeg"}, {"latitude": 29.7595166666667, "longitude": 95.3536333333333, "compass": 4378.0, "image": "random.jpeg"}, {"latitude": 29.7596333333333, "longitude": 95.3536333333333, "compass": 4080.0, "image": "random.jpeg"}, {"latitude": 29.7596833333333, "longitude": 95.3537833333333, "compass": 3928.0, "image": "random.jpeg"}, {"latitude": 29.7597666666667, "longitude": 95.3538, "compass": 3610.0, "image": "random.jpeg"}, {"latitude": 29.7597, "longitude": 95.35395, "compass": 3421.0, "image": "random.jpeg"}, {"latitude": 29.7596666666667, "longitude": 95.3540166666667, "compass": 2962.0, "image": "random.jpeg"}, {"latitude": 29.7596, "longitude": 95.3541166666667, "compass": 2500.0, "image": "random.jpeg"}, {"latitude": 29.7595333333333, "longitude": 95.35415, "compass": 2186.0, "image": "random.jpeg"}, {"latitude": 29.7594333333333, "longitude": 95.3541666666667, "compass": 1846.0, "image": "random.jpeg"}, {"latitude": 29.7594333333333, "longitude": 95.35425, "compass": 1334.0, "image": "random.jpeg"}, {"latitude": 29.7494666666667, "longitude": 95.37785, "compass": 2210.0, "image": "random.jpeg"}, {"latitude": 29.7495166666667, "longitude": 95.3776833333333, "compass": 2579.0, "image": "random.jpeg"}, {"latitude": 29.7495166666667, "longitude": 95.3776166666667, "compass": 3516.0, "image": "random.jpeg"}, {"latitude": 29.7495833333333, "longitude": 95.3774166666667, "compass": 4088.0, "image": "random.jpeg"}, {"latitude": 29.7494333333333, "longitude": 95.3773166666667, "compass": 4678.0, "image": "random.jpeg"}, {"latitude": 29.7493333333333, "longitude": 95.3772333333333, "compass": 4780.0, "image": "random.jpeg"}, {"latitude": 29.7492333333333, "longitude": 95.3772833333333, "compass": 5011.0, "image": "random.jpeg"}, {"latitude": 29.74915, "longitude": 95.37735, "compass": 5791.0, "image": "random.jpeg"}, {"latitude": 29.7490666666667, "longitude": 95.3775666666667, "compass": 5996.0, "image": "random.jpeg"}, {"latitude": 29.7494666666667, "longitude": 95.3775166666667, "compass": 5842.0, "image": "random.jpeg"}, {"latitude": 29.7492666666667, "longitude": 95.37775, "compass": 742.0, "image": "random.jpeg"}, {"latitude": 29.7493166666667, "longitude": 95.37785, "compass": 1589.0, "image": "random.jpeg"}, {"latitude": 29.7646, "longitude": 95.3755333333333, "compass": 1565.0, "image": "random.jpeg"}, {"latitude": 29.7643, "longitude": 95.3755166666667, "compass": 634.0, "image": "random.jpeg"}, {"latitude": 29.7642, "longitude": 95.3754, "compass": 353.0, "image": "random.jpeg"}, {"latitude": 29.7641833333333, "longitude": 95.37505, "compass": 6133.0, "image": "random.jpeg"}, {"latitude": 29.76425, "longitude": 95.37485, "compass": 5767.0, "image": "random.jpeg"}, {"latitude": 29.7644, "longitude": 95.3747833333333, "compass": 5731.0, "image": "random.jpeg"}, {"latitude": 29.76455, "longitude": 95.3748666666667, "compass": 5005.0, "image": "random.jpeg"}, {"latitude": 29.7646666666667, "longitude": 95.3746333333333, "compass": 4732.0, "image": "random.jpeg"}, {"latitude": 29.76475, "longitude": 95.3748, "compass": 4362.0, "image": "random.jpeg"}, {"latitude": 29.76475, "longitude": 95.3749833333333, "compass": 3989.0, "image": "random.jpeg"}, {"latitude": 29.7648166666667, "longitude": 95.3751, "compass": 3161.0, "image": "random.jpeg"}, {"latitude": 29.7647666666667, "longitude": 95.3753, "compass": 2218.0, "image": "random.jpeg"}, {"latitude": 29.7645666666667, "longitude": 95.3770833333333, "compass": 3444.0, "image": "random.jpeg"}, {"latitude": 29.7646666666667, "longitude": 95.3771666666667, "compass": 2851.0, "image": "random.jpeg"}, {"latitude": 29.7644833333333, "longitude": 95.3771666666667, "compass": 2442.0, "image": "random.jpeg"}, {"latitude": 29.7644, "longitude": 95.3771166666667, "compass": 1707.0, "image": "random.jpeg"}, {"latitude": 29.7642166666667, "longitude": 95.3771833333333, "compass": 609.0, "image": "random.jpeg"}, {"latitude": 29.76405, "longitude": 95.3771666666667, "compass": 154.0, "image": "random.jpeg"}, {"latitude": 29.7639833333333, "longitude": 95.3771333333333, "compass": 26.0, "image": "random.jpeg"}, {"latitude": 29.7505833333333, "longitude": 95.3560833333333, "compass": 2402.0, "image": "random.jpeg"}, {"latitude": 29.7505333333333, "longitude": 95.3561, "compass": 1869.0, "image": "random.jpeg"}, {"latitude": 29.75045, "longitude": 95.3561833333333, "compass": 1452.0, "image": "random.jpeg"}, {"latitude": 29.7504166666667, "longitude": 95.3560833333333, "compass": 944.0, "image": "random.jpeg"}, {"latitude": 29.7504, "longitude": 95.3560166666667, "compass": 447.0, "image": "random.jpeg"}, {"latitude": 29.75045, "longitude": 95.35585, "compass": 5797.0, "image": "random.jpeg"}, {"latitude": 29.75045, "longitude": 95.3557833333333, "compass": 5368.0, "image": "random.jpeg"}, {"latitude": 29.7505, "longitude": 95.35565, "compass": 5021.0, "image": "random.jpeg"}, {"latitude": 29.7505166666667, "longitude": 95.3557333333333, "compass": 4714.0, "image": "random.jpeg"}, {"latitude": 29.7506333333333, "longitude": 95.3557333333333, "compass": 4235.0, "image": "random.jpeg"}, {"latitude": 29.75065, "longitude": 95.3557666666667, "compass": 4044.0, "image": "random.jpeg"}, {"latitude": 29.7507166666667, "longitude": 95.3558666666667, "compass": 3624.0, "image": "random.jpeg"}, {"latitude": 29.7507, "longitude": 95.3558833333333, "compass": 3182.0, "image": "random.jpeg"}, {"latitude": 29.7505833333333, "longitude": 95.3557833333333, "compass": 2674.0, "image": "random.jpeg"}, {"latitude": 29.7519, "longitude": 95.3552666666667, "compass": 4097.0, "image": "random.jpeg"}, {"latitude": 29.7518833333333, "longitude": 95.3552166666667, "compass": 4519.0, "image": "random.jpeg"}, {"latitude": 29.7518, "longitude": 95.35525, "compass": 5103.0, "image": "random.jpeg"}, {"latitude": 29.7517333333333, "longitude": 95.3552666666667, "compass": 5425.0, "image": "random.jpeg"}, {"latitude": 29.75165, "longitude": 95.3553333333333, "compass": 5982.0, "image": "random.jpeg"}, {"latitude": 29.7516333333333, "longitude": 95.3554166666667, "compass": 6388.0, "image": "random.jpeg"}, {"latitude": 29.7515833333333, "longitude": 95.35545, "compass": 261.0, "image": "random.jpeg"}, {"latitude": 29.7516166666667, "longitude": 95.3555166666667, "compass": 490.0, "image": "random.jpeg"}]}
    print("read the json")
    data = json_data['data']
    array = []
    images_array = []
    for d in data:
        ut_cordinates = utm.from_latlon(d['latitude'], -d['longitude'])
        t_list = [ut_cordinates[0],ut_cordinates[1],d['compass']*0.05625+2.58]
        images_array.append(d['image'])
        array.append(t_list)
    array = np.array(array)
    images_array = np.array(images_array)
    # print(array)

    X = array[:,[0,1]]
    # print(np.shape(X))
    ms = MeanShift(bandwidth=50)
    labels = ms.fit_predict(X)
    cluster_centers = ms.cluster_centers_
    labels = np.vstack(labels)
    array = np.hstack((array,labels))
    print('Number of clusters ', len(cluster_centers))
    # print(array)

    return_value = []
    for cluster in range(len(cluster_centers)):
    # for cluster in range(1):
        current_cluster_result = {}
        indices_of_cluster = np.where(array[:,3] == cluster)
        cluster_array = array[indices_of_cluster]  
        # print(cluster_array)
        compass_array = cluster_array[:,[2]]
        a = np.tan(np.radians(90-compass_array))
        b = np.ones(np.shape(compass_array))
        c = np.multiply(a,cluster_array[:,[0]]) - cluster_array[:,[1]]
        eq_coeff_cluster = np.hstack((a, -b ,c))
        # we take the value of p as 300 just for analysing the time taken to run this
        # p = 300
        p = 100
        len_of_cluster = len(cluster_array)
        # print('Length of current cluster ', len_of_cluster)
        intersections_of_lines = np.empty([p,2]) # Initializing the intersection of lines numpy array
        for i in range(p):
            idx = np.random.randint(len_of_cluster, size=2)
            lines = eq_coeff_cluster[idx, :]
            # print(idx)
            # print(eq_coeff_cluster)
            # print(lines)
            A = lines[:, [0,1]]
            Y = lines[:, [2]]
            # print('A value is ')
            # print(A)
            # print('Y value is ')
            # print(Y)
            X = np.matmul(np.linalg.pinv(A),  Y)
            X = np.concatenate(X)
            # print(X)
            intersections_of_lines[i,:] = X

        # Performing mean shift clustering and finding the cluster with the maximum number of points
        # This center point is taken as the estimated center of the object
        if len_of_cluster < 2:
            continue
        ms = MeanShift(bandwidth=100)  
        labels = (ms.fit_predict(intersections_of_lines)).tolist()
        cluster_centers = ms.cluster_centers_
        print('Number of clusters ', str(len(cluster_centers)))
        # mode_of_labels = most_common(labels)
        mode_of_labels = max(set(labels), key=labels.count)
        current_cluster_result['cluster_id'] = cluster
        # current_cluster_result['cluster_center'] = (cluster_centers[mode_of_labels]).tolist()
        lat_long = utm.to_latlon(cluster_centers[mode_of_labels][0], cluster_centers[mode_of_labels][1], 15, 'R')
        current_cluster_result['cluster_center_latitude'] = lat_long[0]
        current_cluster_result['cluster_center_longitude'] = lat_long[1]
        current_cluster_result['cluster_images'] = (images_array[indices_of_cluster]).tolist()
        return_value.append(current_cluster_result)
        # print("this is the return value",return_value)
    # print(json.dumps(return_value))
    # return {
    #     'statusCode': 200,
    #     'body': json.dumps(return_value)
    # }
    # print("final json dump", json.dumps(return_value))
    return {
        "statusCode": 200,
        "body": json.dumps({'objects': return_value})
    }


print(lambda_handler({},{}))