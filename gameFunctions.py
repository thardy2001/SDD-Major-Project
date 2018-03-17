from moveRules import *

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
    RANK[end_rank][int(end_column)-1] = RANK[start_rank][int(start_column)-1]
    RANK[start_rank][start_column] = '  '

def checkMove(move, RANK, turn):
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
        move_legal = checkMovePawn(start_pos_rank, start_pos_column, end_pos_rank, end_pos_column, team, start_pos, end_pos)
    elif "R" in piece:
        move_legal =  checkMoveRook(start_pos_rank, start_pos_column, end_pos_rank, end_pos_column, team, start_pos, end_pos)
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
        performMove(start_pos_rank, start_pos_column, end_pos, RANK)
        print(start_pos, piece, "moves to", end_pos)
        return True
    else:
        return False

def makeMove(RANK, turn):
    move = input("Make Your Move:") # moves must be in the format B2xD2 that is, starting position x ending position
    if checkMove(move, RANK, turn) == False:
        print("Illigal Move")
        makeMove()
    else:
        print("Move complete!")
        displayBoard()
        turn = False

def checkSquareContent (coordinate, board):
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