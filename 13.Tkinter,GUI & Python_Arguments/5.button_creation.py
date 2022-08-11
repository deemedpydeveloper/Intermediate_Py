from tkinter import *

# window.
window = Tk()
window.minsize(width=500, height=300)
window.title('My First GUI program')

# label.
label = Label(text='My text', font=('Arial', 20, 'bold'))
label.pack()

# ways to change the label text.
label['text'] = "New text"  # kwargs method.
# or
label.config(text="New text")  # tkinter label class method.

# button.
def button_clicked():
    label.config(text="Button Got Clicked")
    new_text = entry.get()
    label.config(text=new_text)


button = Button(text='Click Me', command=button_clicked)
button.pack()


# entry.
entry = Entry(width=30)
entry.pack()


# Use to run above code until closes manually.
window.mainloop()