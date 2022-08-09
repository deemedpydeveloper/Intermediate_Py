import pandas

student_dict = {
    "student": ['Angela', 'James', 'Lily'],
    "score": [56, 76, 98]
}

student_scores_DataFrame = pandas.DataFrame(student_dict)
print(student_scores_DataFrame)

# # getting keys & values from dataframe.
# for (key, value) in student_scores_DataFrame.items():
#     # print(key)  # print only keys from dictionary.
#     print(value)  # print only values from dictionary.

# looping through rows of DataFrame.
for (index, row) in student_scores_DataFrame.iterrows():
    # print(index)  # prints only index.
    # print(row)  # prints entire row.
    # print(row.student)  # prints only student key values.
    if row.student == 'Angela':
        print(row.score)  # prints particular student score on condition.
