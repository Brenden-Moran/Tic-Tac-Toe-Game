
# author: Brenden Moran
# date: 2/4/23
# file: tictac.py a Python program that implements a tic-tac-toe game
# input: user's answers to questions in the form of strings
# output: a playable tic-tac-toe game

class Board:
      def __init__(self):
            # board is a list of cells that are represented 
            # by strings (" ", "O", and "X")
            # initially it is made of empty cells represented 
            # by " " strings
            self.sign = " "
            self.size = 3
            self.board = list(self.sign * self.size**2)
            # the winner's sign O or X
            self.winner = ""
      def get_size(self): 
            return self.size ** 2 # return the board size (an instance size)
      def get_winner(self):
            return self.winner  # return the winner's sign O or X (an instance winner)     
      def set(self, cell, sign):
          self.sign = sign
          self.cell = cell
          list_cells = ["A1", "B1", "C1", "A2", "B2", "C2", "A3", "B3", "C3"]
          for i in list_cells:
            if self.cell == i:
              self.board[list_cells.index(i)] = self.sign                              # you can use a tuple ("A1", "B1",...) to obtain indexes 
                                                             
      def isempty(self, cell):
            self.cell = cell
            possible_cells = ("A1", "B1", "C1", "A2", "B2", "C2", "A3", "B3", "C3")       # Tuple of possible moves
            if self.cell in possible_cells:                                         # Checks if the players input is a possible move
              index = possible_cells.index(self.cell)                               # assigns index as the index of the move
            else:
              return False                                                        # Returns false if move is not in possible_cells
            if self.board[index] == " ":        # if the index of the cell is empty in the board list it will return true
              return True                       # return True if the cell is empty (not marked with X or O)
            else:
              return False
      def isdone(self):
            done = False
            self.winner = ""
            sign_x = "X"
            sign_o = "O"
            if sign_x == self.board[0] and sign_x == self.board[1] and sign_x == self.board[2]:     #Checks for winning conditions of X
              done = True                                                     
              self.winner = sign_x           
            elif sign_x == self.board[3] and sign_x == self.board[4] and sign_x == self.board[5]:
              done = True                                                     
              self.winner = sign_x                                                            # Checks all winning conditions with elif statements after the move was just made in game
            elif sign_x == self.board[6] and sign_x == self.board[7] and sign_x == self.board[8]:
              done = True                                                     
              self.winner = sign_x                                                            # returns done as True and returns winner as the player's sign or nothing which means it was a tie
            elif sign_x == self.board[0] and sign_x == self.board[3] and sign_x == self.board[6]:
              done = True                                                     
              self.winner = sign_x
            elif sign_x == self.board[1] and sign_x == self.board[4] and sign_x == self.board[7]:
              done = True                                                     
              self.winner = sign_x 
            elif sign_x == self.board[2] and sign_x == self.board[5] and sign_x == self.board[8]:
              done = True                                                     
              self.winner = sign_x 
            elif sign_x == self.board[0] and sign_x == self.board[4] and sign_x == self.board[8]:
              done = True                                                     
              self.winner = sign_x 
            elif sign_x == self.board[2] and sign_x == self.board[4] and sign_x == self.board[6]:
              done = True                                                     
              self.winner = sign_x 
            
            
            elif sign_o == self.board[0] and sign_o == self.board[1] and sign_o == self.board[2]:  #Checks for winning conditions for O
              done = True                                                     
              self.winner = sign_o           
            elif sign_o == self.board[3] and sign_o == self.board[4] and sign_o == self.board[5]:
              done = True                                                     
              self.winner = sign_o                                                            # Checks all winning conditions with elif statements after the move was just made in game
            elif sign_o == self.board[6] and sign_o == self.board[7] and sign_o == self.board[8]:
              done = True                                                     
              self.winner = sign_o                                                            # returns done as True and returns winner as the player's sign or nothing which means it was a tie
            elif sign_o == self.board[0] and sign_o == self.board[3] and sign_o == self.board[6]:
              done = True                                                     
              self.winner = sign_o
            elif sign_o == self.board[1] and sign_o == self.board[4] and sign_o == self.board[7]:
              done = True                                                     
              self.winner = sign_o 
            elif sign_o == self.board[2] and sign_o == self.board[5] and sign_o == self.board[8]:
              done = True                                                     
              self.winner = sign_o 
            elif sign_o == self.board[0] and sign_o == self.board[4] and sign_o == self.board[8]:
              done = True                                                     
              self.winner = sign_o 
            elif sign_o == self.board[2] and sign_o == self.board[4] and sign_o == self.board[6]:
              done = True                                                     
              self.winner = sign_o 
            elif " " not in self.board:
                  done = True
            return done
      def show(self):
            print(f'''   A   B   C
 +---+---+---+
1| {self.board[0]} | {self.board[1]} | {self.board[2]} | 
 +---+---+---+
2| {self.board[3]} | {self.board[4]} | {self.board[5]} |
 +---+---+---+
3| {self.board[6]} | {self.board[7]} | {self.board[8]} |
 +---+---+---+''')                                                # Draws the board by calling on the list of self.board by index