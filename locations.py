import pandas as pd
data=pd.read_csv('data01.csv')
lat_dms = data.iloc[:,2].values
long_dms = data.iloc[:,3].values
pic_no = data.iloc[:,:]
lat_dd = []
for i in lat_dms:
    deg, minutes, seconds =  i.split(':')
    lat_dd.append([(float(deg) + float(minutes)/60 + float(seconds)/(60*60))])
long_dd = []
for i in long_dms:
    deg, minutes, seconds =  i.split(':')
    long_dd.append([(float(deg) + float(minutes)/60 + float(seconds)/(60*60))])

locations = []
coordinates = []
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="GoogleV3")
c = 0
for i,j in zip(lat_dd,long_dd):
    location = geolocator.reverse(str(i[0])+","+str(j[0]))
    if(location not in locations):
        print(location)
        locations.append(location)
        coordinates.append([i,j])
    c = c + 1
    print(f"Progess:{c*100/len(long_dd)}%")
