import random
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Random Password Generator")
root.geometry("200x380+400+100")
root.resizable(False, False)
var = IntVar()
chVar1 = BooleanVar()
chVar1.set(True)
chVar2 = BooleanVar()
chVar2.set(True)
chVar3 = BooleanVar()
chVar3.set(True)
chVar4 = BooleanVar()
chVar4.set(True)

pwd = ""
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWYXZ"
lower_case = upper_case.lower()
num = "0123456789"
symbols = "!@#$%^&*~?/"


def generate():
    chosen = ''
    if chVar1.get() == False and chVar2.get() == False and chVar3.get() == False and chVar4.get() == False:
        messagebox.showwarning("Error", "Please check at least one")
    else:
        if chVar1.get():
            chosen += upper_case
        if chVar2.get():
            chosen += lower_case
        if chVar3.get():
            chosen += num
        if chVar4.get():
            chosen += symbols

        length = var.get()
        pwd = "".join(random.sample(chosen, length))
        txt.delete(1.0, "end")
        txt.insert(1.0, pwd)
        txt.focus()
        chosen =''


def check():
    if (chVar1.get() == False and chVar2.get() == False and chVar3.get() == False and chVar4.get()) or (chVar1.get() == False and chVar2.get() == False and chVar4.get() == False and chVar3.get()):
        scale.config(to=10, tickinterval=1)
    else:
        scale.config(to=20, tickinterval=2)


label1 = Label(root, text="Password strength:").pack(pady=5)
check1 = Checkbutton(root, text="Uppercase", onvalue=1, offvalue=0, variable=chVar1, command=check).pack()
check2 = Checkbutton(root, text="Lowercase", onvalue=1, offvalue=0, variable=chVar2, command=check).pack()
check3 = Checkbutton(root, text="Numbers", onvalue=1, offvalue=0, variable=chVar3, command=check).pack()
check4 = Checkbutton(root, text="Symbols", onvalue=1, offvalue=0, variable=chVar4, command=check).pack()
scale = Scale(root, orient=HORIZONTAL, length=150, label="Password length", from_=8, to=20, width=10, tickinterval=2, variable=var)
scale.pack(pady=20)
lbl3 = Label(root, text="Your random password is: ").pack(pady=20)
txt = Text(root, height=1, width=22)
txt.pack()
btn = Button(root, text="Generate", command=generate).pack(pady=10)
root.mainloop()