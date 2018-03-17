from moveRules import *
from gameFunctions import *


gameRunning = True
turn = True
#Create Board Positions
#         H                          G                          F                          E                          D
board = [['','','','','','','',''], ['','','','','','','',''], ['','','','','','','',''], ['','','','','','','',''], ['','','','','','','',''],
      #   C                          B                          A
         ['','','','','','','',''], ['','','','','','','',''], ['','','','','','','','']]
RANK = {"A":board[7], "B":board[6], "C":board[5], "D":board[4], "E":board[3], "F":board[2], "G":board[1], "H":board[0]}



reset_board(board, RANK)

displayBoard(board)


while gameRunning == True:
    makeMove(RANK, turn, board)
