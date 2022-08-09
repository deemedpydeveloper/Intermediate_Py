import turtle

screen = turtle.Screen()

screen.title("U.S. States Game")
image = 'blank_states_img.gif'
screen.addshape(image)

turtle.shape(image)

def get_coor_on_mouse_click(x, y):
    print(x, y)


screen.onscreenclick(get_coor_on_mouse_click)
screen.mainloop()