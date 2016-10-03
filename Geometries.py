from tkinter import *

root = Tk()
# Makes a Button!
# Inherits from widget class which inherits from the Geometries
# a lot of inheriting goes on
button1 = Button(root, text="I'm a Button!")
button2 = Button(root, text="I'm a Button Too!")
# Make sure to only have one of the Geometries active for both buttons| DO NOT MIX different geometries!
# Experiment with the options of each geometry
# Using this website to determine what the options can do
# _________________________________________________________#
# Pack - http://effbot.org/tkinterbook/pack.htm
# Grid - http://effbot.org/tkinterbook/grid.htm
# Place - http://effbot.org/tkinterbook/place.htm

# Try to make the buttons line up in a line

# button1.pack()
# button1.grid()
# button1.place(x=0, y=0)

# button2.pack()
# button2.grid()
# button2.place(x=0, y=0)


root.mainloop()
