import tkinter.messagebox
from tkinter import*
click2 = True
def play_tic_tac_toe():
    root = Tk()
    root.geometry("1350x750+0+0")
    root.title("4x4 Tic Tac Toe")
    root.configure(background = 'darkseagreen')

    Tops = Frame(root , bg = '' , pady = 2, width = 1350 ,height = 100 ,relief = RIDGE)
    Tops.grid(row = 0,column = 0)
    lblTitle = Label(Tops,font = ('Times new roman',50,'bold'),text = "4x4 TIC TAC TOE GAME",bd = 21,bg = "darkseagreen",fg ='floralwhite',justify = CENTER)
    lblTitle.grid(row = 0,column = 0)
    MainFrame = Frame(root,bg = 'beige',bd = 10,width = 1350,height = 600,relief = RIDGE)
    MainFrame.grid(row=1,column = 0)

    LeftFrame = Frame(MainFrame ,bd = 10,width = 750,height = 500,pady = 2,padx = 10,bg = 'darkseagreen',relief = RIDGE)
    LeftFrame.pack(side = LEFT)

    RightFrame = Frame(MainFrame ,bd = 10,width = 560,height = 500,padx = 10,pady = 2,bg = 'darkseagreen',relief = RIDGE)
    RightFrame.pack(side = RIGHT)

    RightFrame1 = Frame(RightFrame ,bd = 10,width = 560,height = 200,padx = 10,pady = 2,bg = 'darkseagreen',relief = RIDGE)
    RightFrame1.grid(row=0,column = 0)

    RightFrame2 = Frame(RightFrame ,bd = 10,width = 560,height = 200,padx = 10,pady = 2,bg = 'darkseagreen',relief = RIDGE)
    RightFrame2.grid(row=1,column = 0)

    PlayerX = IntVar()
    PlayerO = IntVar()
    PlayerX.set(0)
    PlayerO.set(0)

    buttons = StringVar()

    def Checker(buttons):
        global click2
        if buttons["text"]==" " and click2 == True:
            buttons["text"] ="X"
            click2 = False
            scorekeeper()
        elif buttons["text"]==" " and click2 == False:
            buttons["text"] = "O"
            click2 = True
            scorekeeper()

    def scorekeeper():
        if(button1["text"]=="X" and button2["text"]=="X" and button3["text"]=="X" and button4["text"]=="X"):
            button1.configure(background = "lightcoral")
            button2.configure(background = "lightcoral")
            button3.configure(background = "lightcoral")
            button4.configure(background = "lightcoral")
            n = float(PlayerX.get())
            score = (n+1)
            PlayerX.set(score)
            tkinter.messagebox.showinfo("Winner X","you have just won a game")
            reset()

        if(button5["text"]=="X" and button6["text"]=="X" and button7["text"]=="X" and button8["text"]=="X"):
            button5.configure(background = "lightcoral")
            button6.configure(background = "lightcoral")
            button7.configure(background = "lightcoral")
            button8.configure(background = "lightcoral")
            n = float(PlayerX.get())
            score = (n+1)
            PlayerX.set(score)
            tkinter.messagebox.showinfo("Winner X","you have just won a game")
            reset()

        if(button9["text"]=="X" and button10["text"]=="X" and button11["text"]=="X" and button12["text"]=="X"):
            button9.configure(background = "lightcoral")
            button10.configure(background = "lightcoral")
            button11.configure(background = "lightcoral")
            button12.configure(background = "lightcoral")
            n = float(PlayerX.get())
            score = (n+1)
            PlayerX.set(score)
            tkinter.messagebox.showinfo("Winner X","you have just won a game")
            reset()
            
        if(button13["text"]=="X" and button14["text"]=="X" and button15["text"]=="X" and button16["text"]=="X"):
            button13.configure(background = "lightcoral")
            button14.configure(background = "lightcoral")
            button15.configure(background = "lightcoral")
            button16.configure(background = "lightcoral")
            n = float(PlayerX.get())
            score = (n+1)
            PlayerX.set(score)
            tkinter.messagebox.showinfo("Winner X","you have just won a game")
            reset()

        if(button1["text"]=="X" and button5["text"]=="X" and button9["text"]=="X" and button13["text"]=="X"):
            button1.configure(background = "cyan")
            button5.configure(background = "cyan")
            button9.configure(background = "cyan")
            button13.configure(background = "cyan")
            n = float(PlayerX.get())
            score = (n+1)
            PlayerX.set(score)
            tkinter.messagebox.showinfo("Winner X","you have just won a game")
            reset()

        if(button2["text"]=="X" and button6["text"]=="X" and button10["text"]=="X" and button14["text"]=="X"):
            button2.configure(background = "cyan")
            button6.configure(background = "cyan")
            button10.configure(background = "cyan")
            button14.configure(background = "cyan")
            n = float(PlayerX.get())
            score = (n+1)
            PlayerX.set(score)
            tkinter.messagebox.showinfo("Winner X","you have just won a game")
            reset()

        if(button3["text"]=="X" and button7["text"]=="X" and button11["text"]=="X" and button15["text"]=="X"):
            button3.configure(background = "cyan")
            button7.configure(background = "cyan")
            button11.configure(background = "cyan")
            button15.configure(background = "cyan")
            n = float(PlayerX.get())
            score = (n+1)
            PlayerX.set(score)
            tkinter.messagebox.showinfo("Winner X","you have just won a game")
            reset()
            
        if(button4["text"]=="X" and button8["text"]=="X" and button12["text"]=="X" and button16["text"]=="X"):
            button4.configure(background = "cyan")
            button8.configure(background = "cyan")
            button12.configure(background = "cyan")
            button16.configure(background = "cyan")
            n = float(PlayerX.get())
            score = (n+1)
            PlayerX.set(score)
            tkinter.messagebox.showinfo("Winner X","you have just won a game")
            reset()

        if(button1["text"]=="X" and button6["text"]=="X" and button11["text"]=="X" and button16["text"]=="X"):
            button1.configure(background = "fuchsia")
            button6.configure(background = "fuchsia")
            button11.configure(background = "fuchsia")
            button16.configure(background = "fuchsia")
            n = float(PlayerX.get())
            score = (n+1)
            PlayerX.set(score)
            tkinter.messagebox.showinfo("Winner X","you have just won a game")
            reset()

        if(button4["text"]=="X" and button7["text"]=="X" and button10["text"]=="X" and button13["text"]=="X"):
            button4.configure(background = "fuchsia")
            button7.configure(background = "fuchsia")
            button10.configure(background = "fuchsia")
            button13.configure(background = "fuchsia")
            n = float(PlayerX.get())
            score = (n+1)
            PlayerX.set(score)
            tkinter.messagebox.showinfo("Winner X","you have just won a game")
            reset()

        if(button1["text"]=="O" and button2["text"]=="O" and button3["text"]=="O" and button4["text"]=="O"):
            button1.configure(background = "lightcoral")
            button2.configure(background = "lightcoral")
            button3.configure(background = "lightcoral")
            button4.configure(background = "lightcoral")
            n = float(PlayerO.get())
            score = (n+1)
            PlayerO.set(score)
            tkinter.messagebox.showinfo("Winner O","you have just won a game")
            reset()

        if(button5["text"]=="O" and button6["text"]=="O" and button7["text"]=="O" and button8["text"]=="O"):
            button5.configure(background = "lightcoral")
            button6.configure(background = "lightcoral")
            button7.configure(background = "lightcoral")
            button8.configure(background = "lightcoral")
            n = float(PlayerO.get())
            score = (n+1)
            PlayerO.set(score)
            tkinter.messagebox.showinfo("Winner O","you have just won a game")
            reset()

        if(button9["text"]=="O" and button10["text"]=="O" and button11["text"]=="O" and button12["text"]=="O"):
            button9.configure(background = "lightcoral")
            button10.configure(background = "lightcoral")
            button11.configure(background = "lightcoral")
            button12.configure(background = "lightcoral")
            n = float(PlayerO.get())
            score = (n+1)
            PlayerO.set(score)
            tkinter.messagebox.showinfo("Winner O","you have just won a game")
            reset()
            
        if(button13["text"]=="O" and button14["text"]=="O" and button15["text"]=="O" and button16["text"]=="O"):
            button13.configure(background = "lightcoral")
            button14.configure(background = "lightcoral")
            button15.configure(background = "lightcoral")
            button16.configure(background = "lightcoral")
            n = float(PlayerO.get())
            score = (n+1)
            PlayerO.set(score)
            tkinter.messagebox.showinfo("Winner O","you have just won a game")
            reset()

        if(button1["text"]=="O" and button5["text"]=="O" and button9["text"]=="O" and button13["text"]=="O"):
            button1.configure(background = "cyan")
            button5.configure(background = "cyan")
            button9.configure(background = "cyan")
            button13.configure(background = "cyan")
            n = float(PlayerO.get())
            score = (n+1)
            PlayerO.set(score)
            tkinter.messagebox.showinfo("Winner O","you have just won a game")
            reset()

        if(button2["text"]=="O" and button6["text"]=="O" and button10["text"]=="O" and button14["text"]=="O"):
            button2.configure(background = "cyan")
            button6.configure(background = "cyan")
            button10.configure(background = "cyan")
            button14.configure(background = "cyan")
            n = float(PlayerO.get())
            score = (n+1)
            PlayerO.set(score)
            tkinter.messagebox.showinfo("Winner O","you have just won a game")
            reset()

        if(button3["text"]=="O" and button7["text"]=="O" and button11["text"]=="O" and button15["text"]=="O"):
            button3.configure(background = "cyan")
            button7.configure(background = "cyan")
            button11.configure(background = "cyan")
            button15.configure(background = "cyan")
            n = float(PlayerO.get())
            score = (n+1)
            PlayerO.set(score)
            tkinter.messagebox.showinfo("Winner O","you have just won a game")
            reset()
            
        if(button4["text"]=="O" and button8["text"]=="O" and button12["text"]=="O" and button16["text"]=="O"):
            button4.configure(background = "cyan")
            button8.configure(background = "cyan")
            button12.configure(background = "cyan")
            button16.configure(background = "cyan")
            n = float(PlayerO.get())
            score = (n+1)
            PlayerO.set(score)
            tkinter.messagebox.showinfo("Winner O","you have just won a game")
            reset()

        if(button1["text"]=="O" and button6["text"]=="O" and button11["text"]=="O" and button16["text"]=="O"):
            button1.configure(background = "fuchsia")
            button6.configure(background = "fuchsia")
            button11.configure(background = "fuchsia")
            button16.configure(background = "fuchsia")
            n = float(PlayerO.get())
            score = (n+1)
            PlayerO.set(score)
            tkinter.messagebox.showinfo("Winner O","you have just won a game")
            reset()

        if(button4["text"]=="O" and button7["text"]=="O" and button10["text"]=="O" and button13["text"]=="O"):
            button4.configure(background = "fuchsia")
            button7.configure(background = "fuchsia")
            button10.configure(background = "fuchsia")
            button13.configure(background = "fuchsia")
            n = float(PlayerO.get())
            score = (n+1)
            PlayerO.set(score)
            tkinter.messagebox.showinfo("Winner O","you have just won a game")
            reset()


    def reset():
        button1["text"]=" "
        button2["text"]=" "
        button3["text"]=" "
        button4["text"]=" "
        button5["text"]=" "
        button6["text"]=" "
        button7["text"]=" "
        button8["text"]=" "
        button9["text"]=" "
        button10["text"]=" "
        button11["text"]=" "
        button12["text"]=" "
        button13["text"]=" "
        button14["text"]=" "
        button15["text"]=" "
        button16["text"]=" "


        button1.configure(background = "gainsboro")
        button2.configure(background = "gainsboro")
        button3.configure(background = "gainsboro")
        button4.configure(background = "gainsboro")
        button5.configure(background = "gainsboro")
        button6.configure(background = "gainsboro")
        button7.configure(background = "gainsboro")
        button8.configure(background = "gainsboro")
        button9.configure(background = "gainsboro")
        button10.configure(background = "gainsboro")
        button11.configure(background = "gainsboro")
        button12.configure(background = "gainsboro")
        button13.configure(background = "gainsboro")
        button14.configure(background = "gainsboro")
        button15.configure(background = "gainsboro")
        button16.configure(background = "gainsboro")


    def Newgame():
        reset()
        PlayerX.set(0)
        PlayerO.set(0)
        
    lblPlayerX = Label(RightFrame1,font = ('Times new roman',50,'bold'),text = "PLAYER X :",padx = 2,pady = 2,bg = "lightgoldenrodyellow")
    lblPlayerX.grid(row = 0,column = 0,sticky= W)
    txtPlayerX = Entry(RightFrame1,font = ('Times new roman',50,'bold'),bd=2,fg="black",textvariable=PlayerX,width=14,
                                        justify=LEFT).grid(row=0,column= 1)

    lblPlayerO = Label(RightFrame1,font = ('Times new roman',50,'bold'),text = "PLAYER O :",padx = 2,pady =2 ,bg = "lightgoldenrodyellow")
    lblPlayerO.grid(row = 1,column = 0,sticky = W)
    txtPlayerO = Entry(RightFrame1,font = ('Times new roman',50,'bold'),bd=2,fg="black",textvariable=PlayerO,width=14,
                                        justify=LEFT).grid(row=1,column= 1)


    btnReset = Button(RightFrame2,text = "RESET",font=('Times 26 bold'),height = 1,width = 20,command = reset)
    btnReset.grid(row= 2,column = 0,padx =3,pady=8)

    btnNewGame = Button(RightFrame2,text = "NEW GAME",font=('Times 26 bold'),height = 1,width =20,command = Newgame)
    btnNewGame.grid(row= 3,column = 0,padx=3,pady=8)


    button1 = Button(LeftFrame,text=" ",font=('Times 26 bold'),height = 3,width = 8,bg = 'gainsboro',command=lambda:Checker(button1))
    button1.grid(row= 1,column = 0,sticky = S+N+E+N)

    button2 = Button(LeftFrame,text=" ",font=('Times 26 bold'),height = 3,width = 8,bg = 'gainsboro',command=lambda:Checker(button2))
    button2.grid(row= 1,column = 1,sticky = S+N+E+N)

    button3 = Button(LeftFrame,text=" ",font=('Times 26 bold'),height = 3,width = 8,bg = 'gainsboro',command=lambda:Checker(button3))
    button3.grid(row= 1,column = 2,sticky = S+N+E+N)

    button4 = Button(LeftFrame,text=" ",font=('Times 26 bold'),height = 3,width = 8,bg = 'gainsboro',command=lambda:Checker(button4))
    button4.grid(row= 1,column = 3,sticky = S+N+E+N)

    button5 = Button(LeftFrame,text=" ",font=('Times 26 bold'),height = 3,width = 8,bg = 'gainsboro',command=lambda:Checker(button5))
    button5.grid(row= 2,column = 0,sticky = S+N+E+N)

    button6 = Button(LeftFrame,text=" ",font=('Times 26 bold'),height = 3,width = 8,bg = 'gainsboro',command=lambda:Checker(button6))
    button6.grid(row= 2,column = 1,sticky = S+N+E+N)

    button7 = Button(LeftFrame,text=" ",font=('Times 26 bold'),height = 3,width = 8,bg = 'gainsboro',command=lambda:Checker(button7))
    button7.grid(row= 2,column = 2,sticky = S+N+E+N)

    button8 = Button(LeftFrame,text=" ",font=('Times 26 bold'),height = 3,width = 8,bg = 'gainsboro',command=lambda:Checker(button8))
    button8.grid(row= 2,column = 3,sticky = S+N+E+N)

    button9 = Button(LeftFrame,text=" ",font=('Times 26 bold'),height = 3,width = 8,bg = 'gainsboro',command=lambda:Checker(button9))
    button9.grid(row= 3,column = 0,sticky = S+N+E+N)

    button10 = Button(LeftFrame,text=" ",font=('Times 26 bold'),height = 3,width = 8,bg = 'gainsboro',command=lambda:Checker(button10))
    button10.grid(row= 3,column = 1,sticky = S+N+E+N)

    button11 = Button(LeftFrame,text=" ",font=('Times 26 bold'),height = 3,width = 8,bg = 'gainsboro',command=lambda:Checker(button11))
    button11.grid(row= 3,column = 2,sticky = S+N+E+N)

    button12 = Button(LeftFrame,text=" ",font=('Times 26 bold'),height = 3,width = 8,bg = 'gainsboro',command=lambda:Checker(button12))
    button12.grid(row= 3,column = 3,sticky = S+N+E+N)

    button13 = Button(LeftFrame,text=" ",font=('Times 26 bold'),height = 3,width = 8,bg = 'gainsboro',command=lambda:Checker(button13))
    button13.grid(row= 4,column = 0,sticky = S+N+E+N)

    button14 = Button(LeftFrame,text=" ",font=('Times 26 bold'),height = 3,width = 8,bg = 'gainsboro',command=lambda:Checker(button14))
    button14.grid(row= 4,column = 1,sticky = S+N+E+N)

    button15 = Button(LeftFrame,text=" ",font=('Times 26 bold'),height = 3,width = 8,bg = 'gainsboro',command=lambda:Checker(button15))
    button15.grid(row= 4,column = 2,sticky = S+N+E+N)

    button16 = Button(LeftFrame,text=" ",font=('Times 26 bold'),height = 3,width = 8,bg = 'gainsboro',command=lambda:Checker(button16))
    button16.grid(row= 4,column = 3,sticky = S+N+E+N)

    root.mainloop()

if __name__ == "__main__":
    play_tic_tac_toe()