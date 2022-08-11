# Miles to Kilometers Converter.

# importing all classes from tkinter module.
from tkinter import *

# calculate function.
def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    kilometer_result_label.config(text=f'{km}')

# window.
window = Tk()
window.title('Mile to Km Converter')
window.config(padx=20, pady=20)

# entry.
miles_input = Entry(width=7)
miles_input.grid(row=0, column=1)

# label1.
miles_label = Label(text='Miles')
miles_label.grid(row=0, column=2)

# label2.
is_equal_label = Label(text='is equal to')
is_equal_label.grid(row=1, column=0)

# label3.
kilometer_result_label = Label(text='0')
kilometer_result_label.grid(row=1, column=1)

# label4.
kilometer_label = Label(text='Km')
kilometer_label.grid(row=1, column=2)

# button.
calculate_button = Button(text='Calculate', command=miles_to_km)
calculate_button.grid(row=2, column=1)

# method to avoid window display error.
window.mainloop()