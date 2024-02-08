from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
GERMAN = "Deutsch"
LANGUAGE_FONT = "Arial 40 italic"
WORD_FONT = "Arial 60 bold"
current_card = {}

# -------------------------- CSV PROCESSING ----------------------- #
df = pandas.read_csv(filepath_or_buffer="data/deutsch-english.csv")
to_learn = df.to_dict(orient="records")


def next_card():
    global current_card, flip_timer

    window.after_cancel(flip_timer)

    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="Deutsch", fill="black")
    canvas.itemconfig(card_word, text=current_card["Deutsch"], fill="black")
    canvas.itemconfig(card_background, image=front_image)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=back_image)


def is_known():
    to_learn.remove(current_card)
    next_card()


# ---------------------------- UI SETUP --------------------------- #

window = Tk()
window.geometry("860x750")
window.config(background=BACKGROUND_COLOR, highlightthickness=0, bd=0, borderwidth=0)
window.title("My Flashcard App")

flip_timer = window.after(3000, flip_card)

# Canvas
canvas = Canvas(window, width=800, height=560, highlightthickness=0, borderwidth=0, background=BACKGROUND_COLOR)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(2, 2, anchor=NW, image=front_image)
canvas.grid(row=1, column=1, columnspan=2, padx=35, pady=(50, 0))

card_title = canvas.create_text(400, 150, text='Title', font=LANGUAGE_FONT)
card_word = canvas.create_text(400, 263, text="word", font=WORD_FONT)

# Buttons w PhotoImages
red_image = PhotoImage(file='images/wrong.png')
red_button = Button(image=red_image, highlightthickness=0, command=next_card)
red_button.grid(row=2, column=1, pady=(0, 40))

green_image = PhotoImage(file='images/right.png')
green_button = Button(image=green_image, highlightthickness=0, command=is_known)
green_button.grid(row=2, column=2, pady=(0, 40))

next_card()

window.mainloop()




