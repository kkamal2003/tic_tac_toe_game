from tkinter import *
from tkinter import messagebox
from random import choice

class TicTacToe:

    def __init__(self):
        """
        Sets up the GUI windows and the game itself
        """
        self.mark = {1: ' O ', 2: ' X '}
        self.player = 1
        self.ai = None
        self.level = 9
        self.ai_board = [['   ' for _ in range(3)] for _ in range(3)]
        self.depth = 0
        ###############################################
        self.root = Tk()
        self.root.title("Tic-Tac-Toe")
        self.root.geometry('1350x750')
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.config(bg="darkseagreen")
        ###############################################
        Tops = Frame(self.root , bg = '' , pady = 2, width = 1350 ,height = 100 ,relief = RIDGE)
        Tops.grid(row = 0,column = 0)
        lblTitle = Label(Tops,font = ('Times new roman',50,'bold'),text = "TIC TAC TOE GAME",bd = 21,bg = "darkseagreen",fg ='floralwhite',justify = CENTER)
        lblTitle.grid(row = 0,column = 0)
        self.MainFrame = Frame(self.root,bg = 'beige',bd = 10,width = 1350,height = 600,relief = RIDGE)
        self.MainFrame.grid(row=1,column = 0)

        self.LeftFrame = Frame(self.MainFrame ,bd = 10,width = 1250,height = 600,pady = 2,padx = 10,bg = 'darkseagreen',relief = RIDGE)
        self.LeftFrame.pack(side = LEFT)

        self.RightFrame = Frame(self.MainFrame ,bd = 10,width = 950,height = 600,padx = 10,pady = 2,bg = 'darkseagreen',relief = RIDGE)
        self.RightFrame.pack(side = RIGHT)
        lblTitle = Label(self.RightFrame,font = ('Times new roman',30,'bold'),text = "SELECT AN OPTION",bd = 21,bg = "darkseagreen",fg ='floralwhite',justify = CENTER)
        lblTitle.grid(row = 0,column = 0)
        self.RightFrame2 = Frame(self.RightFrame ,bd = 10,width = 560,height = 200,padx = 10,pady = 2,bg = 'darkseagreen',relief = RIDGE)
        self.RightFrame2.grid(row=1,column = 0)
        def button(frame):
            b = Button(self.LeftFrame,text=" ",font=('Times 26 bold'),height = 3,width = 8,bg = 'gainsboro')
            return b
        self.button_level_easy = Button(self.RightFrame2, text='Easy',font=('Times 26 bold'),height = 3,width = 8,bg = 'gainsboro', command=lambda: self.game_vs_ai(1))
        self.button_level_medium = Button(self.RightFrame2, text='Medium',font=('Times 26 bold'),height = 3,width = 8,bg = 'gainsboro', command=lambda: self.game_vs_ai(5))
        self.button_level_hard = Button(self.RightFrame2, text='Hard', font=('Times 26 bold'),height = 3,width = 8,bg = 'gainsboro',command=lambda: self.game_vs_ai(9))
        self.button_level_easy.grid(row= 1,column = 0,sticky = S+N+E+N)
        self.button_level_medium.grid(row= 2,column = 0,sticky = S+N+E+N)
        self.button_level_hard.grid(row= 3,column = 0,sticky = S+N+E+N)
        ###############################################
        self.board_frame = Frame(self.root,bg = "darkseagreen")
        self.board_frame.grid(row=0, column=0, sticky='news')
        for i in range(3):
            self.board_frame.grid_columnconfigure(index=i, weight=1)
            self.board_frame.grid_rowconfigure(index=i, weight=1)
        self.board = [[], [], []]
        for i in range(3):
            for j in range(3):
                self.board[i].append(button(self.board_frame))
                self.board[i][j].config(command=lambda row=i, col=j: self.player_click(row, col))
                self.board[i][j].grid(row=i, column=j, sticky=NSEW) 
        self.label = Label(self.board_frame, text=f'Player {self.player}: {self.mark[self.player]}',
                           font = ('Times new roman',50,'bold'),bd = 21,bg = "darkseagreen",fg ='floralwhite',justify = CENTER)
        self.label.grid(row=0, column=0, columnspan=2)
        ###############################################
        self.MainFrame.tkraise()
        
   

    def mainloop(self):
        """
        Infinite loop used to run the application
        """
        self.root.mainloop()

    def player_click(self, row, col):
        """
        def player_click(self, row, col):: The function is named player_click, takes three arguments: self, row, and col.
        self.board[row][col].config(text=self.mark[self.player], state=DISABLED): This line sets the text of the button at row row and column col on the board to the current player's mark (self.mark[self.player]) and disables the button (so that it can't be clicked again).
        self.ai_board[row][col] = self.mark[self.player]: This line updates the AI's internal representation of the game board with the current player's mark at row row and column col.
        self.check_gui_board(): This line checks whether there is a winner or a tie on the GUI board and updates the label to display the result.
        self.player = 3 - self.player: This line switches the current player to the other player, which is done by subtracting the current player's number from 3.
        self.label.config(text=f'Player {self.player}: {self.mark[self.player]}'): This line updates the label at the top of the game window to display the current player's number and mark.
        if self.ai: self.ai_click(): This line checks if the AI is enabled, and if it is, it triggers the AI to make a move.
        """
        self.board[row][col].config(text=self.mark[self.player], state=DISABLED)
        self.ai_board[row][col] = self.mark[self.player]
        self.check_gui_board()
        self.player = 3 - self.player
        self.label.config(text=f'Player {self.player}: {self.mark[self.player]}')
        if self.ai:
            self.ai_click()

    def game_vs_ai(self, level):
        """
        level parameter specifies the desired level of difficulty.
        self.level is assigned the value of level.
        self.ai is assigned a random value of either 1 or 2 using the choice() function from the random module.
        self.board_frame.tkraise() brings the game board frame to the front.
        If the player is assigned the first move, self.player will be equal to 1, and if the AI is assigned the first move, self.player will be equal to 2. If the player is assigned the first move, the if condition evaluates to False, and the if block is skipped. However, if the AI is assigned the first move, the if condition evaluates to True, and self.ai_click() method is called to initiate the AI's first move.
        """
        self.level = level
        self.ai = choice([1, 2])
        self.board_frame.tkraise()
        if self.player == self.ai:
            self.ai_click()

    def ai_click(self):
        """
        Defines the function ai_click.

        Uses the best_move function to determine the best row and column for the AI to move.

        Sets the corresponding button's text to the AI's mark (X or O), and disables the button.

        Updates the ai_board with the AI's mark in the chosen row and column.

        Calls the check_gui_board function to see if there is a winner or tie.

        Switches the player turn by setting self.player to the other player (e.g., from player 1 to player 2).

        Updates the label to indicate which player's turn it is next.

        Ends the function.
        """
        row, col = self.best_move(self.ai)
        self.board[row][col].config(text=self.mark[self.player], state=DISABLED)
        self.ai_board[row][col] = self.mark[self.player]
        self.check_gui_board()
        self.player = 3 - self.player
        self.label.config(text=f'Player {self.player}: {self.mark[self.player]}')

    def best_move(self, player):
        """
        best_score = -100 if player == self.ai else 100:
        This line initializes the best_score variable with a value that is worse than any possible score. If the current player is the AI, then the best_score is initialized with -100 (a low value), else it is initialized with 100 (a high value).

        best_move = None:
        This line initializes the best_move variable to None. best_move is the variable that will hold the best move calculated by the AI.

        for i in range(3): for j in range(3)::
        This is a nested for loop that iterates through each cell in the 3x3 grid of the game.

        if self.ai_board[i][j] == ' '::
        This line checks whether a cell is empty or not. If the cell is empty, the AI will calculate the score of making a move in that cell.

        self.ai_board[i][j] = self.mark[player]:
        This line temporarily sets the player's mark (either 'X' or 'O') in the empty cell to evaluate the score.

        score = self.move_score(player):
        This line calls the move_score method to calculate the score of making a move in the current cell.

        self.ai_board[i][j] = ' ':
        This line resets the cell to empty after the score has been evaluated.

        if player == self.ai and score > best_score: best_score = score best_move = i, j:
        This block of code is executed if the current player is the AI, and the score of making a move in the current cell is better than the best_score so far. In this case, the best_score is updated, and best_move is set to the current cell.

        if player != self.ai and score < best_score: best_score = score best_move = i, j:
        This block of code is executed if the current player is not the AI, and the score of making a move in the current cell is worse than the best_score so far. In this case, the best_score is updated, and best_move is set to the current cell.

        if self.depth == 0: return best_move:
        This block of code is executed if the search has reached the highest node. In this case, the method returns the best_move calculated.

        else: self.depth -= 1 return best_score:
        If the search has not reached the highest node, the depth of the search is reduced by one, and the method returns the best_score calculated. The search continues until it reaches the highest node.
        """
        best_score = -100 if player == self.ai else 100
        best_move = None
        for i in range(3):
            for j in range(3):
                if self.ai_board[i][j] == '   ':
                    self.ai_board[i][j] = self.mark[player]
                    score = self.move_score(player)
                    print(score)
                    self.ai_board[i][j] = '   '
                    if player == self.ai and score > best_score:
                        best_score = score
                        best_move = i, j
                    if player != self.ai and score < best_score:
                        best_score = score
                        best_move = i, j
        if self.depth == 0:
            return best_move
        else:
            self.depth -= 1
            return best_score

    def move_score(self, player):
        """
        score = 10 - self.depth if player == self.ai else -10 + self.depth
        This line initializes the score to be returned. If player is the AI player, then the score starts at 10 minus the current depth of the search. Otherwise, if player is the human player, then the score starts at negative 10 plus the current depth.
        if self.ai_board[0][0] == self.ai_board[1][1] == self.ai_board[2][2] != '   ':
                    return score
        This line checks if there is a diagonal win on the board. If the ai_board has the same symbol on all three diagonal positions and that symbol is not an empty space, then return the score.
        if self.ai_board[0][2] == self.ai_board[1][1] == self.ai_board[2][0] != '   ':
                    return score
        This line checks if there is a diagonal win on the board. If the ai_board has the same symbol on all three diagonal positions and that symbol is not an empty space, then return the score.
        for i in range(3):
                    if self.ai_board[i][0] == self.ai_board[i][1] == self.ai_board[i][2] != '   ':
                        return score
                    if self.ai_board[0][i] == self.ai_board[1][i] == self.ai_board[2][i] != '   ':
                        return score
        These lines check if there is a horizontal or vertical win on the board. If the ai_board has the same symbol on all three positions of any horizontal or vertical row and that symbol is not an empty space, then return the score.
        if all([True if self.ai_board[i][j] != '   ' else False for i in range(3) for j in range(3)]):
                    return - self.depth if player == self.ai else self.depth
        This line checks if the board is full. If every position of ai_board is not an empty space, then the game is a tie, so return the negative depth if player is the AI player, or the positive depth otherwise.
        if self.depth < self.level:
                    player = 1 if player == 2 else 2
                    self.depth += 1
                    return self.best_move(player)
        If the board is not full, then the function checks if the current search depth is less than the desired depth. If so, then player is switched to the other player, self.depth is incremented, and the function recursively calls self.best_move(player) to find the best move for the other player.
        else:
                    return - self.depth if player == self.ai else self.depth
        If the current search depth is equal to the desired depth, then the function returns the same score as in the first line, but with a negative sign if player is the AI player, or the same score with a positive sign otherwise.
        """
        score = 10 - self.depth if player == self.ai else -10 + self.depth
        if self.ai_board[0][0] == self.ai_board[1][1] == self.ai_board[2][2] != '   ':
            return score
        if self.ai_board[0][2] == self.ai_board[1][1] == self.ai_board[2][0] != '   ':
            return score
        for i in range(3):
            if self.ai_board[i][0] == self.ai_board[i][1] == self.ai_board[i][2] != '   ':
                return score
            if self.ai_board[0][i] == self.ai_board[1][i] == self.ai_board[2][i] != '   ':
                return score
        if all([True if self.ai_board[i][j] != '   ' else False for i in range(3) for j in range(3)]):
            return - self.depth if player == self.ai else self.depth
        if self.depth < self.level:
            player = 1 if player == 2 else 2
            self.depth += 1
            return self.best_move(player)
        else:
            return - self.depth if player == self.ai else self.depth

    def check_gui_board(self):
        """
        Checks if there is a winner or a draw in the GUI board
        """
        if self.board[0][0]['text'] == self.board[1][1]['text'] == self.board[2][2]['text'] == self.mark[self.player]:
            self.display_winner_message()
        if self.board[0][2]['text'] == self.board[1][1]['text'] == self.board[2][0]['text'] == self.mark[self.player]:
            self.display_winner_message()
        for i in range(3):
            if self.board[i][0]['text'] == self.board[i][1]['text'] == self.board[i][2]['text'] == self.mark[self.player]:
                self.display_winner_message()
            if self.board[0][i]['text'] == self.board[1][i]['text'] == self.board[2][i]['text'] == self.mark[self.player]:
                self.display_winner_message()
        if all([True if self.board[i][j]['state'] == DISABLED else False for i in range(3) for j in range(3)]):
            self.display_draw_message()

    def reset(self):
        """
        Resets the game
        """
        for i in range(3):
            for j in range(3):
                self.board[i][j]["text"] = "   "
                self.board[i][j]["state"] = NORMAL
        self.ai_board = [['   ' for _ in range(3)] for _ in range(3)]
        self.player = 2
        self.ai = None
        self.MainFrame.tkraise()

    def display_winner_message(self):
        """
        Display a message box for a win
        """
        if self.player == self.ai:
            messagebox.showinfo(message=f"Sorry!! You lost")
        else:
            messagebox.showinfo(message=f"Congrats!! You won")
        self.reset()

    def display_draw_message(self):
        """
        Display a message box for a draw
        """
        messagebox.showinfo(message="No winners! The game ended with a draw")
        self.reset()


if __name__ == "__main__":
    TicTacToe().mainloop()