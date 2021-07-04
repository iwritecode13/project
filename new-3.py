import turtle, random, sys
from turtle import Turtle, Screen

screen = Screen()
screen.setup(800, 800)
screen.tracer(0, 0)

turd = Turtle('turtle')
turd.speed(0)

def square(size):
    turd.pd()
    turd.color('lightblue')
    turd.begin_fill()
    for i in range(4):
        turd.fd(size)
        turd.lt(90)
    turd.end_fill()
    turd.pu()

def triangle(size):
    turd.pd()
    turd.color('black')
    turd.begin_fill()
    turd.lt(30)
    turd.forward(size)
    turd.lt(120)
    turd.forward(size)
    turd.lt(120)
    turd.forward(size)
    turd.end_fill()
    turd.pu()

def hexagon(size):
    turd.pd()
    turd.color('pink')
    turd.begin_fill()
    for i in range(6):
        turd.lt(60)
        turd.forward(size)
    turd.end_fill()
    turd.pu()

def shape():
    hexagon(30)
    turd.rt(30)
    for i in range(6):
        turd.rt(150)
        turd.fd(30)
        turd.lt(90)
        square(30)

    turd.fd(30)
    turd.lt(90)
    turd.fd(30)
    triangle(30)
    
    for i in range(5):
        turd.lt(120)
        turd.fd(30)
        turd.lt(30)
        turd.fd(30)
        triangle(30)

def row():
    shape()
    for i in range(4):
        turd.fd(-30)
        turd.lt(150)
        turd.fd(30)
        turd.rt(30)
        turd.fd(30)
        turd.rt(30)
        turd.fd(30)
        shape()
        turd.lt(120)
        turd.fd(30)
        turd.rt(90)
        turd.fd(30)
        turd.lt(60)
        turd.fd(30)
        shape()

def move(times):
    turd.pu()
    turd.setpos(-225, -275)
    for i in range(times):
        turd.fd(30)
        turd.lt(30)
        turd.fd(30)
        turd.rt(60)
        turd.fd(30)
        turd.lt(30)
    
    turd.lt(90)
    turd.stamp()

move(0)
for i in range(7):
    row()
    move(i+1)

screen.mainloop()