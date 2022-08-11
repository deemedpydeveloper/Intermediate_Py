from tkinter import *

# widgets.

## window.
window = Tk()
window.minsize(width=500, height=300)
window.title("My_Window")

## label.
label = Label(text='Label', font=('Arial', 20, 'bold'))
### grid(row=horizontal_index, column=vertical_index)
label.grid(row=0, column=0)

## button.
button = Button(text='Button', font=('Arial', 20, 'bold'))
button.grid(row=1, column=1)

## button2.
button2 = Button(text='New Button', font=('Arial', 20, 'bold'))
button2.grid(row=0, column=2)

## entry.
entry = Entry(font=('Arial', 20, 'bold'))
entry.insert(END, string='Entry')
entry.grid(row=2, column=3)

## entry2.
entry2 = Entry(font=('Arial', 20, 'bold'))
entry2.insert(END, string='Entry2')
### place(x=pixels,y=pixels)
entry2.place(x=400, y=200)

## Tk method to setup window.
window.mainloop()