from tkinter import *
import webbrowser
MathTopics = ["Trigonometry", "Algebra", "Calculus", "Linear Algebra"]


def send():

    selected = listButton.curselection()
    webbrowser.open("https://www.google.ca/#q="+MathTopics[selected[0]])  # google search query


def insert():
    listButton.insert(END, *MathTopics)


root = Tk()
controlPanel = Frame(root)
controlPanel.pack()

listButton = Listbox(controlPanel, selectmode=SINGLE)
listButton.pack()
insert()

sendB = Button(controlPanel, text="Send", command=send)
sendB.pack()

root.mainloop()
