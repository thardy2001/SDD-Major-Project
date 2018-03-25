import moveRules
import artificial_player

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
    #Print the labels for ranks and files
    for i in range(len(board)):
        print(changeDigitToRank(7- i),board[i])
    print("    1     2     3     4     5     6     7     8")

def performMove(start_rank,start_column, end_pos, RANK):
    #Get End Position Details
    end_rank = end_pos[:1]
    end_column = end_pos[1:]

    #Make Move
    RANK[end_rank.upper()][int(end_column)-1] = RANK[start_rank.upper()][int(start_column)]
    RANK[start_rank][start_column] = '  '



def checkMove(move, RANK, board, turn):
    move_legal = False

    #Seperate the given move into where the peice is and where the user wants it
    moves = move.split("x")
    start_pos = moves[0]
    end_pos = moves[1]

    #Break down the known start position of the piece into its rank and column position values
    start_pos_rank = start_pos[:1]
    start_pos_rank = start_pos_rank.upper()

    #Break down the known target position of the piece into its rank and column position values
    end_pos_rank = end_pos[:1]
    end_pos_rank = end_pos_rank.upper()

    #Account for lists index counting starting at 0 not one as on the board
    start_pos_column = int(start_pos[1:]) - 1
    end_pos_column = int(end_pos[1:]) -1


    #Get the piece the player wants to move
    piece = RANK[start_pos_rank][start_pos_column]
    #What team is the piece?
    piece_team = checkTeam(start_pos,board)

    #If the piece is of the wrong team
    if piece_team != turn:
        print("It's not your turn!")
        return False




    #If the piece is a Pawn
    if "P" in piece:
        move_legal = moveRules.checkMovePawn(start_pos_rank, start_pos_column, end_pos_rank, end_pos_column, piece_team, start_pos, end_pos, board)
    #If the piece is a Rook
    elif "R" in piece:
        move_legal =  moveRules.checkMoveRook(start_pos_rank, start_pos_column, end_pos_rank, end_pos_column, piece_team, start_pos, end_pos, board)
    #If the piece is a Bishop
    elif "B" in piece:
        move_legal =  moveRules.checkMoveBishop(start_pos_rank, start_pos_column, end_pos_rank, end_pos_column, piece_team, start_pos, end_pos, board)
    #If the piece is a Queen
    elif "Q" in piece:
        move_legal =  moveRules.checkMoveQueen(start_pos_rank, start_pos_column, end_pos_rank, end_pos_column, piece_team, start_pos, end_pos, board)
    #If the piece is a King
    elif "K" in piece:
        move_legal =  moveRules.checkMoveKing(start_pos_rank, start_pos_column, end_pos_rank, end_pos_column, piece_team, start_pos, end_pos, board)
    #If the piece is a Knight
    elif "N" in piece:
        move_legal =  moveRules.checkMoveKnight(start_pos_rank, start_pos_column, end_pos_rank, end_pos_column, piece_team, start_pos, end_pos, board)



    #If the move tested was legal
    if move_legal == True:
        #Make the move occur
        performMove(start_pos_rank, start_pos_column, end_pos, RANK)
        #Is it check ?
        checked = testForCheck(board)
        # If it is check for the player who moved the piece then the move is Illigal
        if turn == checked:
            print("Illegal Move! That Would Be Check!")
            return False
            #Revert the move
            performMove(end_pos_rank, end_pos_column, start_pos, RANK)
        #If it isn't the above case but still check
        elif turn == "W" and checked == "B":
            print("White has Checked Black!")
        elif turn == "B" and checked == "W":
            print("Black has Checked White!")
        #Print what has moved grom where to where
        print(start_pos, piece, "moves to", end_pos)
        #Change the turn
        turn = 'B'
        return True
    else:
        return False




def makeMove(RANK, board, turn):
    #If it is blacks turn
    if turn == "B":
        #Have AI make Move
        artificial_player.AImove(board)
    #Take in a move
    move = input("Make Your Move:") # moves must be in the format B2xD2 that is, starting position x ending position
    #Test if the move is legal or not
    if checkMove(move, RANK, board, turn) == False:
        print("Illigal Move")
        #Resubmit the queiry, ask for a new move
        makeMove(RANK , board, turn)
    else:
        #Display the board after the appropriate move has been made
        displayBoard(board)


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

def testForCheck(board):
    #Test every square in the board
    for rank in range(len(board)):
        for cell in range(len(board[rank])):
            # Does the square contain the white king ?
            if board[rank][cell]  == "WK":
                WK_pos_rank = changeDigitToRank(rank)
                WK_pos_column = cell
                WK_pos = WK_pos_rank + str(WK_pos_column)
            # Does the square contain the black king ?
            elif board[rank][cell] == "BK":
                BK_pos_rank = changeDigitToRank(rank)
                BK_pos_column = cell
                BK_pos = BK_pos_rank + str(BK_pos_column)
    #Test every square on the board
    for rank in range(len(board)):
        for cell in range(len(board[rank])):

            # If there is a piece is in the square
            if board[rank][cell] != "  ":
                start_pos = changeDigitToRank(rank) + str(cell)
                #What is the piece, type and team
                piece = board[rank][cell]
                team = piece[:1]
                piece_type = piece[1:]
                # If the piece is the black team
                if team == "B":
                    #If the piece is a Pawn
                    if piece_type == "P":
                        # Test if the piece can move to the location of the opposing teams king
                        if moveRules.checkMovePawn(changeDigitToRank(rank),cell, WK_pos_rank,WK_pos_column, team, start_pos, WK_pos, board):
                            return "W"
                    #If the piece is a Bishop
                    elif piece_type == "B":
                        # Test if the piece can move to the location of the opposing teams king
                        if moveRules.checkMoveBishop(changeDigitToRank(rank),cell, WK_pos_rank,WK_pos_column, team, start_pos, WK_pos, board):
                            return "W"
                    #If the piece is a Queen
                    elif piece_type == "Q":
                        # Test if the piece can move to the location of the opposing teams king
                        if moveRules.checkMovePawn(changeDigitToRank(rank),cell, WK_pos_rank,WK_pos_column, team, start_pos, WK_pos, board):
                            return "W"
                    #If the piece is a King
                    elif piece_type == "K":
                        # Test if the piece can move to the location of the opposing teams king
                        if moveRules.checkMoveKing(changeDigitToRank(rank),cell, WK_pos_rank,WK_pos_column, team, start_pos, WK_pos, board):
                            return "W"
                    #If the piece is a Knight
                    elif piece_type == "N":
                        # Test if the piece can move to the location of the opposing teams king
                        if moveRules.checkMoveKnight(changeDigitToRank(rank),cell, WK_pos_rank,WK_pos_column, team, start_pos, WK_pos, board):
                            return "W"
                    #If the piece is a Rook
                    elif piece_type == "R":
                        # Test if the piece can move to the location of the opposing teams king
                        if moveRules.checkMoveRook(changeDigitToRank(rank),cell, WK_pos_rank,WK_pos_column, team, start_pos, WK_pos, board):
                            return "W"
                # If it is a white piece
                else:
                    #If the piece is a Pawn
                    if piece_type == "P":
                        # Test if the piece can move to the location of the opposing teams king
                        if moveRules.checkMovePawn(changeDigitToRank(rank),cell, BK_pos_rank,BK_pos_column, team, start_pos, BK_pos, board):
                            return "B"
                    #If the piece is a Bishop
                    elif piece_type == "B":
                        # Test if the piece can move to the location of the opposing teams king
                        if moveRules.checkMoveBishop(changeDigitToRank(rank),cell, BK_pos_rank,BK_pos_column, team, start_pos, BK_pos, board):
                            return "B"
                    #If the piece is a Queen
                    elif piece_type == "Q":
                        # Test if the piece can move to the location of the opposing teams king
                        if moveRules.checkMoveQueen(changeDigitToRank(rank),cell, BK_pos_rank,BK_pos_column, team, start_pos, BK_pos, board):
                            return "B"
                    #If the piece is a King
                    elif piece_type == "K":
                        # Test if the piece can move to the location of the opposing teams king
                        if moveRules.checkMoveKing(changeDigitToRank(rank),cell, BK_pos_rank,BK_pos_column, team, start_pos, BK_pos, board):
                            return "B"
                    #If the piece is a Knight
                    elif piece_type == "N":
                        # Test if the piece can move to the location of the opposing teams king
                        if moveRules.checkMoveKnight(changeDigitToRank(rank),cell, BK_pos_rank,BK_pos_column, team, start_pos, BK_pos, board):
                            return "B"
                    #If the piece is a Rook
                    elif piece_type == "R":
                        # Test if the piece can move to the location of the opposing teams king
                        if moveRules.checkMoveRook(changeDigitToRank(rank),cell, BK_pos_rank,BK_pos_column, team, start_pos, BK_pos, board):
                            return "B"




def changeDigitToRank(rank):
    conversion = {
    0 :'A',
    1 :'B',
    2 :'C',
    3 :'D',
    4 :'E',
    5 :'F',
    6 :'G',
    7 :'H',

    }
    r = conversion[rank]
    return r


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

    }
    digit = conversion[rank.upper()]
    return digit
