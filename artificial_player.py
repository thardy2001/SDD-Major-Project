import gameFunctions
import moveRules
import random

def AImove(board):
    #Generate a list of all legal moves
    possibleMovesList = getAllAIMoves(board)

    #Take a random move from that list
    print(possibleMovesList)
    #perform move




def checkAImove(board, start_pos, start_rank, start_column, end_pos, piece):
    #What type of piece is it ? (Pawn, Knight, King, Queen, Bishop, Rook)
    type = piece[1:]
    #Get the rank of the square that is being tested
    end_rank = end_pos[:1]
    #Get the column of the square that is being tested
    end_column = end_pos[1:]

    #If it is a Pawn piece
    if type == "P":
        return moveRules.checkMovePawn(start_rank,int(start_column), end_rank, int(end_column), "B", start_pos, end_pos, board)
    #If it is a Rook piece
    elif type == "R":
        return moveRules.checkMoveRook(start_rank, int(start_column), end_rank, int(end_column), "B", start_pos, end_pos, board)
    #If it is a Knight piece
    elif type == "N":
        return moveRules.checkMoveKnight(start_rank, int(start_column), end_rank, int(end_column), "B", start_pos, end_pos, board)
    #If it is a Bishoppiece
    elif type == "B":
        return moveRules.checkMoveBishop(start_rank, int(start_column), end_rank, int(end_column), "B", start_pos, end_pos, board)
    #If it is a Queen piece
    elif type == "Q":
        return moveRules.checkMoveQueen(start_rank, int(start_column), end_rank, int(end_column), "B", start_pos, end_pos, board)
    #If it is a King piece
    elif type == "K":
        return moveRules.checkMoveKing(start_rank, int(start_column), end_rank, int(end_column), "B", start_pos, end_pos, board)
    #Case where it is not any type of piece
    return False

def findAllLegalMovesAI(board, start_pos):
    #Break the start pos value into the rank (letter) and column (number)
    start_rank = start_pos[:1]
    start_col = start_pos[1:]
    #Create a list for all legal moves found for the piece
    moves = []

    print(int(start_col))
    print(start_rank)
    #What piece is in the square
    piece = board[gameFunctions.changeRankToDigit(start_rank)][int(start_col)]
    #Check all squares on the board
    for rows in range(len(board)):
        for columns in range(len(board[rows])):
            end_pos = gameFunctions.changeDigitToRank(rows) + str(columns + 1)
            #Test if the currently tesed piece can legally move there
            if checkAImove(board, start_pos, start_rank, str(int(start_col) + 1), end_pos, piece):
                #Recombine the location the piece is currently at and where it would go
                move = start_pos + "x" + end_pos
                #Add the move to the list of other moves found for this piece
                moves.append(move)

    return moves


def getAllAIMoves(board):
    #A list for all legal moves found
    possibleMoves = []
    # check all squares on the board for a black piece
    for rows in range(len(board)):
        for columns in range(len(board[rows])):
            if board[rows][columns][:1] == "B":
                #Generate a start_pos value from the rank and column
                start_pos = gameFunctions.changeDigitToRank(rows) + str(columns)
                # Add all legal moves found for the piece to the overall legal moves list
                possibleMoves.append(findAllLegalMovesAI(board, start_pos))
    return possibleMoves
