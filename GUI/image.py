from tkinter import *
from PIL import Image ,ImageTk

root = Tk()

# root.geometry("800x400")
photo = PhotoImage(file = "GUI/img.png")
Image_label = Label(root,image = photo)
Image_label.pack()
 
root.mainloop()

# For jpeg Images

# root = Tk()

# # root.geometry("800x400")
# photo = ImageTk.PhotoImage(Image.open("GUI/img.jpeg"))
# Image_label = Label(root,image = photo)
# Image_label.pack()
 
# root.mainloop()