from tkinter import *
from PIL import ImageTk, Image
import pygame, os, sys

root = Tk()
root.title('Project')
root.geometry('400x400')
root.config(bg='BLACK')

blue = '#0000ff'

def quit_func():
    root.destroy()
    sys.exit()

label = Label(root, text='test', bg=blue, fg='WHITE')

button_quit = Button(root, text='quit', highlightbackground='WHITE', highlightforeground=blue, command=quit_func)

label.grid(row=0, column=0)
button_quit.grid(row=1, column=0)

root.mainloop()