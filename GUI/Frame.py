from tkinter import *

root = Tk()
root.geometry("800x400")
root.title("GUI")

f = Frame(root,bg = "brown",borderwidth = "3",relief = SUNKEN)
f.pack(side = LEFT,fill = "y")

f2 = Frame(root,bg = "brown",borderwidth = "5",relief = SUNKEN)
f2.pack(side = TOP,fill = "x")

l = Label(f,text="Project in Python with GUI",fg = "red",font = "10")
l.pack(anchor = "w",side = LEFT)

l = Label(f2,text = "Welcome to subline text",fg = "red",font = "10")
l.pack()

root.mainloop()