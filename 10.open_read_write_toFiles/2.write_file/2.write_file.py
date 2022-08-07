# opening the existing file and setting mode to 'append'.
file = open("2.write_file.txt", mode='a')

# writing a string into the file.
contents = file.write('\nIam Python Developer.')

# opening the same file and setting mode to 'read-only'.
file = open("2.write_file.txt", mode='r')

# reading the file contents.
contents = file.read()

# printing the file contents.
print(contents)

# closing the file.
file.close()