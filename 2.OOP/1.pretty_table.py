# Prettytable Package from Pypi.

# import class from module.
from prettytable import PrettyTable

# Object Creation from Class.
table = PrettyTable()

# Tapping Methods of Object.
table.add_column('Pokemon Name', ['Pikachu', 'Squirtle', 'Charmander'])  # .add_column('Field_name', [list of strings in the column])
table.add_column('Type', ['Electric', 'Water', 'Fire'])

# Tapping Attributes of Object.
table.align = "l"  # left alignment.

# Final Output.
print(table)