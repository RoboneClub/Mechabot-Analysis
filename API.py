#https://www.worldweatheronline.com/developer/api/docs/historical-weather-api.aspx
import requests
from datetime import datetime,timedelta
url = "https://api.worldweatheronline.com/premium/v1/past-weather.ashx?"
key = "4604ce6dc9974503bb5152326211806" 
def get_weather_data(lat=[],long=[],date=[]):
    weather_data = []
    for lat,long,date in zip(lat,long,date):
        avg_temp = [] #collects the average temp for last 10 years
        for i in range(10):
            try:
                date2 = (datetime.strptime(date,'%d/%m/20%y') - timedelta(365*i)).strftime("%d/%m/%Y") 
                response = requests.get(f"{url}key={key}&q={lat},{long}&date={date2}&format=json")
                avg_temp.append(response.json()['data']['weather'][0]['avgtempC'])
            except:
                avg_temp.append("Failed to retrieve")
        weather_data.append(avg_temp)
    return weather_data

if __name__ == '__main__':
    lat = [51.94]
    long = [-51.28]
    date = ["2018/12/01"]
    print(get_weather_data(lat,long,date)[0].json())
