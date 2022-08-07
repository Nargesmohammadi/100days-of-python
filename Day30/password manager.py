from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

FONT_NAME = "Courier"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password1 = "".join(password_list)
    password_input.insert(0, password1)
    pyperclip.copy(password1)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {website:{
        "email": email,
        "password": password,
    }}

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Oops", message="please make sure you have not left any fields empty.")

    else:
        with open("data.jason", "r") as data_file:
            # reading old data:
            data = json.load(data_file)
            # updating old data with new data:
            data.update(new_data)
        with open("data.jason", "w") as data_file:
            # saving updated data:
            json.dump(data, data_file, indent=4)

            website_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="./Day29/logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", font=(FONT_NAME, 15, "bold"))
website_label.grid(column=0, row=1)
website_input = Entry(width=45)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

email_label = Label(text="Email/Username:", font=(FONT_NAME, 15, "bold"))
email_label.grid(column=0, row=2)
email_input = Entry(width=45)
email_input.grid(column=1, row=2, columnspan=2)
# email_input.insert(0, "Narges@gmail.com")

Password_label = Label(text="Password:", font=(FONT_NAME, 15, "bold"))
Password_label.grid(column=0, row=3)
password_input = Entry(width=24)
password_input.grid(column=1, row=3)

Generate_Password_button = Button(text="Generate Password", font=(FONT_NAME, 10, "bold"), command=generate_password)
Generate_Password_button.grid(column=2, row=3)

add_button = Button(text="add", font=(FONT_NAME, 15, "bold"), width=29, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
