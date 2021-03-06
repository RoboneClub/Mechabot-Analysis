""" Importing the libraries and the modules """
from datetime import datetime,timedelta
import API
import magn
import map
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import noise_filtering

"""_______________________ Part 1: Analyzing the magnometer data _______________________"""


''' 1-Importing the magnometer data '''

#Imports the whole data from the csv using pandas library
data = pd.read_csv('data01.csv')

#Takes only the time,magnometer X,Y,Z readings from the dataset:
time = data.iloc[:,1].values
magnX = data.iloc[:,10].values
magnY = data.iloc[:,11].values
magnZ = data.iloc[:,12].values


''' 2-Preprocessing the data by applying noise filteration '''

magn_filtered_matrix = noise_filtering.noise_filtering(magnX,magnY,magnZ,sensitivity = 0.043, frequency = 20,  rms = (3.2 * 10**-3) )
    #Senstivity and Frequency are according to https://www.st.com/resource/en/datasheet/lsm9ds1.pdf
    #RMS Noise assumtion according to https://www.st.com/resource/en/datasheet/lis3mdl.pdf which is a similar build


''' 3- Calculating the resultant magnitude of the magnetic field, the standard deviation,the mean and the  auto corelation of the points'''

magn_resultant = magn.get_resultant(magn_filtered_matrix[:,0],magn_filtered_matrix[:,1],magn_filtered_matrix[:,2])
magn_sd = magn.get_sd(magn_resultant)
magn_mean = magn.get_mean(magn_resultant)
magn_autocorrelation = magn.autocor(magn_resultant) #A graph is plotted for the magnetic intensity autocorrelation in expirment 2


'''4- Plotting the graphs '''

plt.title("Magnometer Readings")
plt.xlabel("Time")
plt.ylabel("Magnetic Intensity/µT")
plt.plot(time,magnX,label='MagnX')
plt.plot(time,magnY,label='MagnY')
plt.plot(time,magnZ,label='MagnZ')
plt.legend()
plt.show()

plt.title("Magnometer Data")
plt.xlabel("Time")
plt.ylabel("Magnetic Intensity/µT")
plt.plot(time,magn_resultant,label='MagnResultant')
plt.plot(time,[magn_mean]*len(magnX),label='Mean')
plt.plot(time,[magn_sd]*len(magnX),label='Standard Deviation')
plt.legend()
plt.show()

"""_______________________ Part 2: Extracting 20  points to preform the research on _______________________"""

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
#Refrence for decay value: https://www.pnas.org/content/115/20/5111#:~:text=Abstract,since%201600%20or%20even%20earlier.


magn_history = magn.get_magn_history(magn_points_of_study,decay = 0.0005)




"""_______________________ Part 3: Fetching the weather history data for the study points _______________________"""

'''Importing the date for the Points'''
date = data.iloc[points_of_study]['Date'].values

'''1-Downloading the weather data for the last 10 years for each point using the API'''
weather_data = API.get_weather_data(lat_dd, long_dd, date)

'''1.5-Saving the downloaded data in a numpy file '''
np.save("weather_data.npy",weather_data)
#For loading the file:
#weather_data = np.load("weather_data.npy",allow_pickle=True)

'''2-Extract each variable from the downloaded data'''
avg_temp = np.array(API.get_avg_temp(weather_data))
avg_wind_speed = np.array(API.get_avg_wind_speed(weather_data))
avg_uv_index = np.array(API.get_uv_index(weather_data))
avg_precip = np.array(API.get_avg_precipitation(weather_data))
avg_humidity = np.array(API.get_avg_humidity(weather_data))




"""Results of Experiment 1.0:

    ____________ Part 4: Comparing the Magnometer values with the climate of the study points to check general characetistics of magnetic zones __________"""
"""
This experiment checks for the presence of climate characteristics associated with the magnetic intensity.For example it checks if
areas with high magnetic intensities tend to have higher temperatures than other areas with lower magnetic intensities.
The experiment scatters each reading of the magnetic field alongside with the climate values from the 20 locations all in one graph.
"""
#plotting the graphs
plt.title("Magnometer - Temperature")
plt.scatter(magn_points_of_study,avg_temp[:,0])
plt.ylabel("Average Temperature/ C")
plt.xlabel("Magnetic Intensity/µT")
plt.show()

plt.title("Magnometer - Windspeed")
plt.scatter(magn_points_of_study,avg_wind_speed[:,0])
plt.ylabel("Average Wind Speed/ KmHr")
plt.xlabel("Magnetic Intensity/µT")
plt.show()

plt.title("Magnometer - UV index")
plt.scatter(magn_points_of_study,avg_uv_index[:,0])
plt.ylabel("Average UV index")
plt.xlabel("Magnetic Intensity/µT")
plt.show()

plt.title("Magnometer - Precipitation")
plt.scatter(magn_points_of_study,avg_precip[:,0])
plt.ylabel("Average Precipitation/mm")
plt.xlabel("Magnetic Intensity/µT")
plt.show()

plt.title("Magnometer - Humidity")
plt.scatter(magn_points_of_study,avg_humidity[:,0])
plt.ylabel("Average Humidity/%")
plt.xlabel("Magnetic Intensity/µT")
plt.show()



"""Results of Experiment 1.5:
    _______________________ Part 5: Comparing the Magnometer values with  the weather history data for each of the study points _______________________"""

"""
This experiment produces graphs that check for correlations between change in Magnetic field intensity and the change of each of
Average Temperature, Wind Speed, UV Index, Precipitation, and Humidty in 20 locations for the past 10 years.
Each graph contains the past climate history along side with the magnetic intensity history for Each Location from the 20 Points.
"""
import plot
locations = API.get_location(long_dd,lat_dd)

x_axis = np.arange(2012,2022,1)

#plotting the graphs
plot.plot_2d(x_axis,'Year',avg_temp,'Average Temperature of day',magn_history,'Magnetic field intensity/µT',locations)
plot.plot_2d(x_axis,'Year',avg_wind_speed,'Average wind speed',magn_history,'Magnetic field intensity/µT',locations)
plot.plot_2d(x_axis,'Year',avg_uv_index,'Average UV index',magn_history,'Magnetic field intensity/µT',locations)
plot.plot_2d(x_axis,'Year',avg_precip,'Average precip',magn_history,'Magnetic field intensity/µT',locations)
plot.plot_2d(x_axis,'Year',avg_humidity,'Average humidity',magn_history,'Magnetic field intensity/µT',locations)

