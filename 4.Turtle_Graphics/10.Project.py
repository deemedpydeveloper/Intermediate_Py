# Draw a spirograph.

# importing turtle module and random module.
import turtle as t
import random

# creating turtle object from turtle class.
turtle = t.Turtle()

# creating spiral function.
def spiral():
    turtle.circle(100)
    turtle.left(4.5)

# setting turtle speed.
turtle.speed("fastest")

# setting turtle colormode.
t.colormode(255)

# randomization of color.
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors = (r, g, b)
    return colors

# calling spiral and color function.
count = 80
while count:
    count -= 1
    turtle.color(random_color())
    spiral()

# creating screen object from screen function.
screen = t.Screen()

# screen setting.
screen.exitonclick()