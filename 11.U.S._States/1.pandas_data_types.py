# Series, DataFrames.

## Series ---> A Class which is same as list data type in python.
# Columns in table are referred as 'Series'.

## DataFrame ---> A Class which refers to whole tabular attributes and methods.
# In Pandas Library, a full table is referred as single 'DataFrame'.

import pandas

weather_data = pandas.read_csv('weather_data.csv')

# converting csv data to dictionary data.
dict_data = weather_data.to_dict()
print(dict_data)

# converting single column data to list.
list_data = weather_data['temp'].to_list()  # tapping into the column of 'temp'.
print(list_data)


# # Calculating Average Temperature without Series class methods.
# avg_temp = sum(list_data) / len(list_data)
# print(avg_temp)

# Calculating with Series Class methods.
print(weather_data['temp'].mean())  # .mean() --> method which returns mean value of series data type.

# Calculating max value.
print(weather_data['temp'].max())  # .max() --> method to find maximum value od series data type.