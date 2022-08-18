height = float(input("Height: "))
weight = int(input("Weight: "))

# raising errors.
if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)