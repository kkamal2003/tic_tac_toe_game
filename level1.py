import tkinter.messagebox
from tkinter import*
click1 = True
class play_tic_tac_toe:
    
    def __init__(self):
        
        self.root = Tk()
        self.root.geometry("1350x750+0+0")
        self.root.title("Tic Tac Toe")
        self.root.configure(background = 'darkseagreen')

        self.Tops = Frame(self.root , bg = '' , pady = 2, width = 1350 ,height = 100 ,relief = RIDGE)
        self.Tops.grid(row = 0,column = 0)
        self.lblTitle = Label(self.Tops,font = ('Times new roman',50,'bold'),text = "TIC TAC TOE GAME",bd = 21,bg = "darkseagreen",fg ='floralwhite',justify = CENTER)
        self.lblTitle.grid(row = 0,column = 0)
        self.MainFrame = Frame(self.root,bg = 'beige',bd = 10,width = 1350,height = 600,relief = RIDGE)
        self.MainFrame.grid(row=1,column = 0)

        self.LeftFrame = Frame(self.MainFrame ,bd = 10,width = 750,height = 500,pady = 2,padx = 10,bg = 'darkseagreen',relief = RIDGE)
        self.LeftFrame.pack(side = LEFT)

        self.RightFrame = Frame(self.MainFrame ,bd = 10,width = 560,height = 500,padx = 10,pady = 2,bg = 'darkseagreen',relief = RIDGE)
        self.RightFrame.pack(side = RIGHT)

        self.RightFrame1 = Frame(self.RightFrame ,bd = 10,width = 560,height = 200,padx = 10,pady = 2,bg = 'darkseagreen',relief = RIDGE)
        self.RightFrame1.grid(row=0,column = 0)

        self.RightFrame2 = Frame(self.RightFrame ,bd = 10,width = 560,height = 200,padx = 10,pady = 2,bg = 'darkseagreen',relief = RIDGE)
        self.RightFrame2.grid(row=1,column = 0)

        PlayerX = IntVar()
        PlayerO = IntVar()
        PlayerX.set(0)
        PlayerO.set(0)
        

        buttons = StringVar()

        def Checker(buttons):
            global click1
            if buttons["text"]==" " and click1 == True:
                buttons["text"] ="X"
                click1 = False
                scorekeeper()
            elif buttons["text"]==" " and click1 == False:
                buttons["text"] = "O"
                click1 = True
                scorekeeper()

        def scorekeeper():
            if(button1["text"]=="X" and button2["text"]=="X" and button3["text"]=="X"):
                button1.configure(background = "lightcoral")
                button2.configure(background = "lightcoral")
                button3.configure(background = "lightcoral")
                n = float(PlayerX.get())
                score = (n+1)
                PlayerX.set(score)
                tkinter.messagebox.showinfo("Winner X","you have just won a game")
                reset()

            if(button4["text"]=="X" and button5["text"]=="X" and button6["text"]=="X"):
                button4.configure(background = "lightcoral")
                button5.configure(background = "lightcoral")
                button6.configure(background = "lightcoral")
                n = float(PlayerX.get())
                score = (n+1)
                PlayerX.set(score)
                tkinter.messagebox.showinfo("Winner X","you have just won a game")
                reset()

            if(button7["text"]=="X" and button8["text"]=="X" and button9["text"]=="X"):
                button7.configure(background = "lightcoral")
                button8.configure(background = "lightcoral")
                button9.configure(background = "lightcoral")
                n = float(PlayerX.get())
                score = (n+1)
                PlayerX.set(score)
                tkinter.messagebox.showinfo("Winner X","you have just won a game")
                reset()

            if(button1["text"]=="X" and button4["text"]=="X" and button7["text"]=="X"):
                button1.configure(background = "cyan")
                button4.configure(background = "cyan")
                button7.configure(background = "cyan")
                n = float(PlayerX.get())
                score = (n+1)
                PlayerX.set(score)
                tkinter.messagebox.showinfo("Winner X","you have just won a game")
                reset()

            if(button2["text"]=="X" and button5["text"]=="X" and button8["text"]=="X"):
                button2.configure(background = "cyan")
                button5.configure(background = "cyan")
                button8.configure(background = "cyan")
                n = float(PlayerX.get())
                score = (n+1)
                PlayerX.set(score)
                tkinter.messagebox.showinfo("Winner X","you have just won a game")
                reset()

            if(button3["text"]=="X" and button6["text"]=="X" and button9["text"]=="X"):
                button3.configure(background = "cyan")
                button6.configure(background = "cyan")
                button9.configure(background = "cyan")
                n = float(PlayerX.get())
                score = (n+1)
                PlayerX.set(score)
                tkinter.messagebox.showinfo("Winner X","you have just won a game")
                reset()

            if(button1["text"]=="X" and button5["text"]=="X" and button9["text"]=="X"):
                button1.configure(background = "fuchsia")
                button5.configure(background = "fuchsia")
                button9.configure(background = "fuchsia")
                n = float(PlayerX.get())
                score = (n+1)
                PlayerX.set(score)
                tkinter.messagebox.showinfo("Winner X","you have just won a game")
                reset()

            if(button3["text"]=="X" and button5["text"]=="X" and button7["text"]=="X"):
                button3.configure(background = "fuchsia")
                button5.configure(background = "fuchsia")
                button7.configure(background = "fuchsia")
                n = float(PlayerX.get())
                score = (n+1)
                PlayerX.set(score)
                tkinter.messagebox.showinfo("Winner X","you have just won a game")
                reset()

            if(button1["text"]=="O" and button2["text"]=="O" and button3["text"]=="O"):
                button1.configure(background = "lightcoral")
                button2.configure(background = "lightcoral")
                button3.configure(background = "lightcoral")
                n = float(PlayerO.get())
                score = (n+1)
                PlayerO.set(score)
                tkinter.messagebox.showinfo("Winner O","you have just won a game")
                reset()

            if(button4["text"]=="O" and button5["text"]=="O" and button6["text"]=="O"):
                button4.configure(background = "lightcoral")
                button5.configure(background = "lightcoral")
                button6.configure(background = "lightcoral")
                n = float(PlayerO.get())
                score = (n+1)
                PlayerO.set(score)
                tkinter.messagebox.showinfo("Winner O","you have just won a game")
                reset()

            if(button7["text"]=="O" and button8["text"]=="O" and button9["text"]=="O"):
                button7.configure(background = "lightcoral")
                button8.configure(background = "lightcoral")
                button9.configure(background = "lightcoral")
                n = float(PlayerO.get())
                score = (n+1)
                PlayerO.set(score)
                tkinter.messagebox.showinfo("Winner O","you have just won a game")
                reset()

            if(button1["text"]=="O" and button4["text"]=="O" and button7["text"]=="O"):
                button1.configure(background = "cyan")
                button4.configure(background = "cyan")
                button7.configure(background = "cyan")
                n = float(PlayerO.get())
                score = (n+1)
                PlayerO.set(score)
                tkinter.messagebox.showinfo("Winner O","you have just won a game")
                reset()

            if(button2["text"]=="O" and button5["text"]=="O" and button8["text"]=="O"):
                button2.configure(background = "cyan")
                button5.configure(background = "cyan")
                button8.configure(background = "cyan")
                n = float(PlayerO.get())
                score = (n+1)
                PlayerO.set(score)
                tkinter.messagebox.showinfo("Winner O","you have just won a game")
                reset()

            if(button3["text"]=="O" and button6["text"]=="O" and button9["text"]=="O"):
                button3.configure(background = "cyan")
                button6.configure(background = "cyan")
                button9.configure(background = "cyan")
                n = float(PlayerO.get())
                score = (n+1)
                PlayerO.set(score)
                tkinter.messagebox.showinfo("Winner O","you have just won a game")
                reset()

            if(button1["text"]=="O" and button5["text"]=="O" and button9["text"]=="O"):
                button1.configure(background = "fuchsia")
                button5.configure(background = "fuchsia")
                button9.configure(background = "fuchsia")
                n = float(PlayerO.get())
                score = (n+1)
                PlayerO.set(score)
                tkinter.messagebox.showinfo("Winner O","you have just won a game")
                reset()

            if(button3["text"]=="O" and button5["text"]=="O" and button7["text"]=="O"):
                button3.configure(background = "fuchsia")
                button5.configure(background = "fuchsia")
                button7.configure(background = "fuchsia")
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

            
            button1.configure(background = "gainsboro")
            button2.configure(background = "gainsboro")
            button3.configure(background = "gainsboro")
            button4.configure(background = "gainsboro")
            button5.configure(background = "gainsboro")
            button6.configure(background = "gainsboro")
            button7.configure(background = "gainsboro")
            button8.configure(background = "gainsboro")
            button9.configure(background = "gainsboro")


        def Newgame():
            reset()
            PlayerX.set(0)
            PlayerO.set(0)
        
        # Define the widget variables outside of the function
        txtPlayerX = None
        txtPlayerO = None

        def create_widgets():
            global txtPlayerX, txtPlayerO
            # Create the widgets as before
            lblPlayerX = Label(self.RightFrame1, font=('Times new roman', 50, 'bold'), text="PLAYER X:", padx=2, pady=2,
                            bg="lightgoldenrodyellow")
            lblPlayerX.grid(row=0, column=0, sticky=W)
            txtPlayerX = Entry(self.RightFrame1, font=('Times new roman', 50, 'bold'), bd=2, fg="black",
                            textvariable=PlayerX, width=14, justify=LEFT)
            txtPlayerX.grid(row=0, column=1)

            lblPlayerO = Label(self.RightFrame1, font=('Times new roman', 50, 'bold'), text="PLAYER O:", padx=2, pady=2,
                            bg="lightgoldenrodyellow")
            lblPlayerO.grid(row=1, column=0, sticky=W)
            txtPlayerO = Entry(self.RightFrame1, font=('Times new roman', 50, 'bold'), bd=2, fg="black",
                            textvariable=PlayerO, width=14, justify=LEFT)
            txtPlayerO.grid(row=1, column=1)
            
            # Return the widget instances so they can be accessed from outside the function
            return txtPlayerX, txtPlayerO

        create_widgets()
        btnReset = Button(self.RightFrame2,text = "RESET",font=('Times 26 bold'),height = 1,width = 20,command = reset)
        btnReset.grid(row= 2,column = 0,padx =3,pady=8)

        btnNewGame = Button(self.RightFrame2,text = "NEW GAME",font=('Times 26 bold'),height = 1,width =20,command = Newgame)
        btnNewGame.grid(row= 3,column = 0,padx=3,pady=8)

        button1 = Button(self.LeftFrame,text=" ",font=('Times 26 bold'),height = 3,width = 8,bg = 'gainsboro',command=lambda:Checker(button1))
        button1.grid(row= 1,column = 0,sticky = S+N+E+N)

        button2 = Button(self.LeftFrame,text=" ",font=('Times 26 bold'),height = 3,width = 8,bg = 'gainsboro',command=lambda:Checker(button2))
        button2.grid(row= 1,column = 1,sticky = S+N+E+N)

        button3 = Button(self.LeftFrame,text=" ",font=('Times 26 bold'),height = 3,width = 8,bg = 'gainsboro',command=lambda:Checker(button3))
        button3.grid(row= 1,column = 2,sticky = S+N+E+N)

        button4 = Button(self.LeftFrame,text=" ",font=('Times 26 bold'),height = 3,width = 8,bg = 'gainsboro',command=lambda:Checker(button4))
        button4.grid(row= 2,column = 0,sticky = S+N+E+N)

        button5 = Button(self.LeftFrame,text=" ",font=('Times 26 bold'),height = 3,width = 8,bg = 'gainsboro',command=lambda:Checker(button5))
        button5.grid(row= 2,column = 1,sticky = S+N+E+N)

        button6 = Button(self.LeftFrame,text=" ",font=('Times 26 bold'),height = 3,width = 8,bg = 'gainsboro',command=lambda:Checker(button6))
        button6.grid(row= 2,column = 2,sticky = S+N+E+N)

        button7 = Button(self.LeftFrame,text=" ",font=('Times 26 bold'),height = 3,width = 8,bg = 'gainsboro',command=lambda:Checker(button7))
        button7.grid(row= 3,column = 0,sticky = S+N+E+N)

        button8 = Button(self.LeftFrame,text=" ",font=('Times 26 bold'),height = 3,width = 8,bg = 'gainsboro',command=lambda:Checker(button8))
        button8.grid(row= 3,column = 1,sticky = S+N+E+N)

        button9 = Button(self.LeftFrame,text=" ",font=('Times 26 bold'),height = 3,width = 8,bg = 'gainsboro',command=lambda:Checker(button9))
        button9.grid(row= 3,column = 2,sticky = S+N+E+N)

    def mainloop(self):
        """
        Infinite loop used to run the application
        """
        self.root.mainloop()

if __name__ == "__main__":
    play_tic_tac_toe().mainloop()