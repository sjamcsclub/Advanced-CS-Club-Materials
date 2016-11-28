from tkinter import *
import turtle

ioc = False
def intelligent_orientation_control():
    pos = turtle1.heading()
    if ioc:

        if pos == 0:
            return "w", "a", "d", "s"
        elif pos == 90:
            return "w", "a", "d", "s"
        elif pos == 180:
            return "w", "a", "d", "s"
        else:
            return "w", "d", "a", "s"

    else:
        return "w", "a", "d", "s"



def keydownHandler(event):
    a = intelligent_orientation_control()
    if event.char.lower() == a[0]:
        turtle1.forward(20)
    elif event.char.lower() == a[1]:
        turtle1.right(-90)
    elif event.char.lower() == a[2]:
        turtle1.left(-90)
    elif event.char.lower() == a[3]:
        turtle1.back(20)


root = Tk()


frame = Frame(bg='black')
Label(frame, text='Hello', bg='grey', fg='white').pack(fill='x')
s = Canvas(frame, width=750, height=750)
s.pack()
frame.pack(fill='both', expand=True)
turtle1 = turtle.RawTurtle(s)

root.bind("<Key>", keydownHandler)


root.mainloop()
