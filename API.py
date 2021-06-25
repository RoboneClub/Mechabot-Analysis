#https://www.worldweatheronline.com/developer/api/docs/historical-weather-api.aspx
import requests
from datetime import datetime,timedelta
url = "https://api.worldweatheronline.com/premium/v1/past-weather.ashx?"
key = "4604ce6dc9974503bb5152326211806" 
def get_weather_data(lat=[],long=[],date=[]):
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

if __name__ == '__main__':
    lat = [51.94]
    long = [-51.28]
    date = ["01/01/2010"]
    data = get_weather_data(lat,long,date) 
    print(data[0][0]['weather'][0]['avgtempC']) #prints the average tempereature for 01/01/2010 of the first location
