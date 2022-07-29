# Random Walk Version 2.

# import class turtle module instead of object.
import random
import turtle as t

turtle = t.Turtle()

# setting pen width.
turtle.pensize(15)

# setting speed.
turtle.speed("fastest")

# setting color mode to 255.
t.colormode(255)

# color function.
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors = (r, g, b)
    return colors

# randomization of direction and color.
directions = [0, 90, 180, 270]
for _ in range(200):
    turtle.color(random_color())  # calling function.
    turtle.forward(30)
    turtle.setheading(random.choice(directions))