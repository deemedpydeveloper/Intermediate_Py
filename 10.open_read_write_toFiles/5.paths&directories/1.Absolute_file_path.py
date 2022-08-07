# Opening a file using 'Absolute Path'.
with open('/Users/ASUS/Desktop/move_file.txt', mode='r') as file:

    # reading the file.
    contents = file.read()

    # accessing the contents.
    print(contents)