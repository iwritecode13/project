import turtle

turd = turtle.Turtle()
turd.color('black', 'yellow')
turd.pensize(1)
turd.speed(10)

len = 100

turd.left(90)

def square(len):
    turd.begin_fill()
    for i in range(4):
        turd.forward(len)
        turd.left(90)
    turd.end_fill()
    turd.right(10)

for i in range(36):
    square(len)
    len -= 2.5

turd.hideturtle()
turtle.done()