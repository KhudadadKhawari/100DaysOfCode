from tkinter import *
import pandas as pd
import random
from tkinter import messagebox
import os

BACKGROUND_COLOR = "#B1DDC6"


#------------------Saving New word list after closing the window---------#
def on_closing():
    if messagebox.askokcancel("Quit", "Do You want to Save Your Progress?"):
        df = pd.DataFrame(analyzed_data, columns=["French","English"])
        df.to_csv("data/progress.csv", index=False)
    window.destroy()

#------------------Reading and Displaying Data----------------#
analyzed_data = []

def open_source_file():
    global analyzed_data
    try:
        data = pd.read_csv('data/progress.csv')
    except:
        data = pd.read_csv('data/french_words.csv')
    analyzed_data = data.to_dict('records')
    next_card()

def reset_progress():
    user_reset_confirm = messagebox.askyesnocancel("Progress File Empty", "You may finished learning All words. The [progress.csv] file is Empty.Do You want to Reset you progress?")   
    if user_reset_confirm:
        os.remove('data/progress.csv')
        open_source_file()
    next_card()


current_card = {}
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    try:
        current_card = random.choice(analyzed_data)
        canva.itemconfig(card_title, text="French")
        canva.itemconfig(card_word, text=current_card["French"])
        canva.itemconfig(canva_image, image = old_image)
        flip_timer = window.after(3000, func=flip_card)
    except:
        # canva.itemconfig(card_word, text="No More Words in the Progress File",font=("Times New Roman", 20, "bold"))
        reset_progress()

def next_card_known():
    global analyzed_data
    try:
        analyzed_data.remove(current_card)
        next_card()
    except: 
        reset_progress()
    

def flip_card():
    canva.itemconfig(canva_image, image = new_image)
    canva.itemconfig(card_title, text="English")
    canva.itemconfig(card_word, text=current_card["English"])

#------------------GUI SETUP-------------------#

window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

old_image = PhotoImage(file="images/card_front.png")
new_image = PhotoImage(file="images/card_back.png")


canva = Canvas(width=800, height=526)
canva.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canva_image = canva.create_image(400,263,image=old_image)
card_title = canva.create_text(400,150, text="Title", font=("Times New Roman", 40, "italic"))
card_word = canva.create_text(400,263, text="word", font=("Times New Roman", 60, "bold"))
open_source_file()


right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

wrong_btn = Button(image=wrong_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=next_card)
right_btn = Button(image=right_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=next_card_known)

canva.grid(row=0,column=0, columnspan=2)
wrong_btn.grid(row=1, column=0)
right_btn.grid(row=1, column=1)



window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()