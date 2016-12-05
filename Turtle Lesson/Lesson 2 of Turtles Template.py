from tkinter import *
import turtle





root = Tk()
# root.withdraw()

frame = Frame(bg='black')
Label(frame, text='Hello', bg='grey', fg='white').pack(fill='x')
s = Canvas(frame, width=750, height=750)
s.pack()
frame.pack(fill='both', expand=True)
turtle1 = turtle.RawTurtle(s)




root.bind("<Key>", keydownHandler)
# root.deiconify()

root.mainloop()
