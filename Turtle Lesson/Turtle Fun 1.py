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



def spiral(turtleObject):
    for i in range(0, 1000, 10):
        turtleObject.color("red")
        turtleObject.forward(i + 100)
        turtleObject.left(90)


def ss2(tess):
    tess.color("blue")

    # tess.penup()
    size = 20
    for i in range(300):
        tess.stamp()  # Leave an impression on the canvas
        size += 1  # Increase the size on every iteration
        tess.forward(size)  # Move tess along
        tess.right(i ** 2)


def ss(turtleObject):
    turtleObject.color("blue")

    turtleObject.penup()
    size = 20
    for i in range(300):
        turtleObject.stamp()
        size += 1
        turtleObject.forward(size)
        turtleObject.right(50)


spiral()

