import json
api_key = "4604ce6dc9974503bb5152326211806"
start_date = '2018-05-05'
end_date = '2018-05-06'
frequency = 12 #hours in one year
from WorldWeatherPy import DetermineListOfAttributes
attributes = DetermineListOfAttributes(api_key, True).retrieve_list_of_options()
attribute_list = ['time', 'tempC',  'windspeedKmph', 'winddirDegree', 'precipMM', 'humidity', 'visibility', 'pressure',  'cloudcover', 'HeatIndexC',  'DewPointC',  'WindChillC', 'WindGustKmph', 'FeelsLikeC',  'uvIndex']
from WorldWeatherPy import RetrieveByAttribute
city = 'cairo'
#dataset = RetrieveByAttribute(api_key, attribute_list, city, start_date, end_date, frequency).retrieve_hist_data()
from WorldWeatherPy import HistoricalLocationWeather

dataset = HistoricalLocationWeather(api_key, city, start_date, end_date, frequency).retrieve_hist_data()
print(dataset)

