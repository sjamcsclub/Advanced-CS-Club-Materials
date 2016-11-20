from turtle import *

wn = Screen()
alex = Turtle()
alex.shape("turtle")
alex.speed(10000)
a = [[10, 10], [10, 50], [20, 50], [20, 10]]


def drawCoords(listCoords):
    alex.penup()
    for i in listCoords:
        alex.setposition(i[0], i[1])
        alex.pendown()
    alex.fillcolor("red")


def SquareSpiral(turtleObject):
    turtleObject.hideturtle()
    for i in range(0, 1000, 10):
        turtleObject.color("red")
        turtleObject.forward(i + 100)
        turtleObject.left(90)


def fun(turtleObject):
    turtleObject.color("blue")
    turtleObject.shapesize(0.1)
    turtleObject.penup()
    size = 0
    for i in range(3000):
        turtleObject.stamp()  # Leave an impression on the canvas
        size += 1  # Increase the size on every iteration
        turtleObject.forward(size)  # Move tess along
        turtleObject.right(45+i)


def spiral(turtleObject):
    turtleObject.color("blue")

    turtleObject.penup()
    size = 20
    for i in range(300):
        turtleObject.stamp()
        size += 1
        turtleObject.forward(size)
        turtleObject.right(50)

def star(turtleObject):
    for i in range(20):
        turtleObject.forward(i * 10)
        turtleObject.right(144)

def blackHole(turtleObject):
    turtleObject.hideturtle()
    for i in range(180):
        alex.forward(100)
        alex.right(30)
        alex.forward(20)
        alex.left(60)
        alex.forward(50)
        alex.right(30)
        
        alex.penup()
        alex.setposition(0, 0)
        alex.pendown()
        
        alex.right(2)
    
##fun(alex)
blackHole(alex)
##SquareSpira(alex)
##drawCoords(a)
