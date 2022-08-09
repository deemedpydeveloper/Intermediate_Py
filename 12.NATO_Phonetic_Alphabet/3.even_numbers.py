# Extract even numbers from a list using list comprehension method.

numbers = [1, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [number for number in numbers if number % 2 == 0]  # conditional list comprehension method.
print(result)