# Creating a DataFrame form Squirrel csv file.

import pandas

squirrel_data = pandas.read_csv('004 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv')

# Getting gray, cinnamon, black squirrels count from 'Primary Fur Color' Column.
gray_squirrel_count = len(squirrel_data[squirrel_data['Primary Fur Color'] == 'Gray'])
cinnamon_squirrel_count = len(squirrel_data[squirrel_data['Primary Fur Color'] == 'Cinnamon'])
black_squirrel_count = len(squirrel_data[squirrel_data['Primary Fur Color'] == 'Black'])

# dictionary creation.
squirrel_dict_data = {
    'Color': ['Gray', 'Cinnamon', 'Black'],
    'Count': [gray_squirrel_count, cinnamon_squirrel_count, black_squirrel_count]
}

# csv file creation.
squirrel_tabular_data = pandas.DataFrame(squirrel_dict_data)
squirrel_tabular_data.to_csv('squirrel_csv_data.csv')