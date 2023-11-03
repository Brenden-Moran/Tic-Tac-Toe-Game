
# author: Brenden Moran
# date: 2/4/23
# file: tictac.py a Python program that implements a tic-tac-toe game
# input: user's answers to questions in the form of strings
# output: a playable tic-tac-toe game

from random import choice

class Player:
      def __init__(self, name, sign):
            self.name = name  # player's name
            self.sign = sign  # player's sign O or X
      def get_sign(self):
            return self.sign  # return an instance sign
      def get_name(self):
            return self.name  # return an instance name
      def choose(self, board):
        while 1 == 1:
          user_input = str(input(f'{self.name}, {self.sign}: Enter a cell [A-C] [1-3]')).upper()   # prompt the user to choose a cell
          if board.isempty(user_input) == False:   # If cell is not empty on the board then it will prompt the user to try again
            print("You did not choose correctly.")
          else:
            board.set(user_input, self.sign)    # If cell is empty it will make the move
            break

class AI(Player):
  def __init__(self, name, sign, board):
    super().__init__(name, sign)      # Inherites name and sign from Player class
  def choose(self, board):
    print(f'{self.name}, {self.sign}: Enter a cell [A-C] [1-3]') # Prompts AI to pick a cell
    while 1 == 1:
      possible_moves = ["A1", "B1", "C1", "A2", "B2", "C2", "A3", "B3", "C3"]
      AI_move = choice(possible_moves)          # Randomly picks a move out of the list of moves
      possible_moves.remove(AI_move)            # removes picked move from the list of moves
      if board.isempty(AI_move) == True:        # checks to make sure that the cell is empty
        print(AI_move)
        board.set(AI_move, self.sign)           # If cell is empty the move will be played
        break
      else:                                     # If cell is not empty the random move will be picked again
        pass

class MiniMax(AI):
  def choose(self, board):
        print(f"\n{self.name}, {self.sign}: Enter a cell [A-C][1-3]: ")
        cell = MiniMax.minimax(self, board, 0, True, True)              # Base case calls on minimax function
        print(cell)
        board.set(cell, self.sign)
  def minimax(self, board, depth, self_player, start):
        # check the base conditions
        if self.sign == "X":
          other_sign = "O"
          current_sign = "X"
        else:
          other_sign = "X"
          current_sign = "O"

        if board.isdone():
            # self is a winner
            if board.get_winner() == current_sign:
                return 1
                
            # is a tie
            elif board.get_winner() == "":
                return 0
                
            # self is a looser (opponent is a winner)
            else:
                return -1
                           
        min_score = 1000
        max_score = -1000
        best_move = " "
        score = 0
        if board.isempty("B2"):      # First move will always be middle of board (best position) if it is empty
          return "B2"
        possible_moves = ["A1", "B1", "C1", "A2", "B2", "C2", "A3", "B3", "C3"]
        for move in possible_moves:       # iterates through moves
          if board.isempty(move):
            if self_player:
              board.set(move, current_sign)     # begins to play out possible game
              score = MiniMax.minimax(self, board, depth-1, False, False) # Calls on itself recursively to play out the game and returns whether the self won, lost, or tie
              board.set(move, " ")    # After all recursive calls are done the board will reset to what it originally was
              
              if score > max_score:   # compare score to max score, if score is larger change the optimal move and max score
                  max_score = score
                  best_move = move
                  if start != True:     # If not start then return max score + min score
                    return max_score + min_score


            else:
              board.set(move, other_sign)
              score = MiniMax.minimax(self, board, depth-1, True, False)
              board.set(move, " ")      # After all recursive calls are done the board will reset to what it originally was
              
              if score < min_score:   # compare score to min score, if score is smaller change the optimal move and min score
                  min_score = score
                  best_move = move
                  if start != True:     # If not start then return max score + min score
                    return min_score + max_score


        if start:           # If the end of recursion then return the best move which will then be played
          return best_move
        else:
          return 0

class SmartAI(AI):
  def choose(self, board):
    print(f'{self.name}, {self.sign}: Enter a cell [A-C] [1-3]')
    moves = ["A1", "C3", "A3", "C1", "B1", "A2", "C2", "B3"]
    if self.sign == "O":
      other_sign = "X"
    else:
      other_sign = "O"
    if board.isempty("B2"):             # Always plays B2 if open because it is the best move
        board.set("B2", self.sign)
    else:
      moves = ["A1", "C3", "A3", "C1", "B1", "A2", "C2", "B3"] 
      for move in moves:            # iterates through moves
            if board.isempty(move):
              board.set(move, self.sign)        # tests what would happen on the board if the move was made
              if board.isdone():
                if board.get_winner() == self.sign:   # if the move ends the game and the winer is the SmartAI then the move will be played
                  board.set(move, self.sign)
                  break
              else:
                board.set(move, other_sign)   # Tests what would happen if the move was played by the opponent
                if board.isdone():
                  if board.get_winner() == other_sign:      # if the game is over and the winner is the opponent
                    board.set(move, self.sign)              # then the SmartAI will play that move which will block the opponent
                    break                                   # from winning
                else:
                  board.set(move, " ")                      # resets the board to original
            if move == "B3":
                    while 1 == 1:
                      corner_moves = ["A1", "C1", "A3", "C3"]     # If no moves are available to block or win 
                      AI_move = choice(corner_moves)              # then the AI will randomely choose a corner move
                      corner_moves.remove(AI_move) 
                      if board.isempty(AI_move) == True:
                        print(AI_move)
                        board.set(AI_move, self.sign)
                        break