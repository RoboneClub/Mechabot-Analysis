#https://www.worldweatheronline.com/developer/api/docs/historical-weather-api.aspx
import requests
import numpy as np
from geopy.geocoders import Nominatim
from datetime import datetime,timedelta
url = "https://api.worldweatheronline.com/premium/v1/past-weather.ashx?"
key = "XXXXXXXXXXXXXXXXXXXXXXXX" #Add the API key here

def get_weather_data(lat=[],long=[],date=[]):
    """This function gathers weather data for the corresponding latitude, longitude, and date, for the past 10 years."""
    weather_data = []
    length = len(lat)
    counter = 0
    for lat,long,date in zip(lat,long,date):
        this_location_weather  = [] #collects the weather data for this location for last 10 years
        for i in range(10):
            d = (datetime.strptime(date,'%d/%m/20%y') - timedelta(365*i)).strftime("%d/%m/%Y") 
            try:
                print("Trying to fetch response.....")
                response = requests.get(f"{url}key={key}&q={lat},{long}&date={d}&format=json")
                this_location_weather.append(response.json()['data'])
                print(f"Fetched weather history data for {lat},{long} on {d}")
            except:
                print(f"Failed to retrive data for {lat},{long} on {d}")
                this_location_weather.append("Failed to retrieve")
        counter += 1
        print(f"API Fetching Progress {counter*100/length}%")
        weather_data.append(this_location_weather)
    return weather_data



def get_avg_temp(data):
    """this function gets the average temperatures for each point in the fetched data"""
    temp_history = []
    for point in data:
        this_point_temp = []
        for year_reading in point:
            this_point_temp.append(int(year_reading['weather'][0]['avgtempC']))
        temp_history.append(np.flip(this_point_temp))
    return temp_history


def get_uv_index(data):
    """this function gets the average uv index for each point in the fetched data"""
    uv_index_history = []
    for point in data:
        this_point_temp = []
        for year_reading in point:
            this_point_temp.append(int(year_reading['weather'][0]['uvIndex']))
        uv_index_history.append(np.flip(this_point_temp))
    return uv_index_history

def get_avg_precipitation(data):
    """this function gets the average precipitation for each point in the fetched data"""
    precip_history = []
    for point in data:
        this_point_precip = []
        for year_reading in point:
            hourly = []
            for hour in year_reading['weather'][0]['hourly']:
                hourly.append(float(hour['precipMM']))

            this_point_precip.append(float(np.average(hourly)))
        precip_history.append(np.flip(this_point_precip))
    return precip_history

def get_avg_wind_speed(data):
    """this function gets the average wind speeds for each point in the fetched data"""
    wind_speed_history = []
    for point in data:
        this_point_wind_speed = []
        for year_reading in point:
            hourly = []
            for hour in year_reading['weather'][0]['hourly']:
                hourly.append(float(hour['windspeedKmph']))

            this_point_wind_speed.append(float(np.average(hourly)))
        wind_speed_history.append(np.flip(this_point_wind_speed))
    return wind_speed_history

def get_avg_humidity(data):
    """this function gets the average humidity for each point in the fetched data"""
    humidity_history = []
    for point in data:
        this_point_humidity = []
        for year_reading in point:
            hourly = []
            for hour in year_reading['weather'][0]['hourly']:
                hourly.append(float(hour['humidity']))

            this_point_humidity.append(float(np.average(hourly)))
        humidity_history.append(np.flip(this_point_humidity))
    return humidity_history

def get_location(long,lat):
    geolocator = Nominatim(user_agent="GoogleV3")
    locations = []
    for i,j in zip(long,lat): 
        location = geolocator.reverse(str(i)+","+str(j))
        location = location.address if location != None else 'N/A'
        locations.append(location)
    return locations


if __name__ == '__main__':
    lat = [52.509669]
    long = [13.376294]
    date = ["01/01/2010"]
    data = get_weather_data(lat,long,date) 
    print(data[0][0]['weather'][0]['avgtempC']) #prints the average tempereature for 01/01/2010 of the first location
    print("/n/n//n/n/n\nn\n\n\n\n\n\n\n")
    print(get_location(lat,long)) #prints the average tempereature for 01/01/2010 of the first location
