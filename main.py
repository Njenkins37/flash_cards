from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

#--------------------CREATE CARDS-------------------------#
def correct_button():
    with open('./data/french_words.csv') as file:
        data = pandas.read_csv(file)
        data_dict = data.to_dict()
        num = random.randint(0, len(data))

        french_text = data_dict['French'][num]

        canvas.itemconfig(word, text=french_text)
        window.update()
        window.after(5000, flip_card(num))


#----------------------WRONG------------------------------#

def got_it_wrong():
    with open('./data/french_words.csv') as file:
        data = pandas.read_csv(file)
        data_dict = data.to_dict()
        num = random.randint(0, len(data))
        french_text = data_dict['French'][num]

        canvas.itemconfig(word, text=french_text)
        window.update()
        window.after(5000, flip_card(num))

#---------------------FLIP CARD---------------------------#
def flip_card(needed_num):
    with open('./data/french_words.csv') as file:
        data = pandas.read_csv(file)
        data_dict = data.to_dict()
        english_text = data_dict['English'][needed_num]
        canvas.itemconfig(word, text=english_text)

#-----------------------UI--------------------------------#
window = Tk()
window.title('Flash Cards')
window.config(bg=BACKGROUND_COLOR, padx=20, pady=20)
window.minsize(width=800, height=600)

card_front = PhotoImage(file='/Users/nickjenkins/Downloads/flash-card-project-start/images/card_back.png')
right = PhotoImage(file='./images/right.png')
wrong = PhotoImage(file='./images/wrong.png')

canvas = Canvas(width=600, height=400, highlightthickness=0)
canvas.create_image(400, 200, image=card_front)
word = canvas.create_text(300, 200, text='Flash Cards', font=('Arial', 48, 'normal'))
canvas.grid(row=0, column=2)

right_button = Button(image=right,width=100, height=100, highlightthickness=0, command=correct_button, highlightcolor=BACKGROUND_COLOR)
right_button.grid(row=1, column=3)

wrong_button = Button(image=wrong, width=100, height=100, highlightthickness=0, command=got_it_wrong, highlightcolor=BACKGROUND_COLOR)
wrong_button.grid(row=1, column=0)

window.mainloop()