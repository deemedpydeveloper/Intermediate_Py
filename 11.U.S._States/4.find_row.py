# Find row with maximum temperature.

import pandas

weather_data = pandas.read_csv('weather_data.csv')

# getting maximum temperature value by max() method.
max_value = weather_data.temp.max()

# accessing row by maximum value.
print(weather_data[weather_data.temp == max_value])