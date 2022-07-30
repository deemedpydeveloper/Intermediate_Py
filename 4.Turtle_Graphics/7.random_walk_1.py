# Random Walk.
import random
import turtle
from turtle import Turtle, Screen

turtle = Turtle()

# speed control.
turtle.speed("fastest")

# width.
turtle.width(5)  # or turtle.pensize(integer)

# randomization of paths.
def random_path(input):
    if input == 'right':
        turtle.right(90)

    elif input == 'backward':
        turtle.backward(10)

    elif input == 'forward':
        turtle.forward(10)

    else:
        turtle.left(90)

# randomization of direction.
direction = ['left', 'right', 'backward', 'forward']    # or turtle.setheading(random.choice(directions)) where, directions = [0, 90, 180, 270]

# randomization of colors.
colors = ['deep sky blue', 'lawn green', 'burlywood', 'magenta', 'dark violet', 'teal', 'orange red', 'olive drab']

for _ in range(1000):
    choice = random.choice(direction)   # differnt direction.
    random_path(choice)                 # calling function.
    turtle.color(random.choice(colors))  # differnt colors.

# Screen control.
screen = Screen()
screen.exitonclick()