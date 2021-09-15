from tkinter import *
import pandas
from random import *

BACKGROUND_COLOR = "#B1DDC6"

try:
    panda = pandas.read_csv('words_to_learn.csv')
    print("using learnt words.")
except FileNotFoundError:
    panda = pandas.read_csv('./data/french_words.csv')
    print('No history. Using all words')

words_dict = panda.to_dict(orient="records")

print(words_dict)
current_card = {}


def word_known():
    words_dict.remove(current_card)
    data = pandas.DataFrame(words_dict)
    data.to_csv('words_to_learn.csv', index=False)
    next_card()


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfigure(flashcard, image=flash_card_front)
    current_card = choice(words_dict)
    canvas.itemconfigure(word_text, text=current_card['French'], fill="black")
    canvas.itemconfigure(language_text, text="French", fill="black")
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    global current_card
    canvas.itemconfigure(word_text, text=current_card['English'], fill="white")
    canvas.itemconfigure(language_text, text="English", fill="white")
    canvas.itemconfigure(flashcard, image=flash_card_back)

window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
cross = PhotoImage(file="./images/wrong.png")
check = PhotoImage(file="./images/right.png")
flash_card_front = PhotoImage(file="./images/card_front.png")
flash_card_back = PhotoImage(file="./images/card_back.png")
flashcard = canvas.create_image(400, 263, image=flash_card_front)
language_text = canvas.create_text(400, 150, text="", font=('Arial', 40, 'italic'))
word_text = canvas.create_text(400, 263, text="", font=('Arial', 50, 'bold'))
wrong_button = Button(image=cross, highlightthickness=0, command=next_card)
right_button = Button(image=check, highlightthickness=0, command=word_known)
wrong_button.grid(column=0, row=1)
right_button.grid(column=1, row=1)
flip_timer = window.after(3000, func=flip_card)

canvas.grid(column=0, row=0, columnspan=2)


next_card()
window.mainloop()