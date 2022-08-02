from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

# passing tuples as arguments to goto() method.
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()

# left paddle controls.
screen.onkey(fun=l_paddle.go_up, key='w')
screen.onkey(fun=l_paddle.go_down, key='s')

# right paddle controls.
screen.onkey(fun=r_paddle.go_up, key='Up')
screen.onkey(fun=r_paddle.go_down, key='Down')

game_is_on = True
while game_is_on:
    # for slower animation of ball.
    time.sleep(ball.move_speed)
    screen.update()
    # moves to top-right motion.
    ball.move()
    # detects the collision of ball with the wall.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    # detects the collision of ball with the left and right paddle.
    if ball.xcor() < -320 and ball.distance(l_paddle) < 50 or ball.xcor() > 320 and ball.distance(r_paddle) < 50:
        ball.x_bounce()

    # ball misses for l_paddle
    if ball.xcor() < -380:
        ball.reset_position()
        # score update for left player.
        scoreboard.l_point()


    # ball misses for r_paddle.
    if ball.xcor() > 380:
        ball.reset_position()
        # score update for right player.
        scoreboard.r_point()

screen.exitonclick()