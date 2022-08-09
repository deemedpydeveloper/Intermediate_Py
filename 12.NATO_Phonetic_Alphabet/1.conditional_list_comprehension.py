# Conditional List Comprehension.

##syntax ---> new_list = [new_item for item in list if test]
## A Method intended for checking conditions.
# Example 1 - Appending the names to new list, by condition.
names = ['Alex', 'Beth', 'Carolina', 'Dave', 'Eleanor', 'Freddie']
short_names = [name for name in names if len(name) < 5]
print(short_names)

# Example 2 - Appending the names using methods to new list.
long_formal_names = [name.upper() for name in names if len(name) > 4]
print(long_formal_names)
