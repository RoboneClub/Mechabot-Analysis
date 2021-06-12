from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
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

MagnX = data.iloc[:,10].values
MagnY = data.iloc[:,11].values
MagnZ = data.iloc[:,12].values

Magn_resulatant = []
for i in range(len(MagnX)):
    Magn_resulatant.append((MagnX[i]**2 + MagnY[i]**2 + MagnZ[i] **2)**0.5)

fig = plt.figure(figsize=(12,9))
m = Basemap(projection='mill',
           llcrnrlat = -90,
           urcrnrlat = 90,
           llcrnrlon = -180,
           urcrnrlon = 180,
           resolution = 'c',
           epsg = 4269)
m.axes(projection = '3d')
m.drawcoastlines()
m.plot(long_dd[0:2562],lat_dd[0:2562],color='yellow', latlon = True)
m.plot(long_dd[2562:5019],lat_dd[2562:5019],color='yellow', latlon = True)
m.plot(long_dd[5019:],lat_dd[5019:],color='yellow', latlon = True)
m.drawparallels(np.arange(-90,90,10),labels=[True,False,False,False])
m.drawmeridians(np.arange(-180,180,30),labels=[0,0,0,1])
m.arcgisimage(service='ESRI_Imagery_World_2D', xpixels = 2000, verbose= True)
plt.title(' Experiment runtime ISS orbit', fontsize=20)

plt.show()

