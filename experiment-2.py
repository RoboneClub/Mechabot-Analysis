"""
This expirment tests whether or not the magnetic field affects the objects in 
the LEO by correlating the resultant intensity of the magnetic field with the 
accelertaion and angular velocity of the ISS
"""


""" Importing the libraries and the modules """
from datetime import datetime,timedelta
import magn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import noise_filtering
import plot

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
magn_resultant = magn.get_resultant(magnX,magnY,magnZ)
accX = data.iloc[:,13].values
accY = data.iloc[:,14].values
accZ = data.iloc[:,15].values
acc_resultant = magn.get_resultant(accX,accY,accZ)



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

acc_filtered_resultant = magn.get_resultant(acc_filtered_matrix[:,0],acc_filtered_matrix[:,1],acc_filtered_matrix[:,2])

''' 3- Calculating the resultant magnitude, the standard deviation, the mean and the autocorrelation of the points
for the filtered and unfiltered magnetic field, acceleration, and angular velocity'''

gyroX_sd = magn.get_sd(gyroX_filtered)
gyroY_sd = magn.get_sd(gyroY_filtered)
gyroZ_sd = magn.get_sd(gyroZ_filtered)
gyro_sd_mean = magn.get_mean_3(gyroX_sd, gyroY_sd, gyroZ_sd)

gyroX_mean = magn.get_mean(gyroX_filtered)
gyroY_mean = magn.get_mean(gyroY_filtered)
gyroZ_mean = magn.get_mean(gyroZ_filtered)
gyro_mean_mean = magn.get_mean_3(gyroX_mean, gyroY_mean, gyroZ_mean)

magn_sd = magn.get_sd(magn_filtered_resultant)
magn_mean = magn.get_mean(magn_filtered_resultant)
magn_autocorrelation = magn.autocor(magn_filtered_resultant)

acc_sd = magn.get_sd(acc_filtered_resultant)
acc_mean = magn.get_mean(acc_filtered_resultant)
acc_autocorrelation = magn.autocor(acc_filtered_resultant)
acc_autocorrelation_pure = magn.autocor(acc_resultant)

'''4- Plotting the Autocorrelation'''
#plots accelerometer data
plt.title("Accelerometer Data")
plt.xlabel("Reading number")
plt.ylabel("Acceleration/g")
plt.plot(acc_filtered_resultant,label='AccResultant')
plt.plot([acc_mean]*len(accX),label='Mean')
plt.plot([acc_sd]*len(accX),label='Standard Deviation')
plt.legend()
plt.show()

plt.plot(acc_autocorrelation, label = "Noise filtered acceleration readings autocorrelation")
plt.plot(acc_autocorrelation_pure, label= "Raw  acceleration readings autocorrelation")
plt.xlabel("Readings number")
plt.ylabel("Autocorrelation value")
plt.title("Auto correlation of Resultant Acceleration")
plt.legend()
plt.show()

#plots magnetometer data
plt.title("Magnetometer Data")
plt.ylabel("Magnetic Intensity/µT")
plt.xlabel("Reading number")
plt.plot(magn_filtered_resultant,label='MagnResultant')
plt.plot([magn_mean]*len(magnX),label='Mean')
plt.plot([magn_sd]*len(magnX),label='Standard Deviation')
plt.legend()
plt.show()
#plots autocorrelation data
plot.plot_2d(np.arange(0,len(magn_filtered_resultant),1),'Reading number',[np.append(magn_autocorrelation,magn_autocorrelation[-1])],'Autocorrelation of magnetic field',[magn_filtered_resultant],"Resultant Magnetic field Intensity/µT")






"""_______________________ Part 2: Comparing and correlating data ______________________"""


'''1- Plotting the correlations '''

magn_acc_cor = magn.cor(magn_filtered_resultant, acc_filtered_resultant)

#plots correlation data
plt.title("Correlation between Acceleration and Magnetic Intensity")
plt.xlabel("Reading number")
plt.plot(magn_acc_cor)
plt.ylabel("Correlation value")
plt.legend()
plt.show()

magn_gyroX_cor = magn.cor(magn_filtered_resultant, gyroX_filtered)

#plots correlation data
plt.title("Correlation between Angular velocity in X-axis and Magnetic Intensity")
plt.xlabel("Reading number")
plt.plot(magn_gyroX_cor)
plt.ylabel("Correlation value")
plt.legend()
plt.show()

magn_gyroY_cor = magn.cor(magn_filtered_resultant, gyroY_filtered)

#plots correlation data
plt.title("Correlation between Angular velocity in Y-axis and Magnetic Intensity")
plt.xlabel("Reading number")
plt.plot(magn_gyroY_cor)
plt.ylabel("Correlation value")
plt.legend()
plt.show()

magn_gyroZ_cor = magn.cor(magn_filtered_resultant, gyroZ_filtered)

#plots correlation data
plt.title("Correlation between Angular velocity in Z-axis and Magnetic Intensity")
plt.xlabel("Reading number")
plt.plot(magn_gyroZ_cor)
plt.ylabel("Correlation value")
plt.legend()
plt.show()
