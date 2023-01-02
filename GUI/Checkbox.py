from tkinter import *

def Work():
    print(" Its Work ")

root = Tk()

root.title("Panwar Travels")
root.geometry("800x400")
 
Heading = Label(root , text = "Welcome to Panwar Travels ",pady = 25,fg = "Orange",font = "comicsansms 15 bold")
Heading.grid(row = 0,column = 3)
Name = Label(root,text = "Name : ",fg = "red")
Gender = Label(root,text = "Gender : ",fg = "red")
PhoneNo = Label(root,text = "Phone Number : ",fg = "red")
From = Label(root,text = "From : ",fg = "red")
To = Label(root,text = "To : ",fg = "red")

Name.grid(row = 1,column = 2)
Gender.grid(row = 2,column = 2)
PhoneNo.grid(row = 3,column = 2)
From.grid(row = 4,column = 2)
To.grid(row = 5,column = 2)

NameValue = StringVar()
GenderValue = StringVar()
PhoneValue = StringVar()
FromValue = StringVar()
ToValue =StringVar()

NameEntry = Entry(root,textvariable = NameValue)
GenderEntry = Entry(root,textvariable = GenderValue)
PhoneEntry = Entry(root,textvariable = PhoneValue)
FromEntry = Entry(root,textvariable = FromValue)
ToEntry = Entry(root,textvariable = ToValue)

NameEntry.grid(row = 1,column = 3)
GenderEntry.grid(row = 2,column = 3)
PhoneEntry.grid(row = 3,column = 3)
FromEntry.grid(row = 4,column = 3)
ToEntry.grid(row = 5,column = 3)

Sleeper = Checkbutton(text = " Click For Book Sleeper ",fg = "blue",command = Work)
Sleeper.grid(row = 6 ,column = 3)

Submit = Button(text = "Submit",fg = "red")
Submit.grid(row = 7 , column = 3)

root.mainloop()