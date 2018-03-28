import gameFunctions
import moveRules
import random

def organiseMoveList(initial_list):
    new_list = []
    for i in range(len(initial_list)):
        for k in range(len(initial_list[i])):
            new_list.append(initial_list[i][k])
    return new_list

def AImove(board):
    #Generate a list of all legal moves
    piece_locations = getAllAILocations(board)
    print("Piece Locations:", piece_locations)
    legalMoves = findLegalMovesAI(board, piece_locations)
    print("Legal Moves:", legalMoves)
    #movesList = organiseMoveList(legalMoves)
    rand1 = random.randint(0, len(legalMoves))
    print("Moves List:",legalMoves)

    chosen_move = legalMoves[rand1]
    print("Chosen Move:",chosen_move)
    positions = chosen_move.split("x")
    start_pos = str(positions[0])
    end_pos = str(positions[1])
    print("Start Pos:", start_pos)
    print("End Pos:", end_pos)


    start_rank = start_pos[:1]
    start_column = start_pos[1:]
    #Take a random move from that list

    #perform move
    gameFunctions.performMove(start_rank, int(start_column), end_pos)
    gameFunctions.displayBoard(board)





def checkAImove(board, start_pos, start_rank, start_column, end_pos, piece):
    #What type of piece is it ? (Pawn, Knight, King, Queen, Bishop, Rook)
    piece_type = piece[1:]
    #Get the rank of the square that is being tested
    end_rank = end_pos[:1]
    #Get the column of the square that is being tested
    end_column = end_pos[1:]

    #If it is a Pawn piece
    if piece_type == "P":
        return moveRules.checkMovePawnB(start_rank,int(start_column), end_rank, int(end_column), start_pos, end_pos, board)
    #If it is a Rook piece
    elif piece_type == "R":
        return moveRules.checkMoveRook(start_rank, int(start_column), end_rank, int(end_column), "B", start_pos, end_pos, board)
    #If it is a Knight piece
    elif piece_type == "N":
        return moveRules.checkMoveKnight(start_rank, int(start_column), end_rank, int(end_column), "B", start_pos, end_pos, board)
    #If it is a Bishoppiece
    elif piece_type == "B":
        return moveRules.checkMoveBishop(start_rank, int(start_column), end_rank, int(end_column), "B", start_pos, end_pos, board)
    #If it is a Queen piece
    elif piece_type == "Q":
        return moveRules.checkMoveQueen(start_rank, int(start_column), end_rank, int(end_column), "B", start_pos, end_pos, board)
    #If it is a King piece
    elif piece_type == "K":
        return moveRules.checkMoveKing(start_rank, int(start_column), end_rank, int(end_column), "B", start_pos, end_pos, board)
    #Case where it is not any type of piece
    return False

def findLegalMovesAI(board, piece_starts):
    moves = []
    for i in range(len(piece_starts)):
        start_pos = piece_starts[i]
        start_rank = start_pos[:1]
        start_column = start_pos[1:]
        piece = board[gameFunctions.changeRankToDigit(start_rank)][int(start_column)]

        for rows in range(len(board)):
            for columns in range(len(board[rows])):
                end_pos = gameFunctions.changeDigitToRank(rows) + str(columns)
                #Test if the currently tesed piece can legally move there
                if checkAImove(board, start_pos, start_rank, str(int(start_column)), end_pos, piece):
                    #Recombine the location the piece is currently at and where it would go
                    move = start_pos + "x" + end_pos
                    #Add the move to the list of other moves found for this piece

                    moves.append(move)

    return moves


def getAllAILocations(board): # Returns the start_pos of all black pieces on the board
    #A list for all legal moves found
    startPositions = []
    # check all squares on the board for a black piece
    for rows in range(len(board)):
        for columns in range(len(board[rows])):
            if board[rows][columns][:1] == "B":

                #Generate a start_pos value from the rank and column
                start_pos = gameFunctions.changeDigitToRank(7-rows) + str(7-columns)
                startPositions.append(start_pos)



    return startPositions
