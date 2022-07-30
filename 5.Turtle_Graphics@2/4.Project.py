# Turtle Race.
import random

from turtle import Turtle, Screen

screen = Screen()


# setting screen size.
screen.setup(width=500, height=400)

# prompt from user.
user_bet = screen.textinput(title='Make your bet', prompt="Which turtle will win the race? Enter a color: ")
is_game_start = False

# turtle colors.
colors = ['red', 'orange', 'blue', 'yellow', 'green', 'violet']

# y_positions.
y_positions = [-180, -120, -60, 0, 60, 120, 180]

# turtles list.
all_turtles = []

# getting 6 turtles to left edge of screen.
for index_num in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[index_num])
    new_turtle.goto(x=-230, y=y_positions[index_num])
    all_turtles.append(new_turtle)

# game start.
if user_bet:
    is_game_start = True

while is_game_start:
    for turtle in all_turtles:
        if turtle.xcor() > 220:
            is_game_start = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lose! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

# screen setting.
screen.exitonclick()