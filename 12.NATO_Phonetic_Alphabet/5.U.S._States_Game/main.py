import turtle
import pandas
data = pandas.read_csv('50_states.csv')
all_states = data.state.to_list()

screen = turtle.Screen()
image = 'blank_states_img.gif'
screen.addshape(image)  # ads the shape of an image to the screen.
screen.title('U.S. States Game')


turtle.shape(image)  # setting the turtle shape as image.

guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f'{len(guessed_states)}/50', prompt='Guess the another state\'s name.').title()
    # secret code to exit the game
    missing_states = []
    # before exiting, making the code to track of missed states.
    if answer_state == 'Exit':
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        ## By list comprehension method.
        missing_states = [state for state in all_states if state not in guessed_states]
        missing_states_data = pandas.DataFrame(missing_states)
        missing_states_data.to_csv('states_to_learn.csv')
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)  # appends the state every time the user guesses correctly.
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        # t.write(state_data.state.item()) ---> an alternative to below step.
        t.write(answer_state)