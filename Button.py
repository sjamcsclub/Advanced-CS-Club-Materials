from tkinter import *
from random import choice


def changeColor():
    color = choice(["green", "red", "blue", "yellow"])  # add a few more
    screen.itemconfigure(rectangle, fill=color)


root = Tk()
ColorB = Button(root, text="click me", command=changeColor, repeatdelay=400, repeatinterval=100)

ColorB.grid(row=1, column=1)
screen = Canvas(root, height=800, width=800)

screen.grid(row=1, column=2)

rectangle = screen.create_rectangle(100, 100, 600, 600, fill="pink")

root.mainloop()
