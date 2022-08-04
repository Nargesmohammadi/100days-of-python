from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

# label:
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack(side="left")

# changing the label's property
my_label["text"] = "new text"
my_label.config(text="new text")
# replace the label:
# my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)

# button

def button_clicked():
    print("I got clicked.")
    new_text = input.get()
    # when we click on button, label changes the text:
    my_label.config(text=new_text)


button = Button(text="Click me", command=button_clicked)
button.pack(side="left")

# entry
input = Entry(width=10)
input.pack(side="left")
print(input.get())
# return the input as string by get() method:














# keeping the screen by mainloop(): and this line mus be end of our program
window.mainloop()
