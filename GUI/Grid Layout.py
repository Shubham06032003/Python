from tkinter import *

def GetValue():
    print(UserValue.get())
    print(PassValue.get())

root = Tk()
 
root.geometry("800x400")
root.title("GUI")

user = Label(root,text = "User Name ")
password = Label(root,text = "Password")
user.grid()
password.grid(row = 1)

# Variable classes in tkinter
# BooleanVar , DoubleVar , IntVar , StringVar 

UserValue = StringVar()
PassValue = StringVar()

UserEntry = Entry(root,textvariable = UserValue)
PassEntry = Entry(root,textvariable = PassValue)

UserEntry.grid(row = 0,column = 2)
PassEntry.grid(row = 1,column = 2) 

Button = Button(text = "Submit" , command = GetValue).grid()


root.mainloop()