

def reset_board(board, RANK):
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

def displayBoard(board):
    for i in range(len(board)):
        print(board[i])

def performMove(start_rank,start_column, end_pos, RANK):
    #Get End Position Details
    end_rank = end_pos[:1]
    end_column = end_pos[1:]

    #Make Move
    RANK[end_rank.upper()][int(end_column)-1] = RANK[start_rank.upper()][int(start_column)-1]
    RANK[start_rank][start_column] = '  '

def checkMove(move, RANK, turn, board):
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
    piece_team = checkTeam(start_pos,board)



    if piece_team == 'W' and turn == "B":
        print("It is Black's Turn")
        move_legal = False
        makeMove(RANK, turn, board)
    elif piece_team == 'B' and turn == 'W':
        print("It is White's Turn")
        move_legal = False
        makeMove(RANK, turn, board)
    elif piece_team == 'E':
        print('No piece in',start_pos)
    if move_legal == True:
        performMove(start_pos_rank, start_pos_column, end_pos, RANK)
        print(start_pos, piece, "moves to", end_pos)
        return True
    else:
        return False

    if "P" in piece:
        move_legal = checkMovePawn(start_pos_rank, start_pos_column, end_pos_rank, end_pos_column, team, start_pos, end_pos, board)
    elif "R" in piece:
        move_legal =  checkMoveRook(start_pos_rank, start_pos_column, end_pos_rank, end_pos_column, team, start_pos, end_pos, board)
    elif piece == "WB" or piece == "BB":
        move_legal =  checkMoveBishop(start_pos_rank, start_pos_column, end_pos_rank, end_pos_column, team, start_pos, end_pos, board)
    elif "Q" in piece:
        move_legal =  checkMoveQueen(start_pos_rank, start_pos_column, end_pos_rank, end_pos_column, team, start_pos, end_pos, board)
    elif "K" in piece:
        move_legal =  checkMoveKing(start_pos_rank, start_pos_column, end_pos_rank, end_pos_column, team, start_pos, end_pos, board)
    elif "N" in piece:
        move_legal =  checkMoveKnight(start_pos_rank, start_pos_column, end_pos_rank, end_pos_column, team, start_pos, end_pos, board)






def makeMove(RANK, turn, board):
    move = input("Make Your Move:") # moves must be in the format B2xD2 that is, starting position x ending position
    if checkMove(move, RANK, turn, board) == False:
        print("Illigal Move")
        makeMove(RANK, turn, board)
    else:
        print("Move complete!")
        displayBoard(board)
        turn = 'B'

def checkTeam (coordinate, board):
    #E- Empty
    #B - Black
    #W - White


    co1 = changeRankToDigit(coordinate[0])
    co2 = int(coordinate[1])-1
    content = board[7-co1][co2]
    colour = content[0]

    if content == '  ':
        return 'E'
    else:
        return colour



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

def checkMovePawn(start_rank, start_column, end_rank, end_column, team ,start_pos, end_pos, board):
    return True

def checkMoveRook(start_rank, start_column, end_rank, end_column, team, start_pos, end_pos, board):

    if start_pos != end_pos:
        if changeRankToDigit(start_rank) != changeRankToDigit(end_rank) and start_column == end_column:
            if checkTeam(end_pos, board) != team:
                return True
        elif changeRankToDigit(start_rank) == changeRankToDigit(end_rank) and start_column != end_column:
            if checkTeam(end_pos, board) != team:
                return True


    return False


def checkMoveKnight(start_rank, start_column, end_rank, end_column, team,start_pos, end_pos, board):
    return True

def checkMoveBishop(start_rank, start_column, end_rank, end_column, team,start_pos, end_pos, board):
    return True

def checkMoveKing(start_rank, start_column, end_rank, end_column, team,start_pos, end_pos, board):
    return True

def checkMoveQueen(start_rank, start_column, end_rank, end_column, team,start_pos, end_pos, board):
    if checkMoveRook(start_rank, start_column, end_rank, end_column, team,start_pos, end_pos, board):
        return True
    elif checkMoveBishop(start_rank, start_column, end_rank, end_column, team,start_pos, end_pos, board):
        return True
    return False
