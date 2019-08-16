from tkinter import *

calc = Tk()
calc.title("Basic Calculator")
e = Entry(calc, font=('arial', 25), fg='lime', bg='black', justify='right', width=15, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


# Define button functions
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_clear():
    e.delete(0, END)


def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)


def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)


def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)


def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)


def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + int(second_number))
    if math == "subtraction":
        e.insert(0, f_num - int(second_number))
    if math == "multiplication":
        e.insert(0, f_num * int(second_number))
    if math == "division":
        e.insert(0, f_num / int(second_number))


# Define buttons
button_1 = Button(calc, font="bold", text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(calc, font="bold", text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(calc, font="bold", text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(calc, font="bold", text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(calc, font="bold", text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(calc, font="bold", text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(calc, font="bold", text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(calc, font="bold", text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(calc, font="bold", text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(calc, font="bold", text="0", padx=40, pady=20, command=lambda: button_click(0))
button_add = Button(calc, font="bold", text="+", padx=39, pady=20, command=button_add)
button_subtract = Button(calc, font="bold", text="-", padx=42, pady=20, command=button_subtract)
button_multiply = Button(calc, font="bold", text="*", padx=41, pady=20, command=button_multiply)
button_divide = Button(calc, font="bold", text="/", padx=42.35, pady=20, command=button_divide)
button_equal = Button(calc, font="bold", text="=", padx=38.35, pady=20, command=button_equal)
button_clear = Button(calc, font="bold", text="C", padx=39.45, pady=20, command=button_clear)

# Display buttons on screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_subtract.grid(row=3, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_multiply.grid(row=2, column=3)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_divide.grid(row=1, column=3)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1)
button_equal.grid(row=4, column=2)
button_add.grid(row=4, column=3)


# Launch calculator
calc.mainloop()