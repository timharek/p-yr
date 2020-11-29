import sys

import emojis
from yr.libyr import Yr

symbols_emojis = { # https://listemoji.com/
    "1": ":sunny:",
    "2": ":sun_behind_small_cloud:",
    "3": ":sun_behind_large_cloud:",
    "4": ":cloud:",
    "40": ":sun_behind_rain_cloud:",
    "5": ":cloud_with_rain:",
    "41": ":umbrella:",
    "24": ":cloud_with_lightning_and_rain:",
    "6": ":cloud_with_lightning_and_rain:",
    "25": ":cloud_with_lightning_and_rain:",
    "42": ":cloud_with_snow:",
    "7": ":cloud_with_snow:",
    "43": ":cloud_with_snow:",
    "26": ":cloud_with_lightning_and_rain:",
    "20": ":cloud_with_lightning_and_rain:",
    "27": ":cloud_with_lightning_and_rain:",
    "44": ":cloud_with_snow:",
    "8": ":cloud_with_snow:",
    "45": ":cloud_with_snow:",
    "28": ":cloud_with_snow: :cloud_with_lightning_and_rain:",
    "21": ":cloud_with_snow: :cloud_with_lightning_and_rain:",
    "29": ":cloud_with_snow: :cloud_with_lightning_and_rain:",
    "46": ":cloud_with_rain:",
    "9": ":umbrella:",
    "10": ":umbrella: :umbrella:",
    "30": ":cloud_with_lightning_and_rain:",
    "22": ":umbrella: :cloud_with_lightning_and_rain:",
    "11": ":umbrella: :umbrella: :cloud_with_lightning_and_rain:",
    "47": ":snowflake:",
    "12": ":cloud_with_snow:",
    "48": ":cloud_with_snow: :cloud_with_snow:",
    "31": ":cloud_with_snow: :zap:",
    "23": ":cloud_with_snow: :cloud_with_snow: :zap:",
    "32": ":cloud_with_snow: :cloud_with_snow: :cloud_with_snow: :zap:",
    "49": ":closed_umbrella: :snowflake:",
    "13": ":snowflake:",
    "50": ":snowflake: :snowflake: :snowflake:",
    "33": ":snowflake: :zap:",
    "14": ":snowflake: :snowflake: :zap:",
    "34": ":snowflake: :snowflake: :snowflake: :zap:",
    "15": ":fog:"
}

if len(sys.argv) > 1:
    weather = Yr(location_name=str(sys.argv[1]))
else:
    weather = Yr(location_name='Norway/Vestland/Bergen/Bergen')
    # weather = Yr(location_xyz=(60.388068, 5.331854))
now = weather.now()

weather_location = weather.location_name.split('/')
print('Weather in ' + weather_location[0] + ', ' + weather_location[1] + ', ' + weather_location[len(
    weather_location) - 1])

weather_type = emojis.encode(symbols_emojis[now['symbol']['@number']])
weather_precipitation = now['precipitation']['@value'] + 'mm'
weather_wind = now['windSpeed']['@mps'] + 'm/s'
weather_temp = now['temperature']['@value'] + u'\u00B0C'
print(weather_type + ' · ' + weather_temp + ' · ' + weather_wind + ' · ' + weather_precipitation)
