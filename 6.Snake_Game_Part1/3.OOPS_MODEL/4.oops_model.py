# OOPS Model.

import time
from turtle import Screen
from snake import Snake

screen = Screen()
screen.title("My Snake Game")
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)   # doesn't trace the screen until updated.

snake = Snake()

# Control the snake with keypress.
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()