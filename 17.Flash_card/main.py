from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv('data/french_words.csv')
except FileNotFoundError:
    original_data = pandas.read_csv('data/french_words.csv')
    to_learn = data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(canvas_title, text='French', fill='black')
    canvas.itemconfig(canvas_word, text=current_card["French"], fill='black')
    canvas.itemconfig(card_background, image=card_front_image)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(canvas_title, text='English', fill='white')
    canvas.itemconfig(canvas_word, text=current_card["English"], fill='white')
    canvas.itemconfig(card_background, image=card_back_image)


def is_known():
    to_learn.remove(current_card)
    # print(len(to_learn))
    data2 = pandas.DataFrame(to_learn)
    data2.to_csv('data/words_to_learn.csv', index=False)  # deletes indices in csv file.
    next_card()


# window creation.
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# canvas creation.
canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file='images/card_front.png')
card_back_image = PhotoImage(file='images/card_back.png')
card_background = canvas.create_image(400, 263, image=card_front_image)
canvas_title = canvas.create_text(400, 120, text='', font=("Ariel", 40, 'italic'))
canvas_word = canvas.create_text(400, 263, text='', font=("Ariel", 60, 'bold'))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# buttons creation.
cross_image = PhotoImage(file='images/wrong.png')
unknown_button = Button()
unknown_button.config(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file='images/right.png')
known_button = Button()
known_button.config(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()