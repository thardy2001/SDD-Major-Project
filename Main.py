import moveRules



gameRunning = True
turn = True
#Create Board Positions
#         H                          G                          F                          E                          D
board = [['','','','','','','',''], ['','','','','','','',''], ['','','','','','','',''], ['','','','','','','',''], ['','','','','','','',''],
      #   C                          B                          A
         ['','','','','','','',''], ['','','','','','','',''], ['','','','','','','','']]
RANK = {"A":board[7], "B":board[6], "C":board[5], "D":board[4], "E":board[3], "F":board[2], "G":board[1], "H":board[0]}


def changeRankToDigit(rank):
    """
    Changes a specific rank into a digit, beginning at 0
    e.g.
    A => 0,
    B => 1,
    """
    conversion = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7,
    'I': 8,
    'J': 9,
    'K': 10,
    'L': 11,
    'M': 12,
    'N': 13,
    'O': 14,
    'P': 15,
    'Q':16,
    'R':17,
    'S':18,
    'T':19,
    'U':20,
    'V':21,
    'W':22,
    'X':23,
    'Y':24,
    'Z':25
    }
    digit = conversion[rank.upper()]
    return digit


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
    end_pos_column = int(end_pos[1:]) -1

    start_pos_column = int(start_pos[1:]) - 1
    piece = RANK[start_pos_rank][start_pos_column]
    if "W" in piece:
        team = "W"
    else:
        team = "B"
    if "P" in piece:
        move_legal = moveRules.checkMovePawn(start_pos_rank, start_pos_column, end_pos_rank, end_pos_column, team, start_pos, end_pos)
    elif "R" in piece:
        move_legal =  moveRules.checkMoveRook(start_pos_rank, start_pos_column, end_pos_rank, end_pos_column, team, start_pos, end_pos)
    elif piece == "WB" or piece == "BB":
        move_legal =  checkMoveBishop(start_pos_rank, start_pos_column, end_pos_rank, end_pos_column, team, start_pos, end_pos)
    elif "Q" in piece:
        move_legal =  checkMoveQueen(start_pos_rank, start_pos_column, end_pos_rank, end_pos_column, team, start_pos, end_pos)
    elif "K" in piece:
        move_legal =  checkMoveKing(start_pos_rank, start_pos_column, end_pos_rank, end_pos_column, team, start_pos, end_pos)
    elif "N" in piece:
        move_legal =  checkMoveKnight(start_pos_rank, start_pos_column, end_pos_rank, end_pos_column, team, start_pos, end_pos)





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
