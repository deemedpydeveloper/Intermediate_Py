# List Comprehension.

## syntax ---> new_list = [new_item for item in list]
# Example 1 - Appending items from a list to new list.
numbers = [1, 2, 3]
new_numbers = [num * 2 for num in numbers]
print(new_numbers)

# Example 2 - Appending items from a string to new list.
string = 'Tejendra'
new_string = [letter for letter in string]
print(new_string)

# Example 3 - Appending range function value to a new list.
range_numbers = [number for number in range(1, 5)]
print(range_numbers)

## All data types are treated as 'Python Sequences' in "List Comprehension method". Since, they follow some order in storing value.