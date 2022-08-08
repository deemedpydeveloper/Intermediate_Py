import pandas

# get row
weather_data = pandas.read_csv('weather_data.csv')
print(weather_data[weather_data.day == 'Monday'])