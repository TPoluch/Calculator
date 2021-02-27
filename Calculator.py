from tkinter import *

root = Tk()
root.title("Calculator_GUI")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)



#e.insert(0,"")

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_add():
    first_number = e.get()
    global num1
    global math
    math = "add"
    num1 = int(first_number)
    e.delete(0, END)

def button_subtract():
    first_number = e.get()
    global num1
    global math
    math = "subtract"
    num1 = int(first_number)
    e.delete(0, END)

def button_multiply():
    first_number = e.get()
    global num1
    global math
    math = "multiply"
    num1 = int(first_number)
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    global num1
    global math
    math = "divide"
    num1 = int(first_number)
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "add":
        e.insert(0, num1 + int(second_number))
    elif math == "subtract":
        e.insert(0, num1 - int(second_number))
    elif math == "multiply":
        e.insert(0, num1 * int(second_number))
    elif math == "divide":
        e.insert(0, num1 / int(second_number))

def button_clear():
    e.delete(0, END)
# define buttons




button_1 = Button(root, text="1", bg="Royal Blue4", fg="dark orange", padx=40, pady=20, command=lambda : button_click(1))
button_2 = Button(root, text="2", bg="Royal Blue4", fg="dark orange", padx=40, pady=20, command=lambda : button_click(2))
button_3 = Button(root, text="3", bg="Royal Blue4", fg="dark orange", padx=40, pady=20, command=lambda : button_click(3))
button_4 = Button(root, text="4", bg="Royal Blue4", fg="dark orange", padx=40, pady=20, command=lambda : button_click(4))
button_5 = Button(root, text="5", bg="Royal Blue4", fg="dark orange", padx=40, pady=20, command=lambda : button_click(5))
button_6 = Button(root, text="6", bg="Royal Blue4", fg="dark orange", padx=40, pady=20, command=lambda : button_click(6))
button_7 = Button(root, text="7", bg="Royal Blue4", fg="dark orange", padx=40, pady=20, command=lambda : button_click(7))
button_8 = Button(root, text="8", bg="Royal Blue4", fg="dark orange", padx=40, pady=20, command=lambda : button_click(8))
button_9 = Button(root, text="9", bg="Royal Blue4", fg="dark orange", padx=40, pady=20, command=lambda : button_click(9))
button_0 = Button(root, text="0", bg="Royal Blue4", fg="dark orange", padx=40, pady=20, command=lambda : button_click(0))
button_add = Button(root, text="+", bg="snow3", fg="black", padx=40, pady=20, command=button_add)
button_subtract = Button(root, text="-", bg="snow3", fg="black", padx=40, pady=20, command=button_subtract)
button_multiply = Button(root, text="*", bg="snow3", fg="black", padx=40, pady=20, command=button_multiply)
button_divide = Button(root, text="/", bg="snow3", fg="black", padx=40, pady=20, command=button_divide)
button_equal = Button(root, text="=", bg="dark orange", fg="Royal Blue4", padx=90, pady=20, command=button_equal)
button_clear = Button(root, text="AC", bg="red3", fg="white", width = 35, padx=40, pady=10, command=button_clear)

#position buttons on screen

button_1.grid(row=2, column=0)
button_2.grid(row=2, column=1)
button_3.grid(row=2, column=2)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)

button_7.grid(row=4, column=0)
button_8.grid(row=4, column=1)
button_9.grid(row=4, column=2)

button_0.grid(row=5, column=0)
button_add.grid(row=2,column=3)
button_subtract.grid(row=3,column=3)
button_multiply.grid(row=4,column=3)
button_divide.grid(row=5,column=3)
button_equal.grid(row=5, column=1, columnspan=2)
button_clear.grid(row=1, column=0, columnspan=4)


root.mainloop()