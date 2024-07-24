from tkinter import*
from PIL import Image,ImageTk
from random import randint

#main Window
root = Tk()
root.title("Rock Paper Scissor")
root.configure(background="#ff9001")

#picture
rock_img = ImageTk.PhotoImage(Image.open("rock_user.jpg"))
paper_img = ImageTk.PhotoImage(Image.open("paper_user.jpg"))
scissor_img = ImageTk.PhotoImage(Image.open("scissor_user.jpg"))
rock_img_comp = ImageTk.PhotoImage(Image.open("rock_comp.jpg"))
paper_img_comp = ImageTk.PhotoImage(Image.open("paper_comp.jpg"))
scissor_img_comp = ImageTk.PhotoImage(Image.open("scissor_comp.jpg"))

#insert picture
user_label = Label(root,image=scissor_img,bg="#ff9001")
comp_label = Label(root,image=scissor_img_comp,bg="#ff9001")
comp_label.grid(row=1,column=1)
user_label.grid(row=4,column=1)


#scores
playerscore = Label(root,text=0,font=100,bg="#ff9001",fg="white")
compscore = Label(root,text=0,font=100,bg="#ff9001",fg="white")
compscore.grid(row=2,column=1)
playerscore.grid(row=3,column=1)

#indicators
user_indicator = Label(root,font=50,text="USER",bg="#ff9001",fg="white")
comp_indicator = Label(root,font=50,text="COMPUTER",bg="#ff9001",fg="white")
user_indicator.grid(row=5,column=1)
comp_indicator.grid(row=0,column=1)


#messages
msg = Label(root,font=50,bg="#ff9001",fg="white")
msg.grid(row=7,column=1)

#update_msg
def updatemsg(x):
    msg["text"] = x

#update user score
def updateuserscore():
    score = int(playerscore["text"])
    score +=1
    playerscore["text"] = str(score)

def updatecompscore():
    score = int(compscore["text"])
    score +=1
    compscore["text"] = str(score)

#checkwinner
def checkwin(player,computer):
    if player == computer:
        updatemsg("It's a tie!!")
    elif player == "rock":
        if computer == "paper":
            updatemsg("You loose")
            updatecompscore()
        else:
            updatemsg("You win.")
            updateuserscore()
    elif player == "paper":
        if computer == "scissor":
            updatemsg("You loose")
            updatecompscore()
        else:
            updatemsg("You win.")
            updateuserscore()
    elif player == "scissor":
        if computer == "rock":
            updatemsg("You loose")
            updatecompscore()
        else:
            updatemsg("You win.")
            updateuserscore()
    else:
        pass


    


#update choices
choices = ("rock","paper","scissor")
def updatechoice(x):

    #for user
    if x=="rock":
       user_label.configure(image=rock_img)
    elif x=="paper":
       user_label.configure(image=paper_img)
    else:
       user_label.configure(image=scissor_img)

    #for comp
    compchoice = choices[randint(0,2)]
    if compchoice == "rock":
        comp_label.configure(image=rock_img_comp)
    elif compchoice =="paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp)
          
    checkwin(x,compchoice)       
 

#buttons
rock = Button(root,width=20,height=2,text="ROCK",bg="#a74d20",fg="white",command=lambda:updatechoice("rock")).grid(row=6,column=0)
paper = Button(root,width=20,height=2,text="PAPER",bg="#a74d20",fg="white",command=lambda:updatechoice("paper")).grid(row=6,column=1)
scissor = Button(root,width=20,height=2,text="SCISSOR",bg="#a74d20",fg="white",command=lambda:updatechoice("scissor")).grid(row=6,column=2)



root.mainloop()