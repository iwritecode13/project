import turtle
import random

colors = ['red', 'blue', 'green', 'purple', 'yellow', 'orange', 'black']

turd1 = turtle.Turtle()
turd1.color('red', 'blue')
turd1.pensize(3)
turd1.shape('turtle')

for i in range(5):
    randcolor = random.randint(0, len(colors))
    turd1.color(colors[randcolor])
    rand1 = random.randint(-300, 300)
    rand2 = random.randint(-300, 300)
    turd1.penup()
    turd1.setpos(rand1, rand2)
    turd1.pendown()
    turd1.begin_fill()
    turd1.circle(random.randint(10, 80))
    turd1.end_fill()

turtle.done()