# Drawing Shapes.
import random
from turtle import Turtle, Screen

# object creation.
turtle = Turtle()

# colors list.
colors = ['deep sky blue', 'lawn green', 'burlywood', 'magenta', 'dark violet', 'teal', 'orange red', 'olive drab']

# drawing shape.
def draw_shape(number_of_sides):  # calling this function for each shape.
    angle = 360 / number_of_sides  # calculation of angle.
    for _ in range(number_of_sides):  # repeats for n sides.
        turtle.forward(100)
        turtle.right(angle)

# color randomization.
for shape_side_n in range(3, 11):  # iteration of defined function over a range of number of sides.
    turtle.color(random.choice(colors))
    draw_shape(shape_side_n)

# screen control object creation.
screen = Screen()
screen.exitonclick()