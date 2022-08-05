from tkinter import *


# button
def button_clicked():
    print("I got clicked.")
    new_text = input.get()
    # when we click on button, label changes the text:
    my_label.config(text=new_text)


window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
# add around window a lot of space:
window.config(padx=20, pady=20)

# label:
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))


# changing the label's property
my_label["text"] = "new text"
my_label.config(text="new text")
# replace the label:
# my_label.place(x=0, y=0)
# my_label.pack(side="left")
my_label.grid(column=0, row=0)
my_label.config(padx=30, pady=30)

button = Button(text="Click me", command=button_clicked)
new_button = Button(text="New button", command="mhd")
# button.pack(side="left")
button.grid(column=1, row=1)
new_button.grid(column=2, row=0)

# entry
input = Entry(width=20)
print(input.get())
# input.pack(side="left")
input.grid(column=3, row=2)
# return the input as string by get() method:


# keeping the screen by mainloop(): and this line mus be end of our program
window.mainloop()
