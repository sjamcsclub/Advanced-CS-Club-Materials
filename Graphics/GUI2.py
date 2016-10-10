from tkinter import *



def send():
    a = mode.get()
    string = userIn.get()
    if a == "reversed":
        string = string[::-1]

    userIn.delete(0, END)
    screen.create_text(10, 10, text=string, anchor=NW)
    screen.update()


def cleardispOut():
    dispOut.config(state="normal")
    dispOut.delete("1.0", END)
    dispOut.config(state="disabled")


root = Tk()
controlPanel = Frame(root)
controlPanel.grid(row=1, column=1, sticky=NW)

userIn = Entry(controlPanel)
userIn.grid(row=1, column=1)

sendB = Button(controlPanel, text="send", command=send)
sendB.grid(row=1, column=2)

mode = StringVar()
mode.set("reversed")
outputMode = Checkbutton(controlPanel, text="Reverse", variable=mode, onvalue="reversed", offvalue=" ")
outputMode.grid(row=1, column=3)

output = Frame(root)
output.grid(row=2, column=1, sticky=N)
screen = Canvas(output)
screen.grid(row=1, column=1, sticky=NW)


root.mainloop()
