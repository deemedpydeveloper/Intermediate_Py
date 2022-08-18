try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])

# this block is used to handle file exceptions.
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something.")

# this block is used to catch an exception.
except KeyError as error_message:
    print(f"The key {error_message} does not exist.")

# this block executes when except block is failed.
else:
    content = file.read()
    print(content)

# this block executes irrespective of all above blocks.
finally:
    file.close()
    print("File was closed.")