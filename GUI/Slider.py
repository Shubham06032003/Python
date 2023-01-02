from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()

def get():
    tmsg.showinfo("Amount Details","Your Amount is transfered to your Account")


root.title("Slider in GUI")
root.geometry("800x400")

# MySlider = Scale(root, from_ = 0 , to = 100)
# MySlider.pack()

Label(text = " How many Dollars do you want ? ",fg = "red",font = "20").pack()
MySlider = Scale(root,from_ = 0 , to = 100 , orient = HORIZONTAL)
MySlider.set(35)
MySlider.pack()

Button(root, text = "Get Dollar",pady = 10, fg = "blue", relief= RAISED,font = "arial 10 italic",command = get).pack()

root.mainloop()