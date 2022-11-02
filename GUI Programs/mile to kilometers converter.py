from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=500)
window.config(padx=20, pady=20)


def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    # when we click on button, label changes the text:
    my_label_3.config(text=f"{km}")


my_label = Label(text="Miles", font=("Arial", 24, "normal"))
my_label.config(text="Miles")
my_label.grid(column=2, row=0)

my_label_1 = Label(text="is equal to", font=("Arial", 24, "normal"))
my_label_1.grid(column=0, row=1)

my_label_2 = Label(text="Km", font=("Arial", 24, "normal"))
my_label_2.grid(column=2, row=1)

my_label_3 = Label(text="0", font=("Arial", 24, "normal"))
my_label_3.grid(column=1, row=1)

button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)

miles_input = Entry(width=20)
print(miles_input.get())
# input.pack(side="left")
miles_input.grid(column=1, row=0)

window.mainloop()
