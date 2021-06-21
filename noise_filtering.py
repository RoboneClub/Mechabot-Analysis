import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data01.csv')
time = data['Time']
MagnX = data.iloc[:,10].values
MagnY = data.iloc[:,11].values
MagnZ = data.iloc[:,12].values
Magn = np.transpose(np.array((MagnX,MagnY,MagnZ)))
#Using the sensor data LSM9DS1
s = 0.043; #Senstivity 0.15 microtesla
c = [[1,s,s],
    [s,1,s],
    [s, s, 1]]
c = np.linalg.inv(c) #Crosstalk --> inverse to divide the data on crosstalk
frequency = 20 
noise_rms = 3.2 * 10**-3 * frequency**0.5

noise = np.random.randn(len(MagnX),1) * noise_rms
Magn = Magn - noise

plt.plot(Magn)
plt.show()

