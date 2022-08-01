# Class Inheritance.

class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, Exhale")

# Animal class is passed as a parameter to class fish.
class Fish(Animal):
    def __init__(self):
        # super() ---> Inheriting features from superclass 'Animal'.
        super().__init__()

    def breathe(self):
        # We can also modify the superclass methods.
        super().breathe()
        print("doing this underwater.")

    def swim(self):
        print("moving in water.")

nemo = Fish()
nemo.swim()
nemo.breathe()
