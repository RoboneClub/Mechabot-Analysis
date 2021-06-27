""" Importing the libraries and the modules """
from datetime import datetime,timedelta
import API
import magn
import map
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

magn_filtered_matrix = noise_filtering.noise_filtering(magnX,magnY,magnZ,sensitivity = 0.043, frequency = 20,  rms = (3.2 * 10**-3) )
    #Senstivity and Frequency are according to https://www.st.com/resource/en/datasheet/lsm9ds1.pdf
    #RMS Noise assumtion according to https://www.st.com/resource/en/datasheet/lis3mdl.pdf which is a similar build
acc_filtered_matrix = noise_filtering.noise_filtering(accX,accY,accZ,sensitivity = (0.244*9.81/1000), frequency = 10,  rms = (3.2 * 10**-3) )
    #Senstivity and Frequency are according to https://www.st.com/resource/en/datasheet/lsm9ds1.pdf



''' 3- Calculating the resultant magnitude, the standard deviation, the mean and the auto corelation of the points
for the magnetic field, and the acceleration'''

magn_resultant = magn.get_resultant(magn_filtered_matrix[:,0],magn_filtered_matrix[:,1],magn_filtered_matrix[:,2])
magn_sd = magn.get_sd(magn_resultant)
magn_mean = magn.get_mean(magn_resultant)
magn_autocorrelation = magn.autocor(magn_resultant)

acc_resultant = magn.get_resultant(acc_filtered_matrix[:,0],acc_filtered_matrix[:,1],acc_filtered_matrix[:,2])
acc_sd = magn.get_sd(acc_resultant)
acc_mean = magn.get_mean(acc_resultant)
acc_autocorrelation = magn.autocor(acc_resultant)

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
plt.title("Accelerometer Data")
plt.xlabel("Time")
plt.ylabel("Acceleration/g")
plt.plot(time,acc_resultant,label='AccResultant')
plt.plot(time,[acc_mean]*len(accX),label='Mean')
plt.plot(time,[acc_sd]*len(accX),label='Standard Deviation')
plt.legend()
plt.show()

#plots magnetometer data
plt.title("Magnetometer Data")
plt.xlabel("Time")
plt.ylabel("Magnetic Intensity/µT")
plt.plot(time,magn_resultant,label='MagnResultant')
plt.plot(time,[magn_mean]*len(magnX),label='Mean')
plt.plot(time,[magn_sd]*len(magnX),label='Standard Deviation')
plt.legend()
plt.show()


magn_acc_cor = magn.cor(magn_resultant, acc_resultant)

#plots correlation data
plt.title("Correlation between Acceleration and Magnetic Intensity")
plt.xlabel("Time")
plt.plot(time,magn_acc_cor,label='Correlation')
plt.legend()
plt.show()



"""



'''_______________________ Part 2: Extracting 20  points to preform the research on _______________________'''

''' 0-The chosen points: '''
#Indices of the chosen points:
points_of_study = [78, 179, 447, 597, 689, 771, 833, 953, 1037, 1125, 3974, 4037, 4075, 4133, 4155, 4180, 4197, 4234, 4271, 4286]

'''1-Extracting the location of these points from the dataset'''
long_dms = data.iloc[points_of_study]['Longitude'].values
lat_dms = data.iloc[points_of_study]['Latitude'].values

#Changing the format of the location longitude and latitude from Degree Minutes Seconds to Decimal Degress 
long_dd = map.dms2dd(long_dms)
lat_dd = map.dms2dd(lat_dms)

'''2-Marking the Study Points on the Map'''
#map.plot(long_dd,lat_dd,'Study Points')

#Getting the image numbers for the images of the chosen locations
imgs = data.iloc[points_of_study]['ImgNo'].values
print(f"\n \n {'='*100}\n  Make sure to Check out images: \n{imgs}\n to see the images corresponding to the chosen points \n{'='*100}\n\n\n\n")


'''3-Extract the magnetic field readings corresponding to the chosen indices for the study:'''
magn_points_of_study = pd.DataFrame({'col':magn_resultant}).iloc[points_of_study].values.flatten(order='C')



'''4-Get the magnometic values history for 10 years of each location '''
#https://www.pnas.org/content/115/20/5111#:~:text=Abstract,since%201600%20or%20even%20earlier.


magn_history = magn.get_magn_history(magn_points_of_study,decay = 0.0005)




''''''_______________________ Part 3: Fetching the weather history data for the study points _______________________'''

'''Importing the date for the Points'''
date = data.iloc[points_of_study]['Date'].values

'''1-Downloading the weather data for the last 10 years for each point using the API'''
#weather_data = API.get_weather_data(lat_dd, long_dd, date)

'''1.5-Saving the downloaded data in a numpy file '''
#np.save("weather_data.npy",weather_data)
#For loading the file use 'np.load("weather_data.npy",allow_pickle=True)'
weather_data = np.load("weather_data.npy",allow_pickle=True)

'''2-Extract each variable from the downloaded data'''
avg_temp = API.get_avg_temp(weather_data)
avg_wind_speed = API.get_avg_wind_speed(weather_data)
avg_uv_index = API.get_uv_index(weather_data)
avg_precip = API.get_avg_precipitation(weather_data)
avg_humidity = API.get_avg_humidity(weather_data)






'''_______________________ Part 4: Comparing the Magnometer values with  the weather history data for each of the study points _______________________'''
import plot
x_axis = np.arange(2012,2022,1)
plot.plot_2d(x_axis,'Year',avg_temp,'Average Temperature of day',magn_history,'Magnetic field intensity/µT')
plot.plot_2d(x_axis,'Year',avg_wind_speed,'Average wind speed',magn_history,'Magnetic field intensity/µT')
plot.plot_2d(x_axis,'Year',avg_uv_index,'Average UV index',magn_history,'Magnetic field intensity/µT')
plot.plot_2d(x_axis,'Year',avg_precip,'Average precip',magn_history,'Magnetic field intensity/µT')
plot.plot_2d(x_axis,'Year',avg_humidity,'Average humidity',magn_history,'Magnetic field intensity/µT')


"""


