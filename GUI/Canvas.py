from tkinter import *

root = Tk()

root.title("Canvas in GUI")
root.geometry("800x400")

CanWidget = Canvas(root,width = 800,height = 400)
CanWidget.pack()

CanWidget.create_line(0,0,800,400,fill = "red")
CanWidget.create_line(0,400,800,0,fill = "red")

CanWidget.create_rectangle(100,20,300,200)
root.mainloop()