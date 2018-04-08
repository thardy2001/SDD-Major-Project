from gameFunctions import *
from playerMove import *
from AI import *
from check import *



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


reset_board(board)
turn = "W"


#WHILE game is running THEN
while gameRunning:
    displayBoard(board)
    #IF it is whites turn THEN
    if turn == "W":
        #run player turn
        playerMakeMove(board)
        turn = "B"


    #ELSE THEN
    elif turn == "B":
        #run AI turn
        takeAITurn(board)
        turn = "W"
