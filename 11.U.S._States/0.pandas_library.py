# with open('./weather_data.csv') as weather_data_file:
#     data = weather_data_file.readlines()
#     print(data)
## above method is tedious task to format the csv data.

# import csv  # library used for csv files.
#
# with open('weather_data.csv') as weather_data_file:
#     data = csv.reader(weather_data_file)  # reads the data from csv file.
#     # print(data)  ## creates an object at some memory location.
#     temperatures = []
#     for row in data:  # takes each item in a list and stores in variable 'row'.
#         print(row)  # gives an item in the list.
#         if row[1] == 'temp':
#             pass  # does nothing if row[1] = 'temp' ---> since it is not required.
#         else:
#             temperatures.append(int(row[1]))
#     print(temperatures)
## above csv library method also tedious task for accessing each column.

import pandas
data = pandas.read_csv('weather_data.csv')
print(data)   # prints entire data in tabular form.
print('')
print('')
print(data['temp'])   # prints only temp column.

## above method is best for data analysis.