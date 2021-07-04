import turtle, random, sys
from tkinter import *
from turtle import Turtle, Screen

screen = Screen()
screen.setup(800,800)

winheight = 350

turd1 = Turtle('turtle')
turd2 = Turtle('turtle')
turd3 = Turtle('turtle')
turd4 = Turtle('turtle')
turd5 = Turtle('turtle')
turd6 = Turtle('turtle')
turd7 = Turtle('turtle')

turds = {turd1: 'Blue', turd2: 'Yellow', turd3: 'Green', turd4: 'Pink', turd5: 'Orange', turd6: 'Purple', turd7: 'Aqua'}

turd1.color('blue')
turd2.color('yellow')
turd3.color('green')
turd4.color('pink')
turd5.color('orange')
turd6.color('purple')
turd7.color('aqua')

for turd in turds:
    turd.pu()
    turd.lt(90)

turd1.setpos(-250, -300)
turd2.setpos(-250+(500/6), -300)
turd3.setpos(-250+2*(500/6), -300)
turd4.setpos(-250+3*(500/6), -300)
turd5.setpos(-250+4*(500/6), -300)
turd6.setpos(-250+5*(500/6), -300)
turd7.setpos(-250+6*(500/6), -300)

for turd in turds:
    turd.pd()

def move():
    for turd in turds:
        distance = random.randint(1, 50)
        turd.forward(distance)
        if turd.ycor() >= winheight:
            root = Tk()
            root.title('Winner')

            winner = Label(root, text=(turds[turd].upper() + ' has won!'))
            quit_button = Button(root, text='Quit', command=lambda:sys.exit())
            winner.pack()
            quit_button.pack()

            root.mainloop()
            return
    move()

move()

screen.mainloop()