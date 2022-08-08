import pandas

# get column
weather_data = pandas.read_csv('weather_data.csv')
print(weather_data['temp'])
print('///////////////////////')
# 0r
print(weather_data.temp)