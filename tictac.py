
# author: Brenden Moran
# date: 2/1/23
# file: tictac.py is a Python program that implements a tic-tac-toe game
# input: user's answers to questions in the form of strings
# output: a playable tic-tac-toe game

from board import Board
from player import Player, AI, MiniMax, SmartAI

# main program
print("Welcome to TIC-TAC-TOE Game!")
while True:
    board = Board()
    player1 = Player("Player 1", "X")
    while True:
        player_num = int(input(" Would you like to go against (1) player 2, (2) AI, (3) MiniMax AI, or (4) Smart AI?\n"))
        if player_num == 1:
            player2 = Player("Player 2", "O")
            break
        elif player_num == 2:
            player2 = AI("AI", "O", board)
            break
        elif player_num == 3:
            player2 = MiniMax("MiniMax", "O", board)
            break
        elif player_num == 4:
            player2 = SmartAI("Smart AI", "O", board)
            break
        else:
            print("Invalid Input")

    turn = True
    while True:
        board.show()
        if turn:
            player1.choose(board)
            turn = False
        else:
            player2.choose(board)
            turn = True
        if board.isdone():
            break
    board.show()
    if board.get_winner() == player1.get_sign():
        print(f"{player1.get_name()} is a winner!")
    elif board.get_winner() == player2.get_sign():
        print(f"{player2.get_name()} is a winner!")
    else:
        print("It is a tie!")
    ans = input("Would you like to play again? [Y/N]\n").upper()
    if (ans != "Y"):
        break
print("Goodbye!")