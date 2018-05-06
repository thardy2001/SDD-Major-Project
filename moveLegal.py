from pieceRules import *
import generalFunctions


def checkMove(move, board): # --> tests if the players move is legal
        #get the starting coordinate, starting row, starting file, ending coordinate, ending row, ending file

        move = move.split("x")
        starting_coordinate = move[0]

        starting_row = starting_coordinate[:1]
        starting_column = starting_coordinate[1:]

        ending_coordinate = move[1]
        ending_row = ending_coordinate[:1]
        ending_column = ending_coordinate[1:]
        move = move[0] + "x" + move[1]
        #Get peice that is being moved
        piece = board[int(starting_column)][generalFunctions.changeRowToDigit(starting_row)]
        piece_team = piece[:1]
        piece_type = piece[1:]
        if piece_team == "B":
            legal = checkMoveBlack(move, board)
        elif piece_team == "W":
            legal = checkMoveWhite(move, board)

        return legal

def checkMoveWhite(move, board):

    #get the starting coordinate, starting row, starting file, ending coordinate, ending row, ending file
    move = move.split("x")
    starting_coordinate = move[0]

    starting_row = starting_coordinate[:1]
    starting_column = starting_coordinate[1:]

    ending_coordinate = move[1]
    ending_row = ending_coordinate[:1]
    ending_column = ending_coordinate[1:]

    #Get peice that is being moved
    piece = board[int(starting_column)][generalFunctions.changeRowToDigit(starting_row)]
    piece_type = piece[1:]

    #IF piece is a pawn THEN
    if piece_type == "P":
        #return if move is legal as a black pawn

        return whitePawnMovement(starting_coordinate, ending_coordinate, board)
    #ELSE IF peice is a rook THEN
    elif piece_type == "R":
        #return if move is legal as a rook
        return rookMovement(starting_coordinate, ending_coordinate, "W", board)
    #ELSE IF piece is a knight THEN
    elif piece_type == "N":
        #return if move is legal as a knight
        return knightMovement(starting_coordinate, ending_coordinate,"W",board)
    #ELSE IF piece is a bishop THEN
    elif piece_type == "B":
        #return if move is legal as a bishop
        return bishopMovement(starting_coordinate, ending_coordinate,"W", board)
    #ELSE IF piece is a queen THEN
    elif piece_type == "Q":
        #return if move is legal as a queen
        return queenMovement(starting_coordinate, ending_coordinate,"W", board)
    #ELSE IF piece is a king THEN
    elif piece_type == "K":
        #return if move is legal as a king
        return kingMovement(starting_coordinate, ending_coordinate,"W", board)
    #ELSE
    else:
        #return False
        return False

def checkMoveBlack(move, board):

    #get the starting coordinate, starting row, starting file, ending coordinate, ending row, ending file
    move = move.split("x")
    starting_coordinate = move[0]

    starting_row = starting_coordinate[:1]
    starting_column = starting_coordinate[1:]

    ending_coordinate = move[1]
    ending_row = ending_coordinate[:1]
    ending_column = ending_coordinate[1:]

    #Get peice that is being moved
    piece = board[int(starting_column)][generalFunctions.changeRowToDigit(starting_row)]
    piece_type = piece[1:]

    #IF piece is a pawn THEN
    if piece_type == "P":
        #return if move is legal as a black pawn

        return blackPawnMovement(starting_coordinate, ending_coordinate, board)
    #ELSE IF peice is a rook THEN
    elif piece_type == "R":
        #return if move is legal as a rook
        return rookMovement(starting_coordinate, ending_coordinate, "B", board)
    #ELSE IF piece is a knight THEN
    elif piece_type == "N":
        #return if move is legal as a knight
        return knightMovement(starting_coordinate, ending_coordinate,"B",board)
    #ELSE IF piece is a bishop THEN
    elif piece_type == "B":
        #return if move is legal as a bishop
        return bishopMovement(starting_coordinate, ending_coordinate,"B", board)
    #ELSE IF piece is a queen THEN
    elif piece_type == "Q":
        #return if move is legal as a queen
        return queenMovement(starting_coordinate, ending_coordinate,"B", board)
    #ELSE IF piece is a king THEN
    elif piece_type == "K":
        #return if move is legal as a king
        return kingMovement(starting_coordinate, ending_coordinate,"B", board)
    #ELSE
    else:
        #return False
        return False
