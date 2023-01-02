from tkinter import*
import tkinter.messagebox as tmsg
from PIL import Image,ImageTk
import random

def Game(event):
    text = event.widget.cget("text")
    Charactor = ["Snake","Water","Gun"]
    Computer = random.choice(Charactor)
    if text == "Snake" :
        print(Computer)
        if Computer == "Water":
            M = tmsg.askokcancel("Result","You Win the Game.")

        elif Computer == "Gun":
            M = tmsg.askokcancel("Result","You Lose the Game.")
        else:
            M = tmsg.askokcancel("Result","Match Tie. Try Again...")
    
    if text == "Water" :
        print(Computer)
        if Computer == "Gun":
            M = tmsg.askokcancel("Result","You Win the Game.")
            if M =="ok":
                root.destroy()

        elif Computer == "Snake":
            M = tmsg.askokcancel("Result","You Lose the Game.")
        else:
            M = tmsg.askokcancel("Result","Match Tie. Try Again...")
    
    if text == "Gun" :
        print(Computer)
        if Computer == "Snake":
            M = tmsg.askokcancel("Result","You Win the Game.")
            if M =="ok":
                root.destroy()

        elif Computer == "Water":
            M = tmsg.askokcancel("Result","You Lose the Game.")
        else:
            M = tmsg.askokcancel("Result","Match Tie. Try Again...")

        
def Next(event):
    text = event.widget.cget("text")
    if text == "Play":
        FrontPage['text'] = "Chose a Charactor"
        Play['text'] = "Show Charactors"
    else:
        Snake = Button(root,text = "Snake",width = 6,fg = "lime",bg = "black",bd = 15,relief = RAISED,font = ('arial',20,'bold'))
        Snake.pack(pady = 5)
        Snake.bind("<Button-1>",Game)
        Water = Button(root,text = "Water",width = 6,fg = "lime",bg = "black",bd = 15,relief = RAISED,font = ('arial',20,'bold'))
        Water.pack(pady = 5)
        Water.bind("<Button-1>",Game)
        Gun = Button(root,text = "Gun",width = 6,fg = "lime",bg = "black",bd = 15,relief = RAISED,font = ('arial',20,'bold'))
        Gun.pack(pady = 5)
        Gun.bind("<Button-1>",Game)

root = Tk()

root.title("Snake Water Gun Game")
root.geometry("800x600")

Bg = ImageTk.PhotoImage(Image.open("D:\Python\GUI\Snake.png"))
Image = Label(root,image = Bg)
Image.place(x= 0 ,y = 0 ,relheight=1,relwidth=1)

FrontPage = Label(root, text = "Welcome\n to \n Snake Water Gun \n Game",fg = "red",bg="Black",font = ('arial',30 ,'bold','italic'))
FrontPage.pack(pady = 150)

Play = Button(root,text = "Play",fg = "lime",width = 15,bg = "black",bd = 15,relief = RAISED,font = ('arial',20,'bold'),command = lambda:Play.pack_forget())
Play.pack()
Play.bind("<Button-1>",Next)

root.mainloop()