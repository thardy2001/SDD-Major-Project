from gameFunctions import *
from pieceRules import *
from check import *
import random
from playerMove import *

#BEGIN takeAITURN(board)
def takeAITurn(board): # --> performs the AI's move
    #check the board for all black piece coordinates
    startingPositions = generateStartingCoordinates(board)
    #generate a list of all legal moves black can make
    moves_list = generateMoveList(board, startingPositions)
    #Perform a random move in the list of legal moves
    performMove(moves_list[random.randint(0, len(moves_list)) - 1], board)




#BEGIN generateStartingCoordinates(board)
def generateStartingCoordinates(board): # --> Returns a list of all coordinates containing black pieces
    coordinate_list = []
    #FOR every file on the board
    for file in range(8):
        #FOR every rank on the board
        for rank in range(8):
            # IF the square has a black piece THEN
            coordinate = changeDigitToRank(rank) + str(file)
            if squareContent(coordinate, board) == "B":
                #add the coordinate to a list
                coordinate_list.append(coordinate)
    #return the list of starting coordinates
    return coordinate_list




# BEGIN generateMoveList(board, starting coordinates )
def generateMoveList(board, startingCoordinates): # --> Returns a list of all legal moves that black can make.
    legal_moves = []
    #For every black piece on the board
    for coordinates in range(len(startingCoordinates)):
        #For every square on the board
        for file in range(8):
            for rank in range(8):
                #ending coordinate == current coordinate being tested
                end_coordinate = changeDigitToRank(rank) + str(file)
                #generate a move by combining the starting cordinate and endiong coordinate
                tested_move = startingCoordinates[coordinates] + "x" + end_coordinate
                #IF piece in starting coordinate can legally move there THEN

                if checkMove(board, tested_move):
                    # add move to list of legal moves
                    legal_moves.append(tested_move)
    #Return the list of legal moves
    return legal_moves

#BEGIN checkMove(board, move to be tested)
def checkMove(board, move): # --> Tests the AI moves to find out if the are legal, returns true or false
    #get the starting coordinate, starting rank, starting file, ending coordinate, ending rank, ending file
    move = move.split("x")
    starting_coordinate = move[0]
    starting_rank = starting_coordinate[:1]
    starting_file = starting_coordinate[1:]
    ending_coordinate = move[1]
    ending_rank = ending_coordinate[:1]
    ending_file = ending_coordinate[1:]
    move_legal = False
    #Get peice that is being moved
    piece = board[int(starting_file)][changeRankToDigit(starting_rank)]
    piece_type = piece[1:]
    #IF piece is a pawn THEN
    if piece_type == "P":
        #return if move is legal as a black pawn
        move_legal = blackPawnMovement(starting_coordinate, ending_coordinate, board)
    #ELSE IF peice is a rook THEN
    elif piece_type == "R":
        #return if move is legal as a rook
        move_legal = rookMovement(starting_coordinate, ending_coordinate, "B", board)
    #ELSE IF piece is a knight THEN
    elif piece_type == "N":
        #return if move is legal as a knight
        move_legal = knightMovement(starting_coordinate, ending_coordinate, "B",board)
    #ELSE IF piece is a bishop THEN
    elif piece_type == "B":
        #return if move is legal as a bishop
        move_legal = bishopMovement(starting_coordinate, ending_coordinate,"B", board)
    #ELSE IF piece is a queen THEN
    elif piece_type == "Q":
        #return if move is legal as a queen
        move_legal = queenMovement(starting_coordinate, ending_coordinate,"B", board)
    #ELSE IF piece is a king THEN
    elif piece_type == "K":
        #return if move is legal as a king
        move_legal = kingMovement(starting_coordinate, ending_coordinate,"B", board)
    #ELSE
    else:
        #return False
        move_legal = False

    if move_legal == True:
        if isCheck(board) == "B":
            tested_move = move[0] + "x" + move[1]
            performMove(tested_move, board)
            if isCheck(board) == "B":
                move_legal = False
                performMove(move[1] + "x" + move[0])
    return move_legal
