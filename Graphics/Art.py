from tkinter import *

root = Tk()
screen = Canvas(root, height=1000, width=1000)
screen.grid()  # choose the geometry
screen.create_line(1, 1, 100, 100, 300, 405, 1, 700, fill="green")  # make the line thicker
screen.create_rectangle(400, 500, 900, 900, fill="salmon")  # change the border color
screen.create_oval(400, 500, 900, 900)  # compare rectangle to oval what do you notice?

# Make your own picture

root.mainloop()
