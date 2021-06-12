from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from urllib.request import urlopen
station = 'KCLT'
current_date = datetime(year=2021, month=5, day=5)
with open(f"{station}.csv", 'w') as out_file:
    out_file.write('date,actual_mean_temp,actual_min_temp,actual_max_temp,'
                   'average_min_temp,average_max_temp,'
                   'record_min_temp,record_max_temp,'
                   'record_min_temp_year,record_max_temp_year,'
                   'actual_precipitation,average_precipitation,'
                   'record_precipitation\n')
with open(f"{station}-{current_date.year}-{current_date.month}-{current_date.day}.html") as in_file:
    soup = BeautifulSoup(in_file.read(), 'html.parser')


    weather_data = soup.find(id='historyTable')#.find_all('span', class_='wx-value')
    print(weather_data)
    weather_data_units = soup.find(id='historyTable').find_all('td')

    try:
        actual_mean_temp = weather_data[0].text
        actual_max_temp = weather_data[2].text
        average_max_temp = weather_data[3].text
        record_max_temp = weather_data[4].text
        actual_min_temp = weather_data[5].text
        average_min_temp = weather_data[6].text
        record_min_temp = weather_data[7].text
        record_max_temp_year = weather_data_units[
            9].text.split('(')[-1].strip(')')
        record_min_temp_year = weather_data_units[
            13].text.split('(')[-1].strip(')')

        actual_precipitation = weather_data[9].text
        if actual_precipitation == 'T':
            actual_precipitation = '0.0'
        average_precipitation = weather_data[10].text
        record_precipitation = weather_data[11].text

        # Verify that the parsed data is valid
        if (record_max_temp_year == '-1' or record_min_temp_year == '-1' or
                int(record_max_temp) < max(int(actual_max_temp), int(average_max_temp)) or
                int(record_min_temp) > min(int(actual_min_temp), int(average_min_temp)) or
                float(actual_precipitation) > float(record_precipitation) or
                float(average_precipitation) > float(record_precipitation)):
            raise Exception

        out_file.write('{}-{}-{},'.format(current_date.year, current_date.month, current_date.day))
        out_file.write(','.join([actual_mean_temp, actual_min_temp, actual_max_temp,
                                 average_min_temp, average_max_temp,
                                 record_min_temp, record_max_temp,
                                 record_min_temp_year, record_max_temp_year,
                                 actual_precipitation, average_precipitation,
                                 record_precipitation]))
        out_file.write('\n')
        current_date += timedelta(days=1)
    except:
        # If the web page is formatted improperly, signal that the page may need
        # to be downloaded again.
        print("error")

