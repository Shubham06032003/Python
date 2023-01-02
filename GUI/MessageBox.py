from tkinter import *
import tkinter.messagebox as tmsg
        
def fmFunction():
    print("It`s Work")

def help():
    print("I will help you")
    tmsg.showinfo("Help","I will help you")
    

def rate():
    print("Rate Us")
    a = tmsg.askquestion("Rate Us","How was your experience ?")
    if a == "yes":
        msg = "Great , Please Rate Us on Play Store"
    tmsg.showinfo("Experience",msg)

root = Tk()

root.title(" Massage Box ")
root.geometry("800x400")

FileMenu = Menu(root)
fm = Menu(FileMenu,tearoff = 0)

fm.add_command(label = "New File",command = fmFunction)
fm.add_command(label = "Open",command = fmFunction)
fm.add_separator()
fm.add_command(label = "Save",command = fmFunction)
fm.add_command(label = "Save As",command = fmFunction)

root.config(menu = FileMenu)
FileMenu.add_cascade(label = "File",menu = fm)

em = Menu(FileMenu,tearoff = 0)

em.add_command(label = "Undo",command = fmFunction)
em.add_command(label = "Redo",command = fmFunction)
em.add_separator()
em.add_command(label = "Cut",command = fmFunction)
em.add_command(label = "Copy",command = fmFunction)
em.add_command(label = "Paste",command = fmFunction)


root.config(menu = FileMenu)
FileMenu.add_cascade(label = "Edit",menu = em)

hm = Menu(FileMenu,tearoff = 0)

hm.add_command(label = "Help",command = help)
hm.add_command(label = "Rate Us",command = rate)

root.config(menu = FileMenu)
FileMenu.add_cascade(label = "Help",menu = hm)


root.mainloop()