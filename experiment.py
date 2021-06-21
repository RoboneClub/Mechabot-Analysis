from datetime import datetime,timedelta
import API
import map
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

points_of_study = [78, 179, 447, 597, 689, 771, 833, 953, 1037, 1125, 3974, 4037, 4075, 4133, 4155, 4180, 4197, 4234, 4271, 4286]

data = pd.read_csv('data01.csv')
imgs = data.iloc[points_of_study]['ImgNo'].values
long = data.iloc[points_of_study]['Longitude'].values
lat = data.iloc[points_of_study]['Latitude'].values
date = data.iloc[points_of_study]['Date'].values

long = map.dms2dd(long)
lat = map.dms2dd(lat)
#map.plot(long,lat,"Points of interest")
period = datetime.strptime('05/05/2021','%d/%m/20%y') - timedelta(365)

x = API.get_weather_data(lat, long, date)
x = np.array(x)
np.save("avg_temp.npy", x,allow_pickle=True)
np.save("avg_temp2.npy", x,allow_pickle=False)
