from tkinter import *
import pandas
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Tomato")
window.config(padx=100, pady=500)


canvas = Canvas(width=200, height=224)
tomato_img = PhotoImage(file="./Day28/tomato.png")
canvas.create_image(103, 112, image=tomato_img)
canvas.create_text(103, 112, text="00:00")
canvas.pack()









window.mainloop()