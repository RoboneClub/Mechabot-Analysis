import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
import pandas as pd

data = pd.read_csv('data01.csv')
time = data.iloc[:,1].values
MagnX = data.iloc[:,10].values
MagnY = data.iloc[:,11].values
MagnZ = data.iloc[:,12].values
lat_dms = data.iloc[:,2].values
long_dms = data.iloc[:,3].values
lat_dd = []

for i in lat_dms:
    deg, minutes, seconds =  i.split(':')
    print(f"degree: {deg}, minutes: {minutes}, seconds: {seconds}")
    lat_dd.append(float(deg) + float(minutes)/60 + float(seconds)/(60*60))
long_dd = []
for i in long_dms:
    deg, minutes, seconds =  i.split(':')
    print(f"degree: {deg}, minutes: {minutes}, seconds: {seconds}")
    long_dd.append(float(deg) + float(minutes)/60 + float(seconds)/(60*60))

Magn_resulatant = []
for i in range(len(MagnX)):
    Magn_resulatant.append((MagnX[i]**2 + MagnY[i]**2 + MagnZ[i] **2)**0.5)

total = 0
for i in Magn_resulatant:
    total += i
mean = total/len(Magn_resulatant)
mean_arr = []
for i in range(len(Magn_resulatant)):
    mean_arr.append(mean)

sum_sd = 0
for i in Magn_resulatant:
    sum_sd += (i-mean)**2
sd = (sum_sd/(len(Magn_resulatant) - 1))**0.5
sd_arr = []
for i in range(len(Magn_resulatant)):
    sd_arr.append(sd)

#plt.axes(projection='3d')

#plt.plot(long_dd,lat_dd,MagnX,label='MagnX')
#plt.plot(long_dd,lat_dd,MagnY,label='MagnY')
#plt.plot(long_dd,lat_dd,MagnZ,label='MagnZ')
#plt.plot(long_dd,lat_dd,Magn_resulatant,label='Magn_resultant')
plt.plot(np.arange(0,len(MagnX),1),MagnX,label='MagnX')
plt.plot(np.arange(0,len(MagnX),1),MagnY,label='MagnY')
plt.plot(np.arange(0,len(MagnX),1),MagnZ,label='MagnZ')
plt.legend()
plt.show()
plt.plot(np.arange(0,len(MagnX),1),Magn_resulatant,label='MagnResultant')
plt.plot(np.arange(0,len(MagnX),1),mean_arr,label='Mean')
plt.plot(np.arange(0,len(MagnX),1),sd_arr,label='Standard Deviation')
plt.legend()
plt.show()
