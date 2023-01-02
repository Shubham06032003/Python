from tkinter import *

root = Tk()

root.geometry("800x400")
root.title("GUI")

# Important Label Option
# text - add the text
# bg - background
# fg - foreground
# font - sets the font
# padx - x padding
# pady - y padding
# relief - border styling - SUNKEN,RAISED,GROOVE,RIDGE

title_label = Label(text = "Hello ! I am using GUI",bg = "black",fg ="white",padx = "20",pady = "20",font = "comicsansms 15 bold")

# Important pack Option
# anchor - for diraction
# side - top,bottom,left, right
# fill
# padx
# pady

# title_label.pack(anchor = "center",side = "bottom",fill = X)
title_label.pack(pady = 175)


root.mainloop()