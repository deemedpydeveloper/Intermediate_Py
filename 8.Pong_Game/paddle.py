from turtle import Turtle

# class creation.
class Paddle(Turtle):
    # constructor.
    def __init__(self, position):
        # making paddle a super class, to acquire the turtle attributes and methods.
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y_cor = self.ycor() + 20
        self.goto(x=self.xcor(), y=new_y_cor)

    def go_down(self):
        new_y_cor = self.ycor() - 20
        self.goto(x=self.xcor(), y=new_y_cor)

