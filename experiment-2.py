""" Importing the libraries and the modules """
from datetime import datetime,timedelta
#import API
import magn
#import map
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import noise_filtering

"""_______________________ Part 1: Analyzing the IMU sensor data _______________________"""


''' 1-Importing the IMU sensor data '''

#Imports the whole data from the csv using pandas library
data = pd.read_csv('data01.csv')

#Takes the time, gyroscope, magnometer, and accelerometer X, Y, and Z readings from the dataset:
time = data.iloc[:,1].values
gyroX = data.iloc[:,7].values
gyroY = data.iloc[:,8].values
gyroZ = data.iloc[:,9].values
magnX = data.iloc[:,10].values
magnY = data.iloc[:,11].values
magnZ = data.iloc[:,12].values
accX = data.iloc[:,13].values
accY = data.iloc[:,14].values
accZ = data.iloc[:,15].values



''' 2-Preprocessing the data by applying noise filteration '''

gyro_filtered_matrix = noise_filtering.noise_filtering(gyroX,gyroY,gyroZ,sensitivity = (0.0175), frequency = 476,  rms = (3.2 * 10**-3) )
    #Senstivity and Frequency are according to https://www.st.com/resource/en/datasheet/lsm9ds1.pdf
magn_filtered_matrix = noise_filtering.noise_filtering(magnX,magnY,magnZ,sensitivity = 0.043, frequency = 20,  rms = (3.2 * 10**-3) )
    #Senstivity and Frequency are according to https://www.st.com/resource/en/datasheet/lsm9ds1.pdf
    #RMS Noise assumtion according to https://www.st.com/resource/en/datasheet/lis3mdl.pdf which is a similar build
acc_filtered_matrix = noise_filtering.noise_filtering(accX,accY,accZ,sensitivity = (0.000244*9.81), frequency = 10,  rms = (3.2 * 10**-3) )
    #Senstivity and Frequency are according to https://www.st.com/resource/en/datasheet/lsm9ds1.pdf

gyroX_filtered = gyro_filtered_matrix[:,0]
gyroY_filtered = gyro_filtered_matrix[:,1]
gyroZ_filtered = gyro_filtered_matrix[:,2]

magn_filtered_resultant = magn.get_resultant(magn_filtered_matrix[:,0],magn_filtered_matrix[:,1],magn_filtered_matrix[:,2])
#magnX_filtered = magn_filtered_matrix[:,0]
#magnY_filtered = magn_filtered_matrix[:,1]
#magnZ_filtered = magn_filtered_matrix[:,2]

acc_filtered_resultant = magn.get_resultant(acc_filtered_matrix[:,0],acc_filtered_matrix[:,1],acc_filtered_matrix[:,2])
#accX_filtered = acc_filtered_matrix[:,0]
#accY_filtered = acc_filtered_matrix[:,1]
#accZ_filtered = acc_filtered_matrix[:,2]

''' 3- Calculating the resultant magnitude, the standard deviation, the mean and the auto corelation of the points
for the magnetic field, and the acceleration, and the angular rate'''

gyroX_sd = magn.get_sd(gyroX_filtered)
gyroY_sd = magn.get_sd(gyroY_filtered)
gyroZ_sd = magn.get_sd(gyroZ_filtered)
gyro_sd_mean = magn.get_mean_3(gyroX_sd, gyroY_sd, gyroZ_sd,)

gyroX_mean = magn.get_mean(gyroX_filtered)
gyroY_mean = magn.get_mean(gyroY_filtered)
gyroZ_mean = magn.get_mean(gyroZ_filtered)
gyro_mean_mean = magn.get_mean_3(gyroX_mean, gyroY_mean, gyroZ_mean,)

magn_sd = magn.get_sd(magn_filtered_resultant)
magn_mean = magn.get_mean(magn_filtered_resultant)
#magn_autocorrelation = magn.autocor(magn_filtered_resultant)

acc_sd = magn.get_sd(acc_filtered_resultant)
acc_mean = magn.get_mean(acc_filtered_resultant)
#acc_autocorrelation = magn.autocor(acc_filtered_resultant)

'''4- Plotting the graphs '''

#Adjusting the format of the time for the x-axis by flooring the seconds to remove the seconds fraction
for i in range(len(time)):
    time[i] = time[i].split('.')[0]
"""
plt.title("Magnometer Readings")
plt.xlabel("Time")
plt.ylabel("Magnetic Intensity/µT")
plt.plot(time,magnX,label='MagnX')
plt.plot(time,magnY,label='MagnY')
plt.plot(time,magnZ,label='MagnZ')
plt.legend()
plt.show()
"""

#plots accelerometer data
"""
plt.title("Accelerometer Data")
plt.xlabel("Time")
plt.ylabel("Acceleration/g")
plt.plot(time,acc_filtered_resultant,label='AccResultant')
plt.plot(time,[acc_mean]*len(accX),label='Mean')
plt.plot(time,[acc_sd]*len(accX),label='Standard Deviation')
plt.legend()
plt.show()

#plots magnetometer data
plt.title("Magnetometer Data")
plt.xlabel("Time")
plt.ylabel("Magnetic Intensity/µT")
plt.plot(time,magn_filtered_resultant,label='MagnResultant')
plt.plot(time,[magn_mean]*len(magnX),label='Mean')
plt.plot(time,[magn_sd]*len(magnX),label='Standard Deviation')
plt.legend()
plt.show()

"""
magn_acc_cor = magn.cor(magn_filtered_resultant, acc_filtered_resultant)

#plots correlation data
plt.title("Correlation between Acceleration and Magnetic Intensity")
plt.xlabel("Time")
plt.plot(time,magn_acc_cor,label='Correlation')
plt.legend()
plt.show()
