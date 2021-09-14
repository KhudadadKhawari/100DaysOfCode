import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    #title label "Timer"
    title_label.config(text ="Timer")
    #timer_label "00:00"
    canvas.itemconfig(timer_text, text=f"00:00")
    #reset Chick_marks
    tick_mark_label.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0: # if it's the 8th rep
        count_down(long_break_sec)
        title_label.config(text ="Break", fg = RED)
    elif reps % 2 == 0: # if it's the 2nd/ 4th/ 6th rep
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else: # if it's the 1st /3rd /5th /7th rep
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_minute = math.floor( count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'

    canvas.itemconfig(timer_text, text = f"{count_minute}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            marks += "✔"
        tick_mark_label.config(text = marks)



# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *

window = Tk()
window.title("Pomodoro")
window.config(padx = 100, pady = 50, bg = YELLOW)


title_label = Label(text ="Timer", bg = YELLOW, fg = GREEN, font = (FONT_NAME, 40, 'bold'))
title_label.grid(row = 0, column = 1)

canvas = Canvas(width = 200, height = 224, bg = YELLOW, highlightthickness = 0)
tomato_image = PhotoImage(file = "tomato.png")
canvas.create_image(100,112, image = tomato_image)
timer_text = canvas.create_text(100, 130, text ="00:00", fill ="white", font = (FONT_NAME, 35, "bold"))
canvas.grid(row = 1, column = 1)



tick_mark_label = Label(font = (FONT_NAME, 14), fg=GREEN, bg=YELLOW)
tick_mark_label.grid(row = 2, column = 1)

start_button = Button(text = "Start", highlightthickness = 0, command = start_timer)
start_button.grid(row = 2, column = 0)

reset_button = Button(text = "Reset", highlightthickness = 0, command = reset_timer)
reset_button.grid(row = 2, column = 3)



window.mainloop()
