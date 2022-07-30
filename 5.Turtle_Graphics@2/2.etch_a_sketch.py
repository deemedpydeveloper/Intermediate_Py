# Etch a Sketch.

from turtle import Turtle, Screen

turtle = Turtle()

def forward():
    turtle.forward(10)

def backward():
    turtle.backward(10)

def clockwise():
    turtle.right(10)

def anti_clockwise():
    turtle.left(10)

def clear_drawing():
    turtle.reset()   # resets all values and comes to original position.

screen = Screen()

screen.listen()
screen.onkey(key='w', fun=forward)
screen.onkey(key='s', fun=backward)
screen.onkey(key='d', fun=clockwise)
screen.onkey(key='a', fun=anti_clockwise)
screen.onkey(key='c', fun=clear_drawing)
screen.exitonclick()