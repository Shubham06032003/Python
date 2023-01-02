from tkinter import *

def func1():
    print("hello func1")

def func2():
    print("hello func2")
def func3():
    print("hello func3")

root = Tk()
root.geometry("800x400")

frame1 = Frame(root,borderwidth = 5,bg = "yellow",relief = SUNKEN,padx = 5)
frame1.pack(anchor = "nw")

frame2 = Frame(root,borderwidth = 5,bg = "yellow",relief = SUNKEN,padx = 5)
frame2.pack(pady= 175,padx = 200)

frame3 = Frame(root,borderwidth = 5,bg = "yellow",relief = SUNKEN,padx = 5)
frame3.pack(anchor = "se")

b1 = Button(frame1,bg = "red",fg = "lime", font = "10",text = "SUBMIT" ,command = func1)
b1.pack()

b2 = Button(frame2,bg = "red",fg = "lime", font = "10",text = "SUBMIT",command = func2)
b2.pack()

b3 = Button(frame3,bg = "red",fg = "lime", font = "10",text = "SUBMIT",command = func3)
b3.pack()


root.mainloop()