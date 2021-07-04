import turtle
from turtle import Turtle, Screen

screen = Screen()

turd = Turtle('turtle')
turd.speed(-1)

def dragging(x, y):
    turd.ondrag(None)
    turd.setheading(turd.towards(x, y))
    turd.goto(x, y)
    turd.ondrag(dragging)

def clickright(x, y):
    turd.clear()

def middleclick(x, y):
    print(turd.position())

def main():
    turtle.listen()
    turd.ondrag(dragging)
    turtle.onscreenclick(clickright, 2)
    turtle.onscreenclick(middleclick, 3)
    screen.mainloop()

main()

