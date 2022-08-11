import tkinter

# setting window features.
window = tkinter.Tk()
window.minsize(width=500, height=300)
window.title('My First GUI Program',)

# setting label in th window.
my_label = tkinter.Label(text='My First Label', font=('Arial', 24, 'bold'))
my_label.pack()  # it is a geometrical-based function, used to hold the features of window.
# my_label.pack(expand=True)  ## packs to centre.
# my_label.pack(side='left')  ## packs to left.


# window is displayed by looping through above code only.
window.mainloop()