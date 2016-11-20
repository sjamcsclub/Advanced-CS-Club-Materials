from turtle import *

# Step 1 Teach Basics about Turtle
# Step 2


wn = Screen()

alex = Turtle()
alex.color("hotpink")
alex.pensize(5)



def SquareSpiral(turtleObject):
    turtleObject.hideturtle()
    for i in range(0, 1000, 10):
        turtleObject.color("red")
        turtleObject.forward(i + 100)
        turtleObject.left(90)

def spiral(turtleObject):
    turtleObject.color("blue")

    turtleObject.penup()
    size = 20
    for i in range(300):
        turtleObject.stamp()
        size += 1
        turtleObject.forward(size)
        turtleObject.right(50)