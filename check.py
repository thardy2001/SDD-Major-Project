import generalFunctions
import whiteMove
import AI
import moveLegal


def isCheck(board): # --> Tests if any king is in check, if so then returns the colour of the knig currently in check
    #Get the location of each of the kings on the board
    WK, BK = getKingCoordinates(board)

    #Find the coordinates of all black and white pieces
    startingCoordinatesWhite, startingCoordinatesBlack = getStartingCoordinates(board)
    #Get the list of all legal moves
    moves_list_white = moveLegal.generateMoveList(board,startingCoordinatesWhite, "W" )
    print("All white moves: ", moves_list_white)
    moves_list_black = moveLegal.generateMoveList(board, startingCoordinatesBlack, "B")
    print("All black moves: ", moves_list_black)

    #FOR all starting coordinates
    for item in range(len(startingCoordinatesWhite)):
        #Get current starting coordinate
        startingCoordinate = startingCoordinatesWhite[item]


        #Format a move with the starting cordinate and the location of the black king
        move = startingCoordinate + "x" + BK
        print(move)


        #IF the piece can move to the location of the king THEN
        if move in moves_list_white:
            #Return that black is in check
            print("White has CHECKED Black!")
            return "B"
    #FOR all starting coordinates
    for item in range(len(startingCoordinatesBlack)):
        #Get current starting coordinate
        startingCoordinate = startingCoordinatesBlack[item]

        #Format a move with the starting cordinate and the location of the white king
        move = startingCoordinate + "x" + WK
        #IF the piece can move to the location of the king THEN
        if move in moves_list_black:
            #return that white is in check
            print("Black has CHECKED White!")
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
    if type(coordinateWK) == None:
        print("GAME OVER, BLACK WINS")
        coordinateWK = ""
    elif type(coordinateBK) == None:
        print("GAME OVER, BLACK WINS")
        coordinateBK = ''

    return coordinateWK, coordinateBK


def getStartingCoordinates(board):
    #Initiallise lists for all starting coordinates
    whiteStartingCoordinates = []
    blackStartingCoordinates = []
    #FOR all squares on the board
    for row in range(8):
        for column in range(8):
            #IF the square is not empty THEN
            if board[column][row] != "  ":
                #Get the coordinate
                coordinate = generalFunctions.changeDigitToRow(row) + str(column)
                #Get the piece
                piece = board[column][row]
                #Get the team of the piece
                team = piece[0]
                #IF the piece is white THEN
                if team == "W":
                    #Add it to the list of white locations
                    whiteStartingCoordinates.append(coordinate)
                #IF it's not white then in must be black
                else:
                    #Add coordinate to list of black coordinates
                    blackStartingCoordinates.append(coordinate)
                    
    return whiteStartingCoordinates, blackStartingCoordinates
