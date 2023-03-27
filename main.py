from tkinter import *


def calculate():
    convert = round(int(input_num.get()) * 0.6214, 2)
    num.config(text=convert)


window = Tk()
window.title("公里轉英里")
window.minsize(height=200, width=300)
window.config(padx=50, pady=50)

input_num = Entry(width=10, justify='center')
input_num.focus_set()
input_num.grid(row=0, column=1)

miles = Label(text="英里")
miles.grid(row=1, column=2)

equal = Label(text="等於")
equal.grid(row=1, column=0)
equal.config(padx=20, pady=20)

km = Label(text="公里")
km.grid(row=0, column=2)
km.config(padx=20)

num = Label(text="0")
num.grid(row=1, column=1)
num.config(padx=20, pady=20)

cal = Button(text="計算", command=calculate)
cal.grid(row=2, column=1)

window.mainloop()
