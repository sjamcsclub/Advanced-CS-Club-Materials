from tkinter import *
import turtle




def checkCollison():
    print(s.find_closest(turtle1.xcor(),turtle1.ycor()))

def keydownHandler(event):
    print(event.char)
    if event.char.lower() == "w":
        turtle1.forward(20)
    elif event.char.lower() == "a":
        turtle1.right(-90)
    elif event.char.lower() == "d":
        turtle1.left(-90)
    elif event.char.lower() == "s":
        turtle1.back(20)
    checkCollison()


root = Tk()
# root.withdraw()

frame = Frame(bg='black')
Label(frame, text='Hello', bg='grey', fg='white').pack(fill='x')
s = Canvas(frame, width=750, height=750)
s.pack()
frame.pack(fill='both', expand=True)
turtle1 = turtle.RawTurtle(s)

box = s.create_rectangle(1, 1, 500, 300, fill="red")



root.bind("<Key>", keydownHandler)
# root.deiconify()

root.mainloop()
