from generalFunctions import *
import whiteMove
import AI


#Create Board
board = [   [['  '],['  '],['  '],['  '],['  '],['  '],['  '],['  ']],
            [['  '],['  '],['  '],['  '],['  '],['  '],['  '],['  ']],
            [['  '],['  '],['  '],['  '],['  '],['  '],['  '],['  ']],
            [['  '],['  '],['  '],['  '],['  '],['  '],['  '],['  ']],
            [['  '],['  '],['  '],['  '],['  '],['  '],['  '],['  ']],
            [['  '],['  '],['  '],['  '],['  '],['  '],['  '],['  ']],
            [['  '],['  '],['  '],['  '],['  '],['  '],['  '],['  ']],
            [['  '],['  '],['  '],['  '],['  '],['  '],['  '],['  ']]  ]


'''
 8 [  ][  ][  ][  ][  ][  ][  ][  ]
 7 [  ][  ][  ][  ][  ][  ][  ][  ]
 6 [  ][  ][  ][  ][  ][  ][  ][  ]
 5 [  ][  ][  ][  ][  ][  ][  ][  ]
 4 [  ][  ][  ][  ][  ][  ][  ][  ]
 3 [  ][  ][  ][  ][  ][  ][  ][  ]
 2 [  ][  ][  ][  ][  ][  ][  ][  ]
 1 [  ][  ][  ][  ][  ][  ][  ][  ]
    A   B   C   D   E   F   G   H
'''
gameRunning = True
turn = "W"

reset_board(board)

#WHILE game is running THEN
while gameRunning:
    displayBoard(board)
    #IF it is whites turn THEN
    if turn == "W":
        #run player turn
        whiteMove.makeMove(board)
        turn = "B"


    #ELSE THEN
    elif turn == "B":
        #run AI turn
        AI.makeMove(board)
        turn = "W"
