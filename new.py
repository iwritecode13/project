import turtle
import random

turd = turtle.Turtle()
turd.speed(0)
turd.pensize(5)

colors = ['red', 'blue', 'green', 'purple', 'yellor', 'orange', 'black']

def up():
    turd.setheading(90)
    turd.forward(100)

def down():
    turd.setheading(270)
    turd.forward(100)

def left():
    turd.setheading(180)
    turd.forward(100)

def right():
    turd.setheading(0)
    turd.forward(100)

def clickleft(x, y):
    turd.color = random.choice(colors)

def clickright(x, y):
    turd.stamp()

turtle.listen()

# turtle.onclick(clickleft, 1)

turtle.onscreenclick(clickleft)
turtle.onscreenclick(clickright, 3)

turtle.onkey(up, 'Up')
turtle.onkey(down, 'Down')
turtle.onkey(right, 'Right')
turtle.onkey(left, 'Left')

turtle.done()