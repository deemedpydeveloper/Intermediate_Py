# Finding Monday's temperature and Convert Celsius to Fahrenheit.

import pandas

weather_data = pandas.read_csv('weather_data.csv')

# getting hold of monday row.
monday = weather_data[weather_data.day == 'Monday']

# getting hold of monday's temperature.
temperature_in_celsius = int(monday.temp)
print(f'The Temperature in celsius is: {temperature_in_celsius}C')

# celsius to fahrenheit.
## F = (C * 1.8) + 32
temperature_in_fahrenheit = (temperature_in_celsius * 1.8) + 32
print(f'The Temperature in fahrenheit is: {temperature_in_fahrenheit}F')