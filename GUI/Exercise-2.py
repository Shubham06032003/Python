from tkinter import *

def repeat(Events):
    rooter = Tk()

    rooter.geometry(f"{HeightEntry.get()}x{WidthEntry.get()}")
    rooter.title("Exercise")

    rooter.mainloop()
    

root = Tk()

root.geometry("800x400")
root.title("Exercise")

Height = Label(root, text = " Heigth : ",fg = "Brown")
Width = Label(root, text = " Width : ",fg = "Brown")
Button = Button(root,text = "Click Here",fg = "red" ,font = "5")

Height.grid(row = 0,column = 1,pady = 5,padx = 10)
Width.grid(row = 1,column = 1,pady = 5,padx = 10)
Button.grid(row = 2 ,column = 10,pady = 10)

HeightValue = StringVar()
WidthValue = StringVar()

HeightEntry = Entry(root, textvariable = HeightValue)
WidthEntry = Entry(root,textvariable = WidthValue)

HeightEntry.grid(row = 0,column = 10)
WidthEntry.grid(row = 1 ,column = 10)

Button.bind('<Button-1>',repeat)


root.mainloop()