# Creating a data frame from scratch.

data_dict = {
    'students': ['tej', 'raj', 'sesh'],
    'score': [67, 87, 66],
}

import pandas

data_Frame = pandas.DataFrame(data_dict)
print(data_Frame)

# Creating a new csv file.

data_Frame.to_csv('new_csv')