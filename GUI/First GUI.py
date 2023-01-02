from tkinter import *

anything_root = Tk()

# Width x Height
anything_root.geometry("800x400")

# Width , Height
anything_root.minsize(400,200)

# Width , Height
anything_root.maxsize(1500,950)

Label_name = Label(text = "Welcome to the GUI")
Label_name.pack()

anything_root.mainloop()