from tkinter import *

def FileOpenner():
    print("It`s Working ... ")

root = Tk()

root.title(" Menu in GUI ")
root.geometry("800x400")

# MainMenu = Menu(root)
# MainMenu.add_command(label = "File", command = FileOpenner)
# MainMenu.add_command(label = "Exit", command = quit)
# root.config(menu = MainMenu)

MainMenu = Menu(root)
m1 = Menu(MainMenu,tearoff = 0)
m1.add_command(label = "New Page", command = FileOpenner)
m1.add_command(label = "Save",command = FileOpenner)
m1.add_separator()
m1.add_command(label = "Save As",command = FileOpenner)
m1.add_command(label = "Print",command = FileOpenner)
m1.add_command(label = "Exit",command = quit)

root.config(menu = MainMenu)
MainMenu.add_cascade(label = "File",menu = m1)


em = Menu(MainMenu,tearoff = 0)
em.add_command(label = "Undo",command = FileOpenner)
em.add_command(label = "Redo",command = FileOpenner)
em.add_separator()
em.add_command(label = "Cut",command = FileOpenner)
em.add_command(label = "Copy",command = FileOpenner)
em.add_command(label = "Paste",command = FileOpenner)

root.config(menu = MainMenu)
MainMenu.add_cascade(label = "Edit",menu = em)


root.mainloop()