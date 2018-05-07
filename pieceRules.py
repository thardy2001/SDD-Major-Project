from generalFunctions import *

#BEGIN blackPawnMovement(starting coordinate, ending coordinate, board state)
def blackPawnMovement(starting_coordinate, ending_coordinate, board): # --> returns true if the move is legal otherwise false
    #get starting row, ending row, starting column and ending column
    starting_row = starting_coordinate[:1]
    starting_column = int(starting_coordinate[1:])
    ending_row = ending_coordinate[:1]
    ending_column = int(ending_coordinate[1:])
    #IF ending coordinate is empty THEN
    if pieceTeam(ending_coordinate, board) == "E" and pieceTeam(starting_coordinate, board) == "B":
        #IF starting column == 6 THEN
        if starting_column == 6:
            #IF change in column == -2 AND change in row == 0 OR change in column == -1 AND change in row == 0 THEN
            if ending_column - starting_column == -2 and abs(changeRowToDigit(ending_row) - changeRowToDigit(starting_row)) == 0 or ending_column - starting_column == -1 and abs(changeRowToDigit(ending_row) - changeRowToDigit(starting_row)) == 0:
                # the move is legal
                return True
        #ELSE THEN
        else:
            #IF change in column == -1 AND change in row == 0 THEN
            if ending_column - starting_column == -1 and abs(changeRowToDigit(ending_row) - changeRowToDigit(starting_row)) == 0:
                # the move is legal
                return True
        #IF change in column == -1 AND change in row == 1 AND end coordinate has a white piece THEN
        if ending_column - starting_column == -1 and abs(changeRowToDigit(ending_row) - changeRowToDigit(starting_row)) == 1 and pieceTeam(ending_coordinate, board) == "W":
            # the move is legal
            return True
    # the move is illegal
    return False

#BEGIN whitePawnMovement(starting coordinate, ending coordinate, board state)
def whitePawnMovement(starting_coordinate, ending_coordinate, board): # --> returns true if the move is legal otherwise false
    #get starting row, ending row, starting column and ending column

    starting_row = starting_coordinate[:1]
    starting_column = int(starting_coordinate[1:])
    ending_row = ending_coordinate[:1]
    ending_column = int(ending_coordinate[1:])
    #IF ending coordinate is empty THEN
    if pieceTeam(ending_coordinate, board) == "E" and pieceTeam(starting_coordinate, board) == "W":
        #IF starting column == 1 THEN
        if starting_column == 1:
            #IF change in column == 2 AND change in row == 0 OR change in column == 1 AND change in row == 0 THEN
            if ending_column - starting_column == 2 and abs(changeRowToDigit(ending_row) - changeRowToDigit(starting_row)) == 0 or ending_column - starting_column == 1 and abs(changeRowToDigit(ending_row) - changeRowToDigit(starting_row)) == 0:
                # the move is legal
                return True
        #ELSE THEN
        else:
            #IF change in column == 1 AND change in row == 0 THEN
            if ending_column - starting_column == 1 and abs(changeRowToDigit(ending_row) - changeRowToDigit(starting_row)) == 0:
                # the move is legal
                return True
        #IF change in column == 1 AND change in row == 1 AND end coordinate has a black piece THEN
        if ending_column - starting_column == 1 and abs(changeRowToDigit(ending_row) - changeRowToDigit(starting_row)) == 1 and pieceTeam(ending_coordinate, board) == "B":
            # the move is legal
            return True
    # the move is illegal
    return False

#BEGIN rookMovement(starting coordinate, ending coordinate, turn, board state)
def rookMovement(starting_coordinate, ending_coordinate, turn, board): # --> returns true if the move is legal otherwise false
    #get starting row, ending row, starting column and ending column

    starting_row = starting_coordinate[:1]
    starting_column = int(starting_coordinate[1:])
    ending_row = ending_coordinate[:1]
    ending_column = int(ending_coordinate[1:])

    team = pieceTeam(starting_coordinate, board)
    move = starting_coordinate + 'x' + ending_coordinate



    #IF ending coordinate doesn't have a friendly piece THEN
    if pieceTeam(ending_coordinate, board) != team and pieceTeam(starting_coordinate, board) == turn:
        #IF there is a change in row but no change in column THEN
        if ending_column - starting_column == 0 and abs(changeRowToDigit(ending_row) - changeRowToDigit(starting_row)) != 0:
            #Rook is moving horizontally

            #Rook is moving left
            if changeRowToDigit(starting_row) - changeRowToDigit(ending_row) < 0:
                #IF the change in row is greater than the boundrary THEN
                if abs(changeRowToDigit(starting_row) - changeRowToDigit(ending_row)) > findRookBoundaries(move, board, "Horizontal"):
                    #Move is illigal
                    return False
                else:
                    #Move is legal
                    return True
            #Rook is moving right
            elif changeRowToDigit(starting_row) - changeRowToDigit(ending_row) > 0:
                #IF the change in row is greater than the boundrary THEN
                if changeRowToDigit(starting_row) - changeRowToDigit(ending_row) > findRookBoundaries(move, board, "Horizontal"):
                    #Move is illigal
                    return False
                else:
                    #Move is legal
                    return True



        elif ending_column - starting_column != 0 and abs(changeRowToDigit(ending_row) - changeRowToDigit(starting_row)) == 0:
            #Rook is moving vertically

            #IF rook is moving up THEN
            if starting_column - ending_column < 0:
                #IF the change in column
                if abs(starting_column - ending_column) > findRookBoundaries(move, board, "Vertical"):
                    return False
                else:
                    return True
            #IF the rook is moving down THEN
            elif starting_column - ending_column > 0:

                if starting_column - ending_column > findRookBoundaries(move, board, "Vertical"):
                    return False
                else:
                    return True
            # the move is legal

    # the move is illegal
    return False


#BEGIN knightMovement(starting coordinate, ending coordinate, turn, board state)
def knightMovement(starting_coordinate, ending_coordinate, turn, board): # --> returns true if the move is legal otherwise false
    #get starting row, ending row, starting column and ending column
    starting_row = starting_coordinate[:1]

    starting_column = int(starting_coordinate[1:])
    ending_row = ending_coordinate[:1]
    ending_column = int(ending_coordinate[1:])

    #IF ending coordinate doesn't have a friendly piece THEN
    if pieceTeam(ending_coordinate, board) != pieceTeam(starting_coordinate, board) and pieceTeam(starting_coordinate, board) == turn:
        #IF the change in column == 2 AND the change in row == 1 THEN
        if abs(ending_column - starting_column) == 2 and abs(changeRowToDigit(ending_row) - changeRowToDigit(starting_row)) == 1:
            # the move is legal
            return True
    #ELSE IF the change in column == 1 AND the change in row == 2 THEN
    elif abs(ending_column - starting_column) == 1 and abs(changeRowToDigit(ending_row) - changeRowToDigit(starting_row)) == 2:
        # the move is legal
        return True
    # the move is illegal
    return False

#BEGIN bishopMovement(starting coordinate, ending coordinate, turn, board state)
def bishopMovement(starting_coordinate, ending_coordinate, turn, board): # --> returns true if the move is legal otherwise false
    #get starting row, ending row, starting column and ending column
    starting_row = starting_coordinate[:1]
    starting_column = int(starting_coordinate[1:])
    ending_row = ending_coordinate[:1]
    ending_column = int(ending_coordinate[1:])
    team = pieceTeam(starting_coordinate, board)
    #IF the ending coordinate doesn't contain a friendly piece THEN
    if pieceTeam(ending_coordinate, board) != team and pieceTeam(starting_coordinate, board) == turn:
        #IF the change in row == change in column THEN
        if abs(ending_column - starting_column) == abs(changeRowToDigit(ending_row) - changeRowToDigit(starting_row)):
            # the move is legal
            return True
    #the move is illegal
    return False

#BEGIN queenMovement(starting coordinate, ending coordinate, turn, board state)
def queenMovement(starting_coordinate, ending_coordinate, turn, board): # --> returns true if the move is legal otherwise false

    #IF the move is legal by bishop movement rules THEN
    if bishopMovement(starting_coordinate, ending_coordinate, turn, board):
        # the move is legal
        return True
    #ELSE IF the move is legal by rook movement rules THEN
    elif rookMovement(starting_coordinate, ending_coordinate, turn, board):
        # the move is legal
        return True
    #the move is illegal
    return False

#BEGIN kingMovement(starting coordinate, ending coordinate, turn, board state)
def kingMovement(starting_coordinate, ending_coordinate, turn, board): # --> returns true if the move is legal otherwise false
    #get starting row, ending row, starting column and ending column
    starting_row = starting_coordinate[:1]
    starting_column = int(starting_coordinate[1:])
    ending_row = ending_coordinate[:1]
    ending_column = int(ending_coordinate[1:])
    team = pieceTeam(starting_coordinate, board)
    #IF destination square doen't contain a friendly piece and the piece moved is of the correct team THEN
    if pieceTeam(ending_coordinate, board) != team and pieceTeam(starting_coordinate, board) == team:
        #IF ending_coordinate is adjacent to starting_coordinate THEN
        if abs(ending_column - starting_column) < 1 and abs(ending_column - starting_column) > -1 and abs(changeRowToDigit(ending_row) - changeRowToDigit(starting_row)) > -1 and abs(changeRowToDigit(ending_row) - changeRowToDigit(starting_row)) < 2:
            return True
    return False


def findRookBoundaries(move, board, direction):
    print("Move being tested in rook/queen findRookBoundaries:", move)
    #Break the move down into coordinates
    move = move.split('x')

    #Break down coordinates into x and y
    starting_coordinate = move[0]
    ending_coordinate = move[1]
    starting_row = changeRowToDigit(starting_coordinate[0])
    starting_column = int(starting_coordinate[1]) - 1
    ending_row = changeRowToDigit(ending_coordinate[0])
    ending_column = int(ending_coordinate[1]) -1

    #IF the rook is moving horizontal THEN
    if direction == "Horizontal":
        print("The rook/queen is moving horizontally")
        direction = False
        #IF the change in row is positive THEN
        if starting_row - ending_row > 0:
            print("The rook/queen is moving left")
            print(" ")
            # the rook is moving LEFT
            for steps_away in range(starting_row - ending_row):
                #Prevent counting starting coordinate for testing
                if steps_away != 0:
                    print("testing square:", changeDigitToRow(starting_row - steps_away) + str(starting_column))
                    #If the square in the direction of movement steps_away steps away is not empty i.e. contains a piece THEN
                    if board[starting_row - steps_away][starting_column] != '  ':
                        
                        piece_coordinate = str(starting_row - steps_away) + str(starting_column)
        #IF the change in row is negitive THEN
        if starting_row - ending_row < 0:

            #The rook is moveing RIGHT
            for steps_away in range(abs(starting_row - ending_row)):
                if steps_away != 0:
                    #If the square in the direction of movement steps_away steps away is not empty i.e. contains a piece THEN
                    if board[starting_row + steps_away][starting_row] != '  ':
                        piece_coordinate = str(starting_row + steps_away) + str(starting_row)


    #IF the rook is moving vertically THEN
    if direction == "Vertical":

        direction = True
        #IF the rook is moving Down THEN
        if starting_row - ending_row > 0:

            for steps_away in range(starting_row - ending_row):
                if steps_away != 0:

                    #If the square in the direction of movement steps_away steps away is not empty i.e. contains a piece THEN
                    if board[starting_row][starting_row - steps_away] != '  ':
                        piece_coordinate = str(starting_row) + str(starting_row - steps_away)
        #IF the rook is moving up THEN
        if starting_row - ending_row < 0:

            #The rook is moveing up
            for steps_away in range(abs(starting_row - ending_row)):
                if steps_away != 0:
                    #If the square in the direction of movement steps_away steps away is not empty i.e. contains a piece THEN
                    if board[starting_row][starting_row + steps_away] != '  ':
                        piece_coordinate = str(starting_row) + str(starting_row + steps_away)
    return (getCoordinateDifferenceRook(starting_coordinate, piece_coordinate, direction) - 1)

def getCoordinateDifferenceRook(starting_coordinate, max_coordinate, direction):
    #Break down the coordinates of the found piece and the piece being moved
    starting_row = int(changeRowToDigit(starting_coordinate[0]))
    piece_row = int(max_coordinate[0])
    starting_row = int(starting_coordinate[1])
    piece_row = int(max_coordinate[1])

    diffrow = abs(starting_row- piece_row)
    diffrow = abs(starting_row - piece_row)
    #If the rook is moveing up / down THEN
    if direction:
        return diffrow
    #IF the rook is moveing left / right THEN
    else:
        return diffrow
