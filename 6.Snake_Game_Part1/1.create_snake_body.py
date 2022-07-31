# Create a Snake Body.

from turtle import Turtle, Screen

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
for position in starting_positions:
    new_segment = Turtle('square')
    # print(new_segment.shapesize())
    new_segment.color('white')
    new_segment.goto(position)

screen = Screen()
screen.title("My Snake Game")
screen.setup(width=600, height=600)
screen.bgcolor('black')



screen.exitonclick()