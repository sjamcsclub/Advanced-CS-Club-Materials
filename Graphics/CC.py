from tkinter import *
import os

dataBase = {}
dir = "database\\"
root = Tk()

for file in os.listdir(dir):
    fullPath = dir + file
    if file.endswith(".gif"):
        dataBase[fullPath] = (PhotoImage(file=fullPath))


def check(fileName):
    fileName = dir + fileName + ".gif"
    try:
        ind = dataBase[fileName]
        s.create_image(10, 10, image=ind, anchor=NW)
        s.update()
    except KeyError:
        print("Does Not Exist In Database")


def send():
    string = userIn.get()
    check(string)
    userIn.delete(0,END)


controlPanel = Frame(root)
controlPanel.grid(row=1, column=1, sticky=NW)

userIn = Entry(controlPanel)
userIn.grid(row=1, column=1)

sendB = Button(controlPanel, text="send", command=send)
sendB.grid(row=1, column=2)

output = Frame(root)
output.grid(row=2, column=1, sticky=N)

s = Canvas(output, height=100, width=100)
s.pack()

root.mainloop()
