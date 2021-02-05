import sys
import os
import json
import emojis
from yr.libyr import Yr

cwd = os.path.dirname(os.path.realpath(__file__))

with open(cwd + '/emojis.json') as file:
    symbols_emojis = json.load(file)

if len(sys.argv) > 1:
    weather = Yr(location_name=str(sys.argv[1]))
else:
    weather = Yr(location_name='Norway/Vestland/Bergen/Bergen')
now = weather.now()

weather_location = weather.location_name.split('/')
print('Weather in ' + weather_location[0] + ', ' + weather_location[1] + ', ' + weather_location[len(
    weather_location) - 1])

weather_type = emojis.encode(symbols_emojis[now['symbol']['@number']])
weather_precipitation = now['precipitation']['@value'] + 'mm'
weather_wind = now['windSpeed']['@mps'] + 'm/s'
weather_temp = now['temperature']['@value'] + u'\u00B0C'
print(weather_type + ' · ' + weather_temp + ' · ' + weather_wind + ' · ' + weather_precipitation)
