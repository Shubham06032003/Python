from tkinter import *
import tkinter.messagebox as tmsg


def Message():
    tmsg.showinfo("Food Details","Thanks for your Order")

root = Tk()

root.title("Radio Button in GUI")
root.geometry("800x400")

val = IntVar()
val.set(1)

Label(text = "Which Dish do you want to order ? ",fg = "Brown",font = "Arial 15 bold").pack()
Radio = Radiobutton(root, text = "Salad",pady = 10 ,padx = 10, variable = val , value = 1).pack(anchor= "w")
Radio = Radiobutton(root, text = "Dal Roti",pady = 10 ,padx = 10, variable = val , value = 2).pack(anchor= "w")
Radio = Radiobutton(root, text = "Dal Chaval",pady = 10 ,padx = 10, variable = val , value = 3).pack(anchor= "w")
Radio = Radiobutton(root, text = "Sabji Roti",pady = 10 ,padx = 10, variable = val , value = 4).pack(anchor= "w")

Button(root, text = "Order Now", fg = "red", font = "Arial 12 italic",bd = 5,relief = "ridge",bg = "Skyblue",command = Message).pack()


root.mainloop()