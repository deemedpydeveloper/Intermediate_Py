from turtle import Turtle, Screen

# moves the turtle by a distance.
timmy = Turtle()
timmy.forward(20)
timmy.backward(10)
## or
timmy.fd(20)
timmy.bk(10)


# moves th turtle by an angle.
timmy.right(90)
timmy.lt(45)
## or
timmy.rt(90)
timmy.lt(45)


# returns the current position of turtle.
print(timmy.position())
## or
print(timmy.pos())


# returns the angle between positions.
print(timmy.towards(0, 0))
## or
print(timmy.goto(10, 10))




screen = Screen()
screen.exitonclick()