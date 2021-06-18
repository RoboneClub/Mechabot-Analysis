"""
import json
# import requests module
import requests
from requests.auth import HTTPBasicAuth

# Making a get request
response = requests.get('https://api.meteomatics.com/2021-06-18T00:00:00Z/t_2m:C/52.520551,13.461804/json',
            auth = HTTPBasicAuth('robone_hassaballa', 'S10bomEwY9hAO'))
x = response.json()
value = x['data'][0]['coordinates'][0]['dates'][0]['value']

print(x)
response = requests.get('https://api.meteomatics.com/2019-05-05T00:00:00Z--2021-05-05T00:00:00Z:PT8760H/t_2m:C/52.520551,13.461804/json',
            auth = HTTPBasicAuth('robone_hassaballa', 'S10bomEwY9hAO'))
x = response.json()
value = x['data'][0]['coordinates'][0]['dates'][0]['value']
"""

import pandas as pd
data=pd.read_csv('data01.csv')
lat_dms = data.iloc[:,2].values
long_dms = data.iloc[:,3].values
lat_dd = []
for i in lat_dms:
    deg, minutes, seconds =  i.split(':')
    print(f"degree: {deg}, minutes: {minutes}, seconds: {seconds}")
    lat_dd.append([(float(deg) + float(minutes)/60 + float(seconds)/(60*60))])
long_dd = []
for i in long_dms:
    deg, minutes, seconds =  i.split(':')
    print(f"degree: {deg}, minutes: {minutes}, seconds: {seconds}")
    long_dd.append([(float(deg) + float(minutes)/60 + float(seconds)/(60*60))])

import requests
lat = lat_dd[1100]
long = long_dd[1100]
date = '2019-05-05'
response = requests.get(f"https://api.worldweatheronline.com/premium/v1/past-weather.ashx?key=4604ce6dc9974503bb5152326211806&q={lat},{long}&date={date}&format=json")
print(response.json()['data']['weather'][0]['avgtempC'])
