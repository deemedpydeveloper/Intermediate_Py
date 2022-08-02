from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1  # for changing the speed of ball.

    # top-right motion.
    def move(self):
        new_xcor = self.xcor() + self.x_move
        new_ycor = self.ycor() + self.y_move
        self.goto(new_xcor, new_ycor)

    # bounces when hits the wall.
    def y_bounce(self):
        self.y_move *= -1

    # bounce when hits the paddle.
    def x_bounce(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    # resets the position to centre.
    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.x_bounce()

