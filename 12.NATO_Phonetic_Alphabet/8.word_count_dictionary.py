# Creating a Dictionary of words and their count using Dictionary Comprehension method.

sentence = "What is the Airspeed Velocity of an Unladen Swallow?".split(" ")
print(sentence)

result = {word: len(word) for word in sentence}
print(result)