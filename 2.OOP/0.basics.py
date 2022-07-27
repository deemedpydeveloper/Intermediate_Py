# Basics.

## Class ---> Holds the blueprint of creation of virtual object.
## Classes are identified easily, as they follow "PascalCase".
## Object ---> It is an virtual object created from class.
## Object "has something" and "does something".
## "has something" ---> Attributes ----> Formal name of 'Variables.'
## "does something" ---> Methods ----> Formal name of 'Function'.

# importing class turtle and method screen from turtle module.
from turtle import Turtle, Screen

# Object1 Creation.
timmy = Turtle()   # Turtle() ---> Class, timmy ---> Object
print(timmy)

# Object1 Methods.
timmy.shape("turtle")  # .shape() ---> timmy Method.
timmy.color("CadetBlue")  # .color() ----> timmy Method.
timmy.forward(100)  # .forward() ----> timmy Method.

# Object2 Creation.
my_screen = Screen()   # Screen() ---> Class, my_screen ---> Object.

# Object2 Attribute.
print(my_screen.canvheight)  # .canvheight ---> my_screen Attribute.

# Object2 Method.
my_screen.exitonclick()  # .exitonclick() ---> my_screen Method.