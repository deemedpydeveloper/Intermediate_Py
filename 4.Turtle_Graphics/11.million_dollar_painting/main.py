#  Million Dollar Painting.
import random
import turtle as t

import colorgram

turtle = t.Turtle()

# empty list to store the tuple values of rgb values.
rgb_colors = []

# getting rgb values.
colors = colorgram.extract("color_dots.jpg", 50)
for color in colors:
    r = color.rgb.r  # taps into r value of rgb values.
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

# print(rgb_colors)

# list of rgb tuple values.
rgb_colors_list = [(247, 237, 199), (248, 222, 240), (120, 164, 215), (208, 134, 182), (219, 250, 226), (225, 155, 97), (218, 232, 248), (233, 224, 100), (231, 166, 202), (29, 201, 59), (98, 202, 123), (211, 69, 132), (195, 38, 126), (169, 175, 235), (125, 232, 162), (214, 8, 47), (90, 110, 209), (241, 169, 154), (13, 11, 202), (218, 10, 4), (192, 159, 32), (103, 220, 237), (227, 82, 69), (25, 153, 38), (65, 107, 169), (42, 177, 197), (191, 55, 37), (252, 7, 31), (25, 19, 248), (217, 234, 11), (2, 248, 239), (252, 9, 6), (0, 246, 253), (5, 3, 117), (10, 115, 24), (125, 31, 0)]

# setting color mode.
t.colormode(255)

# setting dot speed and making invisible.
turtle.speed('fastest')
turtle.penup()
turtle.hideturtle()


# set heading of turtle.
turtle.setheading(225)
turtle.forward(350)
turtle.setheading(0)

# printing dots on screen.
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    # printing one line.
    turtle.dot(20, random.choice(rgb_colors_list))
    turtle.forward(50)
    # moving to next line.
    if dot_count % 10 == 0:
        turtle.setheading(90)
        turtle.forward(50)
        turtle.setheading(180)
        turtle.forward(500)
        turtle.setheading(0)

# screen control.
screen = t.Screen()
screen.exitonclick()