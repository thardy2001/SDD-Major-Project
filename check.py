import generalFunctions
import whiteMove
import AI
import moveLegal

def isCheck(board): # --> Tests if any king is in check, if so then returns the colour of the knig currently in check
    #Get the location of each of the kings on the board
    WK, BK = getKingCoordinates(board)
    #For every square on the board
    startingCoordinatesWhite, startingCoordinatesBlack = getStartingCoordinates(board)


    for item in range(len(startingCoordinatesWhite)):
        startingCoordinate = startingCoordinatesWhite[item]


        #Format a move with the starting cordinate and the location of the black king
        move = startingCoordinate + "x" + BK
        #IF the piece can move to the location of the king THEN
        if move in moveLegal.generateMoveList(board,startingCoordinatesWhite, "W" ):
            #Return that black is in check
            return "B"

    for item in range(len(startingCoordinatesBlack)):
        startingCoordinate = startingCoordinatesBlack[item]

        #Format a move with the starting cordinate and the location of the white king
        move = startingCoordinate + "x" + WK
        #IF the piece can move to the location of the king THEN
        if move in moveLegal.generateMoveList(board, startingCoordinatesBlack, "B"):
            #return that white is in check
            return "W"
    else:
        #Return that noone is in check
        return False


def getKingCoordinates(board): # --> finds and returns the coordinates of the black and white kings
    #For every square on the board
    for row in range(8):
        for column in range(8):
            #If the square contains a white king THEN
            if board[row][column] == "WK":
                #Store the coordinates
                coordinateWK = generalFunctions.changeDigitToRow(row) + str(row)
            #IF the square contains a black king THEN
            elif board[row][column] == "BK":
                #Store the coordinates
                coordinateBK = generalFunctions.changeDigitToRow(row) + str(row)
    #Return the location of the kings
    return coordinateWK, coordinateBK


def getStartingCoordinates(board):
    whiteStartingCoordinates = []
    blackStartingCoordinates = []
    for row in range(8):
        for column in range(8):
            if board[column][row] != "  ":
                coordinate = generalFunctions.changeDigitToRow(row) + str(column)
                piece = board[column][row]
                team = piece[0]
                if team == "W":
                    whiteStartingCoordinates.append(coordinate)
                else:
                    blackStartingCoordinates.append(coordinate)
    return whiteStartingCoordinates, blackStartingCoordinates
