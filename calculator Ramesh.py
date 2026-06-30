# Calculator creation
from tkinter import *

# step 1 import libraries
windows = Tk()
windows.geometry('500x500')

# step 2 GUI Interaction

# step 3 adding inputs

# Entry Box
e = Entry(windows, width= 56, borderwidth=5)
e.place(x=0,y=0)

# defining function with entry box e and entry num as variable and get the values through command click

def click(num):
    result = e.get()
    e.delete(0,END)
    e.insert(0, str(result) + str(num))

#Buttons
b=Button(windows, text="1", width=12, command=lambda:click(1))
b.place(x = 10, y=60)
b=Button(windows, text="2", width=12, command=lambda:click(2))
b.place(x = 150, y=60)
b=Button(windows, text="3", width=12, command=lambda:click(3))
b.place(x = 290, y=60)
b=Button(windows, text="4", width=12, command=lambda:click(4))
b.place(x = 10, y=100)
b=Button(windows, text="5", width=12, command=lambda:click(5))
b.place(x = 150, y=100)
b=Button(windows, text="6", width=12, command=lambda:click(6))
b.place(x = 290, y=100)
b=Button(windows, text="7", width=12, command=lambda:click(7))
b.place(x = 10, y=140)
b=Button(windows, text="8", width=12, command=lambda:click(8))
b.place(x = 150, y=140)
b=Button(windows, text="9", width=12, command=lambda:click(9))
b.place(x = 290, y=140)
b=Button(windows, text="0", width=12, command=lambda:click(0))
b.place(x = 10, y=180)

# Operators 
def add():
    n1=e.get()
    global math 
    math = "addition"
    global i
    i = int(n1)
    e.delete(0,END)
    
    
b=Button(windows, text="+", width=12, command=add)
b.place(x = 150, y=180)

def sub():
    n1=e.get()
    global  math
    math = "substraction"
    global i
    i = int(n1)
    e.delete(0,END)
b=Button(windows, text="-", width=12, command=sub)
b.place(x = 290, y=180)


def mult():
    n1=e.get()
    global math
    math = "multiplication"
    global i
    i = int(n1)
    e.delete(0,END)
b=Button(windows, text="*", width=12, command=mult)
b.place(x = 10, y=220)


def div():
    n1=e.get()
    global math
    math = "division"
    global i
    i = int(n1)
    e.delete(0,END)
    
b=Button(windows, text="/", width=12, command=div)
b.place(x = 150, y=220)


def equal():
    n2=e.get()
    e.delete(0,END)
    if math == "addition":
        e.insert(0,i + int(n2))
    elif math == "substraction":
        e.insert(0,i - int(n2))
    elif math == "multiplication":
        e.insert(0,i * int(n2))
    elif math == "division":
        e.insert(0,i / int(n2))

b=Button(windows, text="=", width=12, command=equal)
b.place(x = 290, y=220)

def clear():
    e.delete(0, END)
b=Button(windows, text="Clear", width=12, command=clear)
b.place(x = 10, y=260)



# step 4 mainloop
windows.mainloop()