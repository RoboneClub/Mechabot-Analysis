from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

stations=pd.read_csv('Weather_Radar_Stations.csv')
stations_lat = stations.iloc[:,1].values
stations_long = stations.iloc[:,0].values
near_stations = pd.read_csv('near_stations.csv')
near_stations_long = near_stations.iloc[:,1].values
near_stations_lat = near_stations.iloc[:,2].values
stations_id = stations.iloc[:,3].values
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

fig = plt.figure(figsize=(12,9))
in_USA_X = []
in_USA_Y = []
for i in range(len(lat_dd)):
    if(long_dd[i][0]> -125 and long_dd[i][0]< -60 and lat_dd[i][0]>14 and lat_dd[i][0]<48):
        in_USA_X.append(long_dd[i])
        in_USA_Y.append(lat_dd[i])
"""
For finding the nearest station to our orbit in USA
near_stations = []
near_stations_lat = []
near_stations_long = []
for i in range(len(in_USA_X)):
    shortest = 9999
    shortest_station_name = ''
    shortest_station_lat = 0
    shortest_station_long = 0 
    for j in range(len(stations_lat)):
        distance = ((in_USA_X[i] - stations_long[j])**2+(in_USA_Y[i] - stations_lat[j])**2)**0.5
        if(distance < shortest):
            shortest = distance
            shortest_station_name = stations_id[j]
            shortest_station_long = stations_long[j]
            shortest_station_lat = stations_lat[j]

    
    if not(shortest_station_name in near_stations):
        near_stations.append(shortest_station_name)
        near_stations_lat.append(shortest_station_lat)
        near_stations_long.append(shortest_station_long)
    print(f"Done {i}/{len(in_USA_X)}")
"""
m = Basemap(projection='mill',
           llcrnrlat = -90,
           urcrnrlat = 90,
           llcrnrlon = -180,
           urcrnrlon = 180,
           resolution = 'c',
           epsg = 4269)

m.drawcoastlines()
m.scatter(near_stations_long,near_stations_lat,color='red',s=10, latlon = True)
m.plot(long_dd[0:2562],lat_dd[0:2562],color='yellow', latlon = True)
m.plot(long_dd[2562:5019],lat_dd[2562:5019],color='yellow', latlon = True)
m.plot(long_dd[5019:],lat_dd[5019:],color='yellow', latlon = True)
m.drawparallels(np.arange(-90,90,10),labels=[True,False,False,False])
m.drawmeridians(np.arange(-180,180,30),labels=[0,0,0,1])
m.arcgisimage(service='ESRI_Imagery_World_2D', xpixels = 2000, verbose= True)

plt.title(' Experiment runtime ISS orbit', fontsize=20)

plt.show()

