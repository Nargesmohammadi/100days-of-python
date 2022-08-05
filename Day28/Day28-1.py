from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 20
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 25
reps = 0


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timerr():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN
    long_break_sec = LONG_BREAK_MIN

    if reps % 8 == 0:
        count_down(long_break_sec)
        new_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        new_label.config(text="Break", fg=YELLOW)
    else:
        count_down(work_sec)
        new_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    # for have to 00:00 when second is less than 10.
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        start_timerr()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Tomato")
window.config(padx=100, pady=50, bg=PINK)

new_label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), bg=PINK, fg=GREEN)
new_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=PINK, highlightthickness=0)
tomato_img = PhotoImage(file="./Day28/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 112, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", font=(FONT_NAME, 25, "bold"), command=start_timerr)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", font=(FONT_NAME, 25, "bold"))
reset_button.grid(column=2, row=2)

checkmark_label = Label(text="✔", font=(FONT_NAME, 25, "bold"), bg=PINK, fg=GREEN)
checkmark_label.grid(column=1, row=3)

window.mainloop()
