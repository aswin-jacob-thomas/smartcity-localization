import numpy as np
import csv 
from geopy.distance import geodesic
import json
import time
import pymongo

# requirement numpy geopy pymango pymango[srv] dnspython

### Algorithm for network analysis
def decay_depth(time):
    if time > 0 and time < 3.76:
        return 0
    return 0.57 * (time - 3.76)

def resistance(decay_depth):
    return 0.005436125* ((260 - (2*decay_depth)) ** 3)

def area_pole(age):
    return (0.26 - decay_depth(age)/100) * 11.7

def lambda_handler(event, context):

    if (event["queryStringParameters"] is None) or  ("windspeed" not in event["queryStringParameters"]):
        body = json.dumps({"Error":"Please pass the windspeed to perform network analysis"})
        return {
        'statusCode': 200,
        'body': body
    }

    wind = int(event["queryStringParameters"]['windspeed'])
    fields = [] 
    rows = [] 
    # For storing the extra tension from its neighbors
    client = pymongo.MongoClient("mongodb+srv://user:pass@cluster0-rhzye.mongodb.net/test")
    db = client["test"]
    collection = db["poles"]

    documents = collection.find()
    poles = []
    
    for doc in documents:
        poles.append(doc)

    extra_tension_moment = [0] * len(poles)
    extra_tension_moment = np.array(extra_tension_moment)
    failed = [0] * len(poles)
    failed = np.array(failed)

    condition = True
    iteration = 0
    idArray = []

    while(condition == True):

        iteration += 1

        any_new_failures = False
        for index, pole in enumerate(poles):

            if failed[index] == 1:
                continue

            age = pole['age_10to30']
            angle = pole['angle_3to21']
            s1 = pole['s1']
            s2 = pole['s2']
            fw = pole['fw']
            bw = pole['bw']
            group = pole['group']

            area_of_pole = (0.26 - decay_depth(age)/100) * 11.7
            area_of_conductor = 3 * 0.018 * (s1+s2)/2 
            wind_load_by_pole = 0.613 * wind * wind * 0.98 * 0.96 * area_of_pole
            wind_load_by_conductor = 0.613 * wind * wind * 1.05 * 0.81 * area_of_conductor
            overturning_load = 4466 * np.sin(np.radians(angle))
            bending_moment_by_wind_load = wind_load_by_pole * (11.7/2) * np.cos(np.radians(angle)) + (wind_load_by_conductor * 11.7)
            overturning_moment = overturning_load * (11.7/2) * np.cos(np.radians(angle))
            current_extra_tension_moment_backward = (bw) * 11.7
            current_extra_tension_moment_forward = (fw) * 11.7

            moment = overturning_moment + bending_moment_by_wind_load + extra_tension_moment[index]
            resistance_value = resistance(decay_depth(age))

            uncertainity = 0.88
            if uncertainity * resistance_value < moment:
                any_new_failures = True
                failed[index] = 1

                if index-1 >= 0 and failed[index-1] == 0 and group == poles[index-1]['group']:
                    extra_tension_moment[index-1] += current_extra_tension_moment_forward

                if index+1 < len(poles) and failed[index+1] == 0 and group == poles[index+1]['group']:
                    extra_tension_moment[index+1] += current_extra_tension_moment_backward
                extra_tension_moment[index] = 0

            condition = np.count_nonzero(extra_tension_moment) > 0 and any_new_failures

    failedPoles = np.where(failed == 1)[0] + 1
    return {
        'statusCode': 200,
        'body': json.dumps({'failedpoles':failedPoles.tolist()})
    }

print(lambda_handler({'queryStringParameters': {'windspeed' : 35}},{}))