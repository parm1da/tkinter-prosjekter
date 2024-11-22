from tkinter import *
import math

root = Tk()
root.title("kalkulator")

e = Entry(root,width = 50, borderwidth = 5, justify = "right")
e.grid(row = 0, column = 0, columnspan=5, padx = 10, pady=10)

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0,str(current) + str(number))
    
def button_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num 
    global matte
    matte = "addition"
    f_num = float(first_number)
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if matte == "addition":
        e.insert(0, f_num + float(second_number))
    if matte == "subtraction":
        e.insert(0, f_num - float(second_number))
    if matte == "multiplication":
        e.insert(0, f_num * float(second_number))
    if matte == "division":
        e.insert(0, f_num / float(second_number))
    if matte == "prosent":
        e.insert(0, (f_num * float(second_number)/100))
    if matte == "eksponent":
        e.insert(0, (f_num**float(second_number)))
    if matte == "kvadratrot":
        e.insert(0, math.sqrt(f_num))

def button_subtract():
    first_number = e.get()
    global f_num # gjør global så kan brukes i andre funksjoner
    global matte
    matte = "subtraction"
    f_num = float(first_number)
    e.delete(0, END)

def button_multiply():
    first_number = e.get()
    global f_num 
    global matte
    matte = "multiplication"
    f_num = float(first_number)
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    global f_num 
    global matte
    matte = "division"
    f_num = float(first_number)
    e.delete(0, END)

def button_prosent():
    first_number = e.get()
    global f_num 
    global matte
    matte = "prosent"
    f_num = float(first_number)
    e.delete(0, END)

def button_eksponent():
    first_number = e.get()
    global f_num 
    global matte
    matte = "eksponent"
    f_num = float(first_number)
    e.delete(0, END)

def button_kvadratrot():
    first_number = e.get()
    global f_num 
    global matte
    matte = "kvadratrot"
    f_num = float(first_number)
    e.delete(0, END)

button_1 = Button(root, text = "1", padx=4, pady=2, command = lambda: button_click(1))
button_2 = Button(root, text = "2", padx=4, pady=2, command = lambda: button_click(2))
button_3 = Button(root, text = "3", padx=4, pady=2, command = lambda: button_click(3))
button_4 = Button(root, text = "4", padx=4, pady=2, command = lambda: button_click(4))
button_5 = Button(root, text = "5", padx=4, pady=2, command = lambda: button_click(5))
button_6 = Button(root, text = "6", padx=4, pady=2, command = lambda: button_click(6))
button_7 = Button(root, text = "7", padx=4, pady=2, command = lambda: button_click(7))
button_8 = Button(root, text = "8", padx=4, pady=2, command = lambda: button_click(8))
button_9 = Button(root, text = "9", padx=4, pady=2, command = lambda: button_click(9))
button_0 = Button(root, text = "0", padx=4, pady=2, command = lambda: button_click(0))
button_pi = Button(root, text = "π", padx=4, pady=2, command = lambda: button_click(3.14))
button_add = Button(root, text = "+", padx=5, pady=2, command = button_add)
button_equal = Button(root, text = "=", padx=9, pady=2, command = button_equal)
button_clear = Button(root, text = "Clear", padx=4, pady=2, command = button_clear)

button_subtract = Button(root, text = "-", padx=4, pady=2, command = button_subtract)
button_multiply = Button(root, text = "*", padx=4, pady=2, command = button_multiply)
button_divide = Button(root, text = "/", padx=4, pady=2, command = button_divide)
button_prosent = Button(root, text = "%", padx=4, pady=2, command = button_prosent)
button_eksponent = Button(root, text = "x^n", padx=4, pady=2, command = button_eksponent)
button_kvadratrot = Button(root, text = "√", padx=4, pady=2, command = button_kvadratrot)
label_tom = Label(root, text="   ")

button_1.grid(row=4 ,column =0, sticky = "nsew")
button_2.grid(row=4 ,column =1, sticky = "nsew")
button_3.grid(row=4 ,column =2, sticky = "nsew")

button_4.grid(row=3 ,column =0, sticky = "nsew")
button_5.grid(row=3 ,column =1, sticky = "nsew")
button_6.grid(row=3 ,column =2, sticky = "nsew")

button_7.grid(row=2 ,column =0, sticky = "nsew")
button_8.grid(row=2 ,column =1, sticky = "nsew")
button_9.grid(row=2 ,column =2, sticky = "nsew")

button_0.grid(row=5 ,column = 0, columnspan=3, sticky = "nsew")

button_clear.grid(row = 1, column = 0, sticky = "w")
label_tom.grid(row=1, column=1, sticky = "nsew")
button_pi.grid(row = 1, column = 3, sticky = "nsew")
button_kvadratrot.grid(row = 1, column = 4, sticky = "nsew")

button_divide.grid(row =2, column =3, sticky = "nsew")
button_prosent.grid(row =2, column =4, sticky = "nsew")

button_multiply.grid(row =3, column =3, sticky = "nsew")
button_eksponent.grid(row = 3, column = 4, sticky = "nsew")

button_subtract.grid(row = 4, column =3, sticky = "nsew")
button_add.grid(row = 5, column = 3, sticky = "nsew")
button_equal.grid(row = 4, column = 4, rowspan = 2, sticky = "nsew")

root.mainloop()