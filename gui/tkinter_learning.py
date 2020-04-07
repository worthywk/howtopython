from tkinter import *
from button_functions import *

root = Tk()

root.title("Python GUI")
root.geometry('500x500-0+0')

btn = Button(text="Create new window",
             bg="white",  # фоновый цвет кнопки
             fg="#97270E",
             activeforeground="green",
             relief=RIDGE,
             font=("Verdana", 12, "bold"),
             command=button_click_add_window)


btn1 = Button(text="Create new button",
             bg="white",  # фоновый цвет кнопки
             fg="#97270E",
             activeforeground="green",
             relief=RIDGE,
            padx = '50',
            pady = '50',
             font=("Verdana", 12, "bold"),
             command=button_click_add_button)

# btn1.config(text="END")

btn.place(x=0, y=0, width=250, heigh=100)
btn1.place(x=250, y=0, width=250, heigh=100)

root.mainloop()
