import tkinter

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)


# label:
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()











# keeping the screen by mainloop(): and this line mus be end of our program
window.mainloop()
