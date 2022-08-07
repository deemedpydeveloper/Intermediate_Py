# If there is no file created initially, it creates a new file.
file = open("create_file.txt", mode='a')

# As mode is set to 'a', write function will 'append' the string to that file.
contents = file.write('My Name is Y.Tejendra.')

# closing the file.
file.close()