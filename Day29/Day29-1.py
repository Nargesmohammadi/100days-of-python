from tkinter import *

FONT_NAME = "Courier"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    with open("data.txt", "a") as data_file:
        data_file.write(f"{website} | {email} | {password}\n")
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
email_input.insert(0, "Narges@gmail.com")

Password_label = Label(text="Password:", font=(FONT_NAME, 15, "bold"))
Password_label.grid(column=0, row=3)
password_input = Entry(width=24)
password_input.grid(column=1, row=3)

Generate_Password_button = Button(text="Generate Password", font=(FONT_NAME, 10, "bold"))
Generate_Password_button.grid(column=2, row=3)

add_button = Button(text="add", font=(FONT_NAME, 15, "bold"), width=29, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
