# Create a screen with width 800 and height 600.
## importing screen class from turtle module.
## creating a screen object from screen class.
## setting screen width 800 and screen height 600.
## setting screen background color black.
## setting the title of screen.
## setting the screen to exit on click.

# Create a Paddle that responds to Key Presses.
## importing turtle class from turtle module.
## create paddle object from turtle class.
## set the size of paddle object of width 5 and height 1.
## set the color of paddle object to white.
## set the animation halt by tracer method initially.
## set the penup mode of paddle object to avoid unnecessary drawings on screen.
## set the paddle object position to x = 350 and y = 0.
## At last, set the screen to update animation.

# Creating the paddle class and second paddle.
## paddle related code need to separated by creating paddle class.
## refactor all paddle. with self.
## creating a method for creating left and right paddles.
## creating method for go up and go down of paddles.

# Write the Ball Class and Make the Ball Move.
## create a separate module with ball class.
## make ball as super class.
## make ball to move to top right for every refresh of screen.

# Detect the ball collision with the wall.
## create bounce method in ball class.
## make the logic to reverse its direction.
## call that function in while loop of main.py.

# Detect the Collisions with the Paddle.
## make a method in ball class to reverse its direction when hit the paddle.
## make a condition in while loop for bouncing back for both the paddles.

# Detect when ball goes out of bounds.
## make a method in ball class to reset its position to centre and start off by bouncing in opposite direction.
## call that method in while loop separately for left and right paddles.(to score them separately).

# Change the score for left and right side players.
## create a scoreboard class in separate module.
## display score on left and right side respectively.
## update scoreboard each time the ball misses.
## make an attribute in ball class to change speed of ball when touches the paddle.
## change the speed of ball everytime the paddle touches the ball and reset speed to default on reset position.