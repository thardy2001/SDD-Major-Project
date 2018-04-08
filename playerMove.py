from gameFunctions import *
from pieceRules import *
from check import *


def playerMakeMove(board): # --> takes in and performs the players move
    move = input("Make Your Move:") # MUST be in the form 'starting coordinate x ending coordinate' --> example: B1xC1
    move = convertPlayerMove(move)
    if playerCheckMove(move, board):

        if isCheck(board) == "W":
            performMove(move, board)
            if isCheck(board) == "W":
                move = move.split("x")
                move = move[1] + "x" + move[0]
                performMove(move, board)
                print("illegal move, try again")
                playerMakeMove(board)


    else:
        print("illegal move, try again")
        playerMakeMove(board)

def playerCheckMove(move, board): # --> tests if the players move is legal
        #get the starting coordinate, starting rank, starting file, ending coordinate, ending rank, ending file
        move = move.split("x")
        starting_coordinate = move[0]

        starting_rank = starting_coordinate[:1]
        starting_file = starting_coordinate[1:]

        ending_coordinate = move[1]
        ending_rank = ending_coordinate[:1]
        ending_file = ending_coordinate[1:]

        #Get peice that is being moved
        piece = board[int(starting_file)][changeRankToDigit(starting_rank)]
        print("Piece:", piece)
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

def convertPlayerMove(move): # --> converts the inputed player move to a move usable by calculations. (changes the file of all coordinates by - 1)
    move = move.split("x")
    starting_coordinate = move[0]
    starting_file = str(int(starting_coordinate[1:]) - 1)
    starting_coordinate = starting_coordinate[:1] + starting_file
    ending_coordinate = move[1]
    ending_file = str(int(ending_coordinate[1:]) - 1)
    ending_coordinate = ending_coordinate[:1] + ending_file
    new_move = starting_coordinate + "x" + ending_coordinate
    return new_move
