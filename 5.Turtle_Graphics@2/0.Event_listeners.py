# Event Listeners.

from turtle import Turtle, Screen

turtle = Turtle()

def move():
    turtle.forward(30)

screen = Screen()

screen.listen()
screen.onkey(key='space', fun=move)   # on pressing spacebar, the move function is executed.

screen.exitonclick()