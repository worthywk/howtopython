from tkinter import *

clicks_button1 = 0
clicks_button2 = 0


def button_click_add_window():
    global clicks_button1
    clicks_button1 += 1
    window = Tk()
    buttonText = StringVar(window)
    buttonText.set("Clicks: {}".format(clicks_button1))
    window.title("Clicks: {}".format(clicks_button1))
    window.geometry('300x300')

    button = Button(window,
                    textvariable=buttonText,
                    bg="white",  # фоновый цвет кнопки
                    fg="#97270E",
                    activeforeground="green",
                    relief=RIDGE,
                    padx="15",  # отступ от границ до содержимого по горизонтали
                    pady="15",  # отступ от границ до содержимого по вертикали
                    font=("Verdana", 14, "bold"),
                    command=button_click_add_window)

    button.pack()
    window.mainloop()


def button_click_add_button():
    global clicks_button2
    clicks_button2 += 1
    button = Button(text="Create new button",
                    bg="white",  # фоновый цвет кнопки
                    fg="#97270E",
                    activeforeground="green",
                    relief=RIDGE,
                    padx="15",  # отступ от границ до содержимого по горизонтали
                    pady="15",  # отступ от границ до содержимого по вертикали
                    font=("Verdana", 12, "bold"),
                    command=button_click_add_button)

    button.pack()

