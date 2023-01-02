# from tkinter import *

# def Click(event):
#     global val
#     text = event.widget.cget("text")
#     if text == "=":
#         if val.get().isdigit():
#             value = int(val.get())
#         else :
#             value = eval(Screen.get())
#         val.set(value)    
#         Screen.update()
        
#     elif text == "C":
#         val.set("")
#         Screen.update()
#     else:
#         val.set(val.get() + text)
#         Screen.update()

# root = Tk()

# root.title("Calculator")
# # root .geometry("300x400")
# val = StringVar()
# val.set("")

# Screen = Entry(root,textvariable=val,bg = "powder blue",width = 22,bd = 15,font = ('arial' ,15, 'bold'),justify = RIGHT)
# Screen.grid(columnspan = 20)

# B = Button(root,text = "7",font = ('arial' ,20 ,'bold'),bd = 15, relief = GROOVE,bg = "powderblue",)
# B.grid(row = 3 ,column = 0)
# B.bind("<Button-1>",Click)

# B = Button(root,text = "8",font = ('arial' ,20 ,'bold'),bd = 15, relief = GROOVE,bg = "powderblue")
# B.grid(row = 3 ,column = 1)
# B.bind("<Button-1>",Click)

# B = Button(root,text = "9",font = ('arial' ,20 ,'bold'),bd = 15, relief = GROOVE,bg = "powderblue")
# B.grid(row = 3 ,column = 2)
# B.bind("<Button-1>",Click)

# B = Button(root,text = "/",font = ('arial' ,20 ,'bold'),bd = 15, relief = GROOVE,bg = "powderblue")
# B.grid(row = 3 ,column = 3)
# B.bind("<Button-1>",Click)
# # ======================================================================================================

# B = Button(root,text = "4",font = ('arial' ,20 ,'bold'),bd = 15, relief = GROOVE,bg = "powderblue")
# B.grid(row = 4 ,column = 0)
# B.bind("<Button-1>",Click)

# B = Button(root,text = "5",font = ('arial' ,20 ,'bold'),bd = 15, relief = GROOVE,bg = "powderblue")
# B.grid(row = 4 ,column = 1)
# B.bind("<Button-1>",Click)

# B = Button(root,text = "6",font = ('arial' ,20 ,'bold'),bd = 15, relief = GROOVE,bg = "powderblue")
# B.grid(row = 4 ,column = 2)
# B.bind("<Button-1>",Click)

# B = Button(root,text = "*",font = ('arial' ,20 ,'bold'),bd = 15, relief = GROOVE,bg = "powderblue")
# B.grid(row = 4 ,column = 3)
# B.bind("<Button-1>",Click)
# # =======================================================================================================

# B = Button(root,text = "1",font = ('arial' ,20 ,'bold'),bd = 15, relief = GROOVE,bg = "powderblue")
# B.grid(row = 5 ,column = 0)
# B.bind("<Button-1>",Click)

# B = Button(root,text = "2",font = ('arial' ,20 ,'bold'),bd = 15, relief = GROOVE,bg = "powderblue")
# B.grid(row = 5 ,column = 1)
# B.bind("<Button-1>",Click)

# B = Button(root,text = "3",font = ('arial' ,20 ,'bold'),bd = 15, relief = GROOVE,bg = "powderblue")
# B.grid(row = 5 ,column = 2)
# B.bind("<Button-1>",Click)

# B = Button(root,text = "-",font = ('arial' ,20 ,'bold'),bd = 15, relief = GROOVE,bg = "powderblue")
# B.grid(row = 5 ,column = 3)
# B.bind("<Button-1>",Click)
# # =======================================================================================================

# B = Button(root,text = "C",font = ('arial' ,20 ,'bold'),bd = 15, relief = GROOVE,bg = "powderblue")
# B.grid(row = 6 ,column = 0)
# B.bind("<Button-1>",Click)

# B = Button(root,text = "0",font = ('arial' ,20 ,'bold'),bd = 15, relief = GROOVE,bg = "powderblue")
# B.grid(row = 6 ,column = 1)
# B.bind("<Button-1>",Click)

# B = Button(root,text = ".",font = ('arial' ,20 ,'bold'),bd = 15, relief = GROOVE,bg = "powderblue")
# B.grid(row = 6 ,column = 2)
# B.bind("<Button-1>",Click)

# B = Button(root,text = "+",font = ('arial' ,20 ,'bold'),bd = 15, relief = GROOVE,bg = "powderblue")
# B.grid(row = 6 ,column = 3)
# B.bind("<Button-1>",Click)
# # =======================================================================================================

# B = Button(root,text = "=",font = ('arial' ,20 ,'bold'),bd = 15, relief = GROOVE,bg = "powderblue",width = 10)
# B.grid(row = 7,columnspan = 4 )
# B.bind("<Button-1>",Click)

# root.mainloop()










# ==========================================================================================================
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ==========================================================================================================

from tkinter import *

def Click(event):
    global val
    text = event.widget.cget("text")
    if text == "=":
        if val.get().isdigit():
            value = (val.get())
        else:
            value = eval(Screen.get())
        val.set(value)
        Screen.update()
    elif text =="C":
        val.set("")
        Screen.update()
    elif text == "D":
        if val.get().isdigit():
            value2 = int(Screen.get())//10
        else:
            value2 = Screen.get()
            value2=value2[:-1]
        val.set(str(value2))
        val.__reduce__()
        Screen.update()
    else :
        val.set(val.get()+text)
        Screen.update()

root = Tk()

root.title("Calculator")

val = StringVar()
val.set("")

Screen = Entry(root, textvariable = val ,width = 18,bg = "black",fg = "White",bd = 20 ,font = ('arial',20 ,"bold"),justify = "right")
Screen.grid(columnspan = 150)

b = Button(root , text = "7", bg = "black", fg = "White" ,bd = 20 , font = ('arial',20 ,'bold'),relief = RAISED)
b.grid(row = 1 ,column = 0)
b.bind("<Button-1>",Click)

b = Button(root , text = "8", bg = "black", fg = "White" ,bd = 20 , font = ('arial',20 ,'bold'),relief = RAISED)
b.grid(row = 1 ,column = 1)
b.bind("<Button-1>",Click)


b = Button(root , text = "9", bg = "black", fg = "White" ,bd = 20 , font = ('arial',20 ,'bold'),relief = RAISED)
b.grid(row = 1 ,column = 2)
b.bind("<Button-1>",Click)


b = Button(root , text = "/", bg = "black", fg = "White" ,bd = 20 , font = ('arial',20 ,'bold'),relief = RAISED)
b.grid(row = 1 ,column = 3)
b.bind("<Button-1>",Click)



# =============================================================================================================

b = Button(root , text = "4", bg = "black", fg = "White" ,bd = 20 , font = ('arial',20 ,'bold'),relief = RAISED)
b.grid(row = 2 ,column = 0)
b.bind("<Button-1>",Click)


b = Button(root , text = "5", bg = "black", fg = "White" ,bd = 20 , font = ('arial',20 ,'bold'),relief = RAISED)
b.grid(row = 2 ,column = 1)
b.bind("<Button-1>",Click)


b = Button(root , text = "6", bg = "black", fg = "White" ,bd = 20 , font = ('arial',20 ,'bold'),relief = RAISED)
b.grid(row = 2 ,column = 2)
b.bind("<Button-1>",Click)


b = Button(root , text = "*", bg = "black", fg = "White" ,bd = 20 , font = ('arial',20 ,'bold'),relief = RAISED)
b.grid(row = 2 ,column = 3)
b.bind("<Button-1>",Click)


# =============================================================================================================

b = Button(root , text = "1", bg = "black", fg = "White" ,bd = 20 , font = ('arial',20 ,'bold'),relief = RAISED)
b.grid(row = 3 ,column = 0)
b.bind("<Button-1>",Click)


b = Button(root , text = "2", bg = "black", fg = "White" ,bd = 20 , font = ('arial',20 ,'bold'),relief = RAISED)
b.grid(row = 3 ,column = 1)
b.bind("<Button-1>",Click)


b = Button(root , text = "3", bg = "black", fg = "White" ,bd = 20 , font = ('arial',20 ,'bold'),relief = RAISED)
b.grid(row = 3 ,column = 2)
b.bind("<Button-1>",Click)


b = Button(root , text = "-", bg = "black", fg = "White" ,bd = 20 , font = ('arial',20 ,'bold'),relief = RAISED)
b.grid(row = 3 ,column = 3)
b.bind("<Button-1>",Click)


# =============================================================================================================

b = Button(root , text = "C", bg = "black", fg = "White" ,bd = 20 , font = ('arial',20 ,'bold'),relief = RAISED)
b.grid(row = 4 ,column = 0)
b.bind("<Button-1>",Click)


b = Button(root , text = "0", bg = "black", fg = "White" ,bd = 20 , font = ('arial',20 ,'bold'),relief = RAISED)
b.grid(row = 4 ,column = 1)
b.bind("<Button-1>",Click)


b = Button(root , text = ".", bg = "black", fg = "White" ,bd = 20 , font = ('arial',20 ,'bold'),relief = RAISED)
b.grid(row = 4 ,column = 2)
b.bind("<Button-1>",Click)


b = Button(root , text = "+", bg = "black", fg = "White" ,bd = 20 , font = ('arial',20 ,'bold'),relief = RAISED)
b.grid(row = 4 ,column = 3)
b.bind("<Button-1>",Click)


# =============================================================================================================

b = Button(root , text = "=", bg = "black", fg = "White" ,bd = 20 , font = ('arial',20 ,'bold'),relief = RAISED,width = 8)
b.grid(row = 5 ,columnspan = 3,sticky=W)
b.bind("<Button-1>",Click)

b = Button(root , text ="D",bg = "Black",fg = "White",bd = 20 , font = ('arial',20 ,'bold'),relief = RAISED,width = 5)

b.grid(row = 5 ,columnspan = 5,sticky=E)
b.bind("<Button-1>",Click)


root.mainloop()