import json
import requests
import numpy as np
from sklearn.cluster import MeanShift
import utm
import math
def lambda_handler(event, context):
    url = 'http://18.236.117.181:8081/'
    response = requests.get(url).json()
    json_data = {"count":30,"data":[{"latitude":83,"longitude":113,"compass":23,"image":"images/inlet.jpg"},{"latitude":80,"longitude":98,"compass":56,"image":"images/drain.jpg"},{"latitude":83,"longitude":97.2,"compass":51,"image":"images/storm-drain.jpg"},{"latitude":81,"longitude":97.2,"compass":51,"image":"images/storm-drain.jpg"},{"latitude":67,"longitude":97.2,"compass":51,"image":"images/storm.jpg"},{"latitude":76,"longitude":97.2,"compass":51,"image":"images/mesh.jpg"},{"latitude":70,"longitude":97.2,"compass":51,"image":"images/drainage.jpg"},{"latitude":71,"longitude":97.2,"compass":51,"image":"images/vulnerable.jpg"},{"latitude":76.577,"longitude":97.2,"compass":51,"image":"images/building.jpg"},{"latitude":75.577,"longitude":97.2,"compass":51,"image":"images/vul-buil.jpg"},{"latitude":56.577,"longitude":97.2,"compass":51,"image":"images/demolish.jpeg"},{"latitude":56.577,"longitude":97.2,"compass":51,"image":"images/los-angeles.jpg"},{"latitude":46.577,"longitude":97.2,"compass":51,"image":"images/undo.png"},{"latitude":36.577,"longitude":97.2,"compass":51,"image":"images/buildings.jpeg"},{"latitude":26.577,"longitude":97.2,"compass":55,"image":"images/buildings.jpeg"},{"latitude":76.577,"longitude":97.2,"compass":55,"image":"images/demolition contractors in doylestown pa.jpg"},{"latitude":78,"longitude":99,"compass":98,"image":"images/earth.jpg"},{"latitude":60,"longitude":99,"compass":98,"image":"images/earth.jpg"},{"latitude":40,"longitude":99,"compass":98,"image":"images/earth.jpg"},{"latitude":30.4447461,"longitude":-97.8020798,"compass":5.53125,"image":"images/image.jpeg"},{"latitude":30.4447506,"longitude":-97.8021049,"compass":240.15625,"image":"images/image.jpeg"},{"latitude":56.577,"longitude":97.2,"compass":55,"image":"images/random.jpeg"},{"latitude":57.577,"longitude":97.2,"compass":55,"image":"images/image.jpeg"},{"latitude":30.444773,"longitude":-97.8020652,"compass":19.765625,"image":"images/image.jpeg"},{"latitude":30.4447667,"longitude":-97.8020813,"compass":35.21875,"image":"images/image.jpeg"},{"latitude":30.4447466,"longitude":-97.8020764,"compass":27.234375,"image":"images/1576690321863"},{"latitude":30.4447557,"longitude":-97.8020835,"compass":20.171875,"image":"images/1576690421938"},{"latitude":30.4447574,"longitude":-97.8020849,"compass":36.28125,"image":"images/1576690545399.jpeg"},{"latitude":30.4447658,"longitude":-97.80209,"compass":359.453125,"image":"images/1576690662798.jpeg"},{"latitude":30.4447475,"longitude":-97.8020795,"compass":81.9375,"image":"images/1576690695265.jpeg"}]}
    data = json_data['data']
    array = []
    for d in data:
        ut_cordinates = utm.from_latlon(d['latitude'], d['longitude'])
        t_list = [ut_cordinates[0],ut_cordinates[1],d['compass']]
        array.append(t_list)
    array = np.array(array)
    X = array[:,[0,1]]
    ms = MeanShift()
    labels = ms.fit_predict(X)
    cluster_centers = ms.cluster_centers_
    # Calculating the coefficients of ax+by=c
    a = np.tan(np.radians(90-array[:,2]))
    # return {
    #     'statusCode': 200,
    #     'body': json.dumps(response)
    # }

print(lambda_handler({},{}))