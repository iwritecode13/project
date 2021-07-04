import turtle
import random

turd = turtle.Turtle()
turd.speed(0)
turd.pensize(5)

colors = ['red', 'blue', 'green', 'purple', 'yellow', 'orange', 'black']

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
    turd.color(random.choice(colors))

def clickright(x, y):
    print('rightclick')
    turd.stamp()

turtle.listen()

# turtle.onclick(clickleft, 1)

turtle.onscreenclick(clickleft, 1)
turtle.onscreenclick(clickright, 2)

turtle.onkey(up, 'w')
turtle.onkey(down, 's')
turtle.onkey(right, 'd')
turtle.onkey(left, 'a')

turtle.done()