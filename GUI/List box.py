from tkinter import *

root = Tk()

root.title("List Box in GUI")
root.geometry("800x400")


MyList = Listbox(root,height= 2,width = 50,bd = 10).pack()

MyList2 = Listbox(root,height = 20,width = 50,bd = 10,yscrollcommand = Scrollbar.set)
MyList2.pack(pady = 10)
Button = Button(root,text = "9",pady = 10,padx = 5,font = "arial 20 bold",bd = 5,relief = RIDGE)
Button.pack()

# ScrollBar = Scrollbar(root)
# ScrollBar.pack(fill = Y, side = RIGHT)
# ScrollBar.config(command = MyList.yview)

# InList = Listbox(MyList,height = 2,width = 20)
# InList.pack()

# Button = Button(InList,text = "Click Here").pack()
root.mainloop()