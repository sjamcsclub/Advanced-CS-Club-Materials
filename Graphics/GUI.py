from tkinter import *


def send():
    a = mode.get()
    string = userIn.get()
    if a == "reversed":
        string = string[::-1]

    userIn.delete(0, END)
    dispOut.config(state="normal")
    dispOut.insert(END, string + " ")
    dispOut.config(state="disabled")


def cleardispOut():
    dispOut.config(state="normal")
    dispOut.delete("1.0", END)
    dispOut.config(state="disabled")


root = Tk()
controlPanel = Frame(root)
controlPanel.grid(row=1, column=1, sticky=NW)

userIn = Entry(controlPanel)
userIn.grid(row=1, column=1)

sendB = Button(controlPanel, text="Send", command=send)
sendB.grid(row=1, column=2)

clear = Button(controlPanel, text="Clear Output", relief="flat", command=cleardispOut)
clear.grid(row=1, column=4)

mode = StringVar()
mode.set("reversed")
outputMode = Checkbutton(controlPanel, text="Reverse", variable=mode, onvalue="reversed", offvalue=" ")
outputMode.grid(row=1, column=3)

output = Frame(root)
output.grid(row=2, column=1, sticky=N)

dispOut = Text(output, height=5, width=40, state="disabled")
dispOut.grid(row=1, column=1)

root.mainloop()
