from crypt import methods
from pickle import GET
from flask import Flask, jsonify, render_template, request


import json
import psycopg2
from psycopg2.extras import Json, DictCursor
import time
from sqlalchemy import create_engine
from functools import lru_cache
import numpy as np
import re
import time
from datetime import datetime, timedelta
import io, os, sys
import pandas as pd
from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)


#### code goes here #### 
### Lets connect to DB #####


conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="neerab")

cursor = conn.cursor()



engine = create_engine('postgresql://postgres:neerab@localhost:5432/postgres',
                      pool_pre_ping=True,
        connect_args={
            "keepalives": 1,
            "keepalives_idle": 30,
            "keepalives_interval": 10,
            "keepalives_count": 5,
        })

#### Intialiaze the positons of each location in College ###

location_info = {"Rec": {40.01297682424832:-105.26951649210318}, 
                 "Umc": {40.011032307369426:-105.27250087765096}, 
                 "EC":  { 40.00695042023822:-105.26285328893621},
                 "Farrand":{40.006177767889234:-105.26760138893619},
                 "East Campus": {40.011342810190605:-105.24930511592252},
                 "Norlin Library":{40.00887311584021:-105.2708269177718},
                 "Kittridge":{40.003051055498446:-105.2595575312652},
                 "Friske":{40.003804637406:-105.26345433126522},
                "Folsom":{40.00957059084623:-105.2669190889362}}



closest_loc = {"Rec": -1, "Umc": -1, "EC": -1, "Farrand":-1,
               "East Campus":-1,
               "Norlin Library":-1,
               "Kittridge":-1,
               "Friske":-1,
               "Folsom":-1}





#### push data ###
def save_answers(user_id, survey_id, question_id, answer):
    cursor.execute("""
          insert into community_data.answer_info(student_id, survey_id, question_id, answer, created_at)
          values(%s,%s,%s,%s,now());""",(user_id, survey_id, question_id, answer))
    conn.commit()



### step 2 to store the user data in the DB ####
@app.route('/store_location', methods = ['POST'])
def store_location():
    data = request.json
    user_id = data['user_id']
    lat     = data['lat']
    lng     = data['lng']
    cursor.execute("""
            insert into community_data.student_location_info(student_id, lat, lng, present_time,created_at)
            values(%s, %s, %s, current_timestamp, now());
            """, (user_id, lat, lng) )
    conn.commit()




@app.route('/add', methods = ['POST'])
def get_data():
    data = request.json
    user_id = data['user_id']
    lat     = data['lat']
    lng     = data['lng']
    store_location(user_id, lat, lng)
    return jsonify({"Hello":"world"})



def get_questions(survey_id):
    cursor.execute("""
                    select * from community_data.survey_info where survey_id = '{}';
                    """.format(survey_id) ),

    data = cursor.fetchall()

    data = pd.DataFrame(data)
    
    return data



### get the most significant location of the user for that day ####

def get_student_data(user_id):
    cursor.execute("""
                select * from community_data.student_location_info;
                """),

    data = cursor.fetchall()
    
    data = pd.DataFrame(data)

    loc_data = data.loc[:,1:2]

    loc_data = loc_data.drop_duplicates()
    
    return loc_data
    

def get_centroid(cluster):
    """calculate the centroid of a cluster of geographic coordinate points
    Args:
      cluster coordinates, nx2 array-like (array, list of lists, etc)
      n is the number of points(latitude, longitude)in the cluster.
    Return:
      geometry centroid of the cluster

    """
    
    cluster_ary = pd.DataFrame(cluster)   
    cluster_ary = cluster_ary.astype(float)
    centroid = cluster_ary.mean(axis=0, skipna = False)  
    return centroid

##### Gets each user most of the time in the previous day ######
def userMostTime(loc_data):
    clusters = DBSCAN(min_samples = 2, eps = 3)

    clusters = clusters.fit(loc_data)

    y_pred = clusters.fit_predict(loc_data)



    fac_cluster_labels = clusters.labels_
    # get the number of clusters

    values = np.unique(fac_cluster_labels,return_counts=True)

    k,v = max(zip(*values),key=lambda x:x[1])

    #### The cluster with the maxmium time that day, get the mean of the data ###

    dbsc_clusters = pd.Series([loc_data[fac_cluster_labels == k]])



    '''
    num_clusters = len(set(clusters.labels_))
    # turn the clusters into a pandas series,where each element is a cluster of points
    dbsc_clusters = pd.Series([loc_data[fac_cluster_labels == n] for n in range(num_clusters)])

    '''
    #print(dbsc_clusters)

    # get centroid of each cluster
    fac_centroids = dbsc_clusters.map(get_centroid)






    # unzip the list of centroid points (lat, lon) tuples into separate lat and lon lists
    cent_lats, cent_lons = zip(*fac_centroids)

    centroids_pd = pd.DataFrame({'latitude':cent_lats, 'longitude':cent_lons})



    '''
    ### plotting graphs

    # from these lats/lons create a new df of one representative point for eac cluster
    centroids_pd = pd.DataFrame({'latitude': cent_lats, 'longitude': cent_lons})
    # Plot the student clusters and cluster centroid
    fig, ax = plt.subplots(figsize=[20, 10])
    facility_scatter = ax.scatter(loc_data.loc[:,1], loc_data.loc[:,2], c=fac_cluster_labels,
                                  edgecolor='None', alpha=0.7, s=120)
    centroid_scatter = ax.scatter(centroids_pd['longitude'], centroids_pd['latitude'], marker='x', linewidths=2,
                                  c='k', s=50)
    ax.set_title('Student Clusters & Student Centroid', fontsize=30)
    ax.set_xlabel('Latitude', fontsize=24)
    ax.set_ylabel('Longitude', fontsize=24)
    ax.legend([facility_scatter, centroid_scatter], ['Cluster', 'Cluster Centroid'], loc='upper right',
              fontsize=20)


    '''
    '''

    plt.scatter(loc_data.loc[:,1], loc_data.loc[:,2],c=y_pred, cmap='Paired')
    plt.title("Location")

    print(y_pred)
    '''
    
    return centroids_pd


### After getting user location, send the survey related to his location ####

### get the closest distance to the user ###

from heapq import nsmallest

'''
SQRT(
POW(69.1 * (latitude - [startlat]), 2) +
POW(69.1 * ([startlng] - longitude) * COS(latitude / 57.3), 2)
'''
import re 
import math
def find_closest(pos):
    cur_lat = pos['latitude']
    cur_lng = pos['longitude']
    for p,v in location_info.items():
        v = str(v)
        v = re.split('\{|:|\}', v)
        lat = float(v[1])
        lng = float(v[2].split(" ")[1])
        x = math.sqrt(math.pow(69.1*(cur_lat-lat),2)+math.pow(69.1*(lng-cur_lng)*math.cos(cur_lat/57.3),2))
        closest_loc[p] = x
    loc = sorted(closest_loc.items(), key=lambda item: item[1])
    #min(closest_loc, key=closest_loc.get)
    loc = loc[:3]
    closest = []
    for x in loc:
        closest.append(x[0])
    return closest[0]
        

#### send questions to that specific user at that specific location #######
@app.route('/get_questions', methods=['POST'])
def questions():

    data = request.json
    user_id = data['user_id'] #### get the student id
    print(user_id)
    #user_id = 'neerab'
    pos = userMostTime(get_student_data(user_id))
    place = find_closest(pos)  ### once you got the place we will send the questions with respect to survey_id
    '''
    val = "("
    for x in place:
        val += "'"+x+"',"
    '''
    cursor.execute("""
                    select si.survey_id , qi.question_id , question, qo.options  from community_data.survey_info si 
                    join community_data.question_info qi on si.question_id  = qi.question_id 
                    join community_data.location_survey ls on ls.survey_id = si.survey_id 
                    join community_data.question_options qo on qo.question_id = qi.question_id 
                    where ls.locname = '{}' ;
                    """.format(place))

    #format(val[:-1]+")")),
    data = cursor.fetchall()

    data = pd.DataFrame(data)

    questions = []

    for i in range(len(data)):
        option = data.loc[i][3]
        opt = []
        for j in range(len(option)):
            opt.append({"value": option[j]})
        questions.append({"survey_id": data.loc[i][0], "question_id": data.loc[i][1], "question": data.loc[i][2],"options": opt })

    
    return json.dumps(questions)

@app.route('/test_data', methods=['GET'])
def submit_answers():
      return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

#### send questions to that specific user at that specific location #######
@app.route('/get_answers', methods=['POST'])
def submit_answers():
    print("Hello")
    data = request.json

    survey_id = data['survey']
    answers = data['backendData']

    from collections import defaultdict

    value = {}

    for answer in answers:
        for key, v in answer.items():
            value[key] = v
        
    for question_id, option in value.items():
        save_answers("akhil", survey_id, question_id, option)
        

    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}








app.run(host="0.0.0.0", port=5000,use_reloader=True, debug=True)



