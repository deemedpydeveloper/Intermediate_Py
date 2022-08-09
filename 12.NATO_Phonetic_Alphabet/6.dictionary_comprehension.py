# Dictionary Comprehension.

## syntax ---> new_dict = {new_key:new_value for item in list}

# Example1 - Appending key/value pairs to the new dictionary from list.
import random
names = ['Alex', 'Beth', 'Carolina', 'Dave', 'Eleanor', 'Freddie']
student_scores = {student: random.randint(1, 100) for student in names}
print(student_scores)

# Example2 - Appending dictionary key value pairs to new dictionary.
duplicate_scores = {student: score for (student, score) in student_scores.items()}
print(duplicate_scores)
