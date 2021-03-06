from tkinter import *
from turtle import *
coords = []

root = Tk()
f = Frame(root)
f.grid()


def addCoords(event):
    
    x = event.x
    y = event.y
    print(x, y)
    x -= 500
    if y < 300:
        y = 300-y
    elif y == 300:
        y = 0
    elif y > 300:
        y = -(y-300)
    print(coords)
    coords.append([x,y])
    print(coords)


def setPath():
    global coords
    coords = []
    screen.bind("<Button-1>", addCoords)


def stopPath():
    screen.unbind("<Button-1>")

def draw(turtle):
    turtle.penup()
    print(turtle1.xcor())
    for i in coords:
        turtle.pendown()
        turtle.goto(i[0], i[1])
        print(i[0], "as", i[1])
        
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
