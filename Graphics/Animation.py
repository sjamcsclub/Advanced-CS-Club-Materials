from tkinter import *
from time import sleep

root = Tk()
screen = Canvas(root, height=500, width=500)
screen.grid()

numFrames = 100
width = 10
centerx, centery = 250, 250
x1, y1, x2, y2 = centerx - width, centery - width, centerx + width, centery + width
# rect = screen.create_rectangle(x1, y1, x2, y2, fill="pink")

for i in range(numFrames):
    centerx += 1
    centery += 10
    x1, y1, x2, y2 = centerx - width, centery - width, centerx + width, centery + width
    rect = screen.create_rectangle(x1, y1, x2, y2, fill="pink")
    screen.update()
    sleep(0.1)
    screen.delete(rect)
