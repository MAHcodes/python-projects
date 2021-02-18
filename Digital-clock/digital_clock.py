import tkinter
import time

root = tkinter.Tk()
root.title("Digital Clock")
root.resizable(False, False)

def get_time():
    timeVar = time.strftime("%H:%M:%S")
    clock_label.config(text=timeVar)
    clock_label.after(200, get_time)


clock_label = tkinter.Label(root, font=("Ds-Digital", 100), bg="black", fg="white", width=7, height=1)
clock_label.pack()

get_time()
root.mainloop()