from tkinter import *
from turtle import *
coords = [[33, 0],[-33,0]]

root = Tk()
f = Frame(root)
f.grid()


def addCoords(event):
    
    x = event.x/2-500
    y = -event.y/2
    coords.append([x,y])
    print(coords)


def setPath():
    coords = []
    screen.bind("<Button-1>", addCoords)


def stopPath():
    screen.unbind("<Button-1>")

def draw(turtle):
    turtle.penup()
    print(turtle1.xcor())
    for i in coords:
        turtle.goto(i[0], i[1])
        turtle.pendown()
    turtle.fillcolor("red")

screen = Canvas(f, height=600, width=1000)
screen.pack()
turtle1 = RawTurtle(screen)


Label(f, text="Panel of Control").pack(side=LEFT)
setPB = Button(f, text="Set turtle Path", command=setPath)
setPB.pack(side=LEFT)
finPB = Button(f, text="Finish turtle Path", command=stopPath)
finPB.pack(side=LEFT)
drawB = Button(f, text="Draw through path", command=lambda :draw(turtle1))
drawB.pack(side=LEFT)
root.mainloop()
