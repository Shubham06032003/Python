from tkinter import *

def fun(Events):
    print("Event is running ")

root = Tk()

root.title("Events in GUI")

root.geometry("800x400")

Widget = Button(root,text = "Click Here",fg = "red",font = "15")
Widget.pack(pady = 175)

Widget.bind('<Button-1>',fun)
Widget.bind('<Double-1>',quit)


root.mainloop()