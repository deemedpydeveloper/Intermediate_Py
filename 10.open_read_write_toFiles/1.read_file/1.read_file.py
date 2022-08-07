# opening the existing file and setting the file mode to 'read-only'.
file = open("1.read_file.txt", mode='r')

# accessing the contents of the file.
contents = file.read()

# printing the contents of the file.
print(contents)

# when reading the file is completed, we should close the file.
file.close()