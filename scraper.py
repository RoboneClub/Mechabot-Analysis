
from datetime import datetime, timedelta
from urllib.request import Request, urlopen
import os
current_date = datetime(year=2021, month=5, day=5)
station = 'KCLT'
lookup_URL = 'http://www.wunderground.com/history/daily/{}/date/{}-{}-{}'
formatted_lookup_URL = lookup_URL.format(station,
                                         current_date.year,
                                         current_date.month,
                                         current_date.day)
print(formatted_lookup_URL)
req = Request(formatted_lookup_URL,headers={'User-Agent': 'Mozilla/5.0'})
html = urlopen(req).read().decode('utf-8')

out_file_name = '{}-{}-{}-{}.html'.format(station, current_date.year,
                                          current_date.month,
                                          current_date.day)

with open(out_file_name, 'w') as out_file:
    out_file.write(html)

