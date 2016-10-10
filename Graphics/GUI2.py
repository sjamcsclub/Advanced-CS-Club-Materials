from tkinter import *
import webbrowser
MathTopics = ["Trigonometry", "Algebra", "Calculus", "Linear Algebra"]


def send():

    selected = listb.curselection()
    webbrowser.open("https://www.google.ca/#q="+MathTopics[selected[0]])  # google search query


def insert():
    listb.insert(END, *MathTopics)


root = Tk()
controlPanel = Frame(root)
controlPanel.pack()

listb = Listbox(controlPanel, selectmode=SINGLE)
listb.pack()
insert()

sendB = Button(controlPanel, text="send", command=send)
sendB.pack()

root.mainloop()
