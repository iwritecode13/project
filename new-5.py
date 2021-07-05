import turtle, os, sys, time
from tkinter import *
from turtle import Turtle, Screen

turd = Turtle('turtle')
turd.color('blue')

def shape(size, corners):
    turd.clear()
    turd.begin_fill()
    for i in range(corners):
        turd.lt(360/corners)
        turd.fd(size)
    turd.end_fill()

root = Tk()
root.title('Turtle')

label1 = Label(root, text='Enter size:')
label2 = Label(root, text='Enter roundness:')
e = Entry(root)
e2 = Entry(root)

confirm = Button(root, text='Confirm', command=lambda:shape(int(e.get()), int(e2.get())))

label1.grid(row=0, column=0, sticky=W)
e.grid(row=0, column=1)
label2.grid(row=1, column=0, sticky=W)
e2.grid(row=1, column=1)
confirm.grid(row=2, column=0, columnspan=2)

root.mainloop()

