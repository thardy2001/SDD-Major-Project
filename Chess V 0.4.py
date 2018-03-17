
import moveRules.py

gameRunning = True
turn = True
#Create Board Positions
#         H                          G                          F                          E                          D
board = [['','','','','','','',''], ['','','','','','','',''], ['','','','','','','',''], ['','','','','','','',''], ['','','','','','','',''],
      #   C                          B                          A
         ['','','','','','','',''], ['','','','','','','',''], ['','','','','','','','']]
RANK = {"A":board[7], "B":board[6], "C":board[5], "D":board[4], "E":board[3], "F":board[2], "G":board[1], "H":board[0]}



'''
BEGIN checkmovePawn[startpos, endpos]
	SET Legalmove to FALSE
	IF startpos(x) NOT EQUAL TO endpos(x) THEN
		IF startpos(y) NOT EQUAL TO endpos(y) THEN
			IF startpos(y) is “2” THEN
                            IF endpos(y) - startpos(y) = ‘2’ OR endpos(y) - startpos(y) = ‘1’  THEN
					IF checksquarecontent[endpos] EQUALS “empty” THEN
						SET legalmove to TRUE
					ENDIF
				ENDIF
			ENDIF
			IF endpos(y) – startpos(y) = ‘1’  THEN
				IF checksquarecontent[endpos] EQUALS “empty” THEN
					SET legalmove to TRUE
				ENDIF
			ENDIF
		ENDIF
                IF endpos(x) EQUALS startpos(x) + 1 AND endpos(y) EQUALS startpos(y) +1 OR endpos(x) EQUALS startpos(x) – 1 AND endpos(y) EQUALS startpos(y) + 1 THEN
                    IF checksquarecontent(endpos(x, y)) EQUALS “enemy” THEN
                        SET Legalmove to TRUE
                    ENDIF

		ENDIF

	ENDIF
RETURN legalmove

END checkmovePawn()

'''

'''
def checkMovePawn(start_pos, end_pos):
    move_legal = False
    if start_pos[0] != end_pos[0]:
        if start_pos[1] != end_pos[1]:
            if start_pos[1] ==
        else:
            return False
    else:
        return False

'''
def reset_board():
    #For every "Cell" on the board
    for i in range(len(board)):
        for k in range(len(board[i])):
            #Empty Cell
            board[i][k] = '  '
    #Place All Pawns
    for i in range(8):
        RANK["B"][i] = "WP"
        RANK["G"][i] = "BP"
    #Place the rest of the pieces
        #White
    RANK["A"][0] = "WR"
    RANK["A"][1] = "WN"
    RANK["A"][2] = "WB"
    RANK["A"][3] = "WQ"
    RANK["A"][4] = "WK"
    RANK["A"][5] = "WB"
    RANK["A"][6] = "WN"
    RANK["A"][7] = "WR"
        #Black
    RANK["H"][0] = "BR"
    RANK["H"][1] = "BN"
    RANK["H"][2] = "BB"
    RANK["H"][3] = "BQ"
    RANK["H"][4] = "BK"
    RANK["H"][5] = "BB"
    RANK["H"][6] = "BN"
    RANK["H"][7] = "BR"



def displayBoard():
    for i in range(len(board)):
        print(board[i])

def performMove(start_rank,start_column, end_pos):
    #Get End Position Details
    end_rank = end_pos[:1]
    end_column = end_pos[1:]

    #Make Move
    RANK[end_rank][int(end_column)-1] = RANK[start_rank][start_column]
    RANK[start_rank][start_column] = '  '


def checkMove(move):
    move_legal = False

    moves = move.split("x")
    start_pos = moves[0]
    end_pos = moves[1]

    start_pos_rank = start_pos[:1]
    start_pos_rank = start_pos_rank.upper()

    end_pos_rank = end_pos[:1]
    end_pos_rank = end_pos_rank.upper()
    end_pos_column = int(end_pos[1:] -1)

    start_pos_column = int(start_pos[1:]) - 1
    piece = RANK[start_pos_rank][start_pos_column]
    if "W" in piece:
        team = "W"
    else:
        team = "B"
    if "P" in piece:
        move_legal = moveRules.checkMovePawn(start_pos_rank, start_pos_column, end_pos_rank, end_pos_column, team)
    elif "R" in piece:
        move_legal =  moveRules.checkMoveRook(start_pos_rank, start_pos_column, end_pos_rank, end_pos_column, team)
    elif piece == "WB" or piece == "BB":
        move_legal =  moveRules.checkMoveBishop(start_pos_rank, start_pos_column, end_pos_rank, end_pos_column, team)
    elif "Q" in piece:
        move_legal =  moveRules.checkMoveQueen(start_pos_rank, start_pos_column, end_pos_rank, end_pos_column, team)
    elif "K" in piece:
        move_legal =  moveRules.checkMoveKing(start_pos_rank, start_pos_column, end_pos_rank, end_pos_column, team)
    elif "N" in piece:
        move_legal =  moveRules.checkMoveKnight(start_pos_rank, start_pos_column, end_pos_rank, end_pos_column, team)





    if "W" in piece and turn == False:
        print("It is Blacks Turn")
        move_legal = False
        makeMove()
    elif "W" not in piece and turn == True:
        print("It is Whites Turn")
        move_legal = False
        makeMove()
    if move_legal == True:
        performMove(start_pos_rank, start_pos_column, end_pos)
        print(start_pos, piece, "moves to", end_pos)
        return True
    else:
        return False



reset_board()
displayBoard()

def makeMove():
    move = input("Make Your Move:") # moves must be in the format B2xD2 that is, starting position x ending position
    if checkMove(move) == False:
        print("Illigal Move")
        makeMove()
    else:
        print("Move complete!")
        displayBoard()
        turn = False

while gameRunning == True:
    makeMove()
