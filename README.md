# Analysis-of-Mechabot-Astro-Pi-Data
Analyzing the results from the AstroPi competition for Mechabot where the experiment ran on 2021 

This repo contains the code responsible for analysing the data returned from the ISS astropi experiment, which ran on 5/5/2021.

The iss experiment run:
![Path of ISS during experiment](https://github.com/RoboneClub/Mechabot-Analysis/blob/main/Plots%20for%20unprocessed%20data/Mechabot%20ISS%20runtime%20Orbit.png?raw=true)

## A pictures captured from the ISS raspberry Pi camera for the River Nile in Egypt!
![RiverNile in Egypt](https://github.com/RoboneClub/Mechabot-Analysis/blob/main/Images%20corresponding%20to%20the%2020%20chosen%20points%20in%20expirment-1/image_1296.jpg)
The River Nile in Egypt

## We were researching three main topics:

* Experiment 1:     If certain climate characteristics exist for zones with different Magnetic Intensities.
* Experiment 1.5:   Whether or not the change magnetic intensity and the change in climate over the years is correlated.
* Experiment 2:     Whether or not the magnetic field affects the orbit of the bodies in the Low Earth Orbit.



## The code consisted of 8 different files, with each one accomplishing a certain objective

#### graphs.py:
This file is responsible for producing the graphs for the raw acquired data from the ISS readings.

#### map.py:
This file creates a map for visualising the orbit of ISS relative to Earth during our experiment. If given an array of coordinates, the function will mark the locations corresponding to those coordinates on the map.

#### API.py:
This file handles the world weather online API library, which was used to retrieve weather data at a given location and date. We used it to acquire weather data at certain locations of interest for the past 10 years.

#### plot.py:
This file is a module responsible for plotting graphs with 2 Y-Axis.

#### magn.py:
This file includes functions needed to process IMU sensor data, such as autocorrelation, resultant magnitude, standard deviation, and correlation.

#### noisefiltering.py:
This file was made to filter noise from sensor readings.

#### experiment-1.py:
This file is responsible for executing experiment 1 and 1.5.
It produces graphs that check for correlations between change in Magnetic field intensity and each of Average Temperature, Wind Speed, UV Index, Precipitation, and Humidity in 20 locations for the past 10 years including the current year. Additionally, it produces graphs that check for general characteristic in climate and whether they are correlated to magnetic intensity or not in 20 locations.

#### experiment-2.py:
This file is responsible for executing experiment 2.
It produces graphs that check for any correlation between the magnetic field intensity and the accleration and angular velocity of the ISS which is an object in low Earth orbit.




## Resutls:
  
### For experiment 1:
![Magnetic Intensity and Average Temperature Graph](https://github.com/RoboneClub/Mechabot-Analysis/blob/main/Experiment%201.0%20plots%20and%20results/Magn-Temp.png?raw=true)
This graph clearly shows that locations with higher magnetic intensity tend to have lower temperatures giving a negative correlation between the magnetic field and the average Temperature.


![Magnetic Intensity and Humidity Graph](https://github.com/RoboneClub/Mechabot-Analysis/blob/main/Experiment%201.0%20plots%20and%20results/Magn-Humidity.png?raw=true)
The graph implies that there is no correlation between humidity and magnetic intensity, as the values appear random and there does not appear to be any direct relation between both variables


![Magnetic Intensity and Precipitation Graph](https://github.com/RoboneClub/Mechabot-Analysis/blob/main/Experiment%201.0%20plots%20and%20results/Magn-Precip.png?raw=true)
This graph suggests a positive correlation between precipitation and magnetic intensity, as when the Magnetic intensity increases the average Precipitation also rises.



![Magnetic Intensity and UV Index Graph](https://github.com/RoboneClub/Mechabot-Analysis/blob/main/Experiment%201.0%20plots%20and%20results/Magn-UV.png?raw=true)
The above figure showed a negative correlation between the UV index and the Magnetic intesnity stating that in areas where there is a higher magnetic intensity, theres a lower UV index than in other areas with weaker Magnetic Intensity.


![Magnetic Intensity and Windspeed Graph](https://github.com/RoboneClub/Mechabot-Analysis/blob/main/Experiment%201.0%20plots%20and%20results/Magn-WindSpeed.png)
The random scatterness of points in the above figure shows that there is no direct relation between the areas with high magnetic intensities and the average WindSpeed.


### For experiment 1.5:
![Table for results](https://cdn.discordapp.com/attachments/806968902620938283/859872743457947658/unknown.png)


Most of the variable changes appear to be random and there does not appear to be a relation between climate change and the decay
in the magnetic field. Only some Humidity points hint that the magnetic field decay could be causing their decrease yet more research with a bigger data set should be conducted to reach a more conclusive result. 

### For experiment 2:
![Correlation between Magnetic intensity and GyroScope X](https://github.com/RoboneClub/Mechabot-Analysis/blob/main/Experiment%202.0%20plots%20and%20results/gyroz_magn_corr.png)

This graph shows an obvious oscillating trend between magnetic intensity and angular velocity on the Z-Axis. This hints at a strong relation between
these two values.

![AutoCorrelation of Acceleration](https://github.com/RoboneClub/Mechabot-Analysis/blob/main/Experiment%202.0%20plots%20and%20results/acc_autocorr.png)

The graph of the autocorrelation of the acceleration resultant before the noise filtering have spikes that suggest the presence of micro-vibrations on the ISS.
After the noise filtering, these spikes where remove due to that the noise filtering algorithm is not ideal and omitted such information.
The issue  the values are too small to be distinguished apart from the noise, therefor readings from an acceleration sensor with a higher accuracy is
required to stronger empathies and support the effect that the magnetic field is causing on the orbit of the ISS.
