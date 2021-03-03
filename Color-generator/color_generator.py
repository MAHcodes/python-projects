from tkinter import *
from tkinter import colorchooser
import random
import colors

root = Tk()

root.geometry("300x400")
root.title("Color Chooser")
root.resizable(False, False)

def choose():
    color = colorchooser.askcolor()
    root.config(bg=(color[1]))
    lbl2.config( text="Your Chosen Hex color code is: ", bg="#a3a3a3")
    lbl3.config(text=color[1], bg="#a3a3a3")


def random_color():
    rand_color = random.choice(colors.COLORS)
    root.config(bg=(rand_color))
    lbl2.config(text="Your random color is: ", bg="#a3a3a3")
    lbl3.config(text=rand_color, bg="#a3a3a3")


def clear():
    root.config(bg="white")
    lbl2.config(text="", bg="white")
    lbl3.config(text="", bg="white")


root.config(bg="black")
lbl = Label(root, text="Hello, Press the button to choose color", height=2, width=34, bg="#a3a3a3", fg="black").pack(pady=20)
btn = Button(root, text="Choose color", width=15, command=choose, bg="#a3a3a3", fg="black", relief=GROOVE).pack(pady=15)
lbl2 = Label(root, bg="black")
lbl3 = Label(root, width=20, bg="black")
lbl2.pack(pady=10)
lbl3.pack(pady=10)
btn2 = Button(root, text="Random Color", width=15, command=random_color, bg="#a3a3a3", fg="black", relief=GROOVE).pack(pady=50)
btn3 = Button(root, text="Clear", width=15, command=clear, bg="#a3a3a3", fg="black", relief=GROOVE).pack()




root.mainloop()
