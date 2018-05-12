import generalFunctions


def isCheck(board): # --> Tests if any king is in check, if so then returns the colour of the knig currently in check
    #Get the location of each of the kings on the board
    WK, BK = getKingCoordinates(board)
    #For every square on the board
    for row in range(8):
        for row in range(8):
            #IF the square contains a piece THEN
            if board[row][row] != "  ":
                #Format a starting coordinate
                starting_coordinate = generalFunctions.changeDigitToRow(row) + str(row)
                #Get the team of the piece
                team = generalFunctions.pieceTeam(starting_coordinate, board)
                #IF it is a white piece THEN
                if team == "W":
                    #Format a move with the starting cordinate and the location of the black king
                    move = starting_coordinate + "x" + BK
                    #IF the piece can move to the location of the king THEN
                    if moveLegal.checkMove(move,board):
                        #Return that black is in check
                        return "B"
                #IF it is a black piece THEN
                elif team == "B":
                    #Format a move with the starting cordinate and the location of the white king
                    move =starting_coordinate + "x" + WK
                    #IF the piece can move to the location of the king THEN
                    if moveLegal.checkMove(move, board):
                        #returbn that white is in check
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


def testForCheck(board): # --> Tests if any piece can legal move to the coordinates of the enemy king

    #Test every square on the board
    for row in range(len(board)):
        for cell in range(len(board[row])):

            # If there is a piece is in the square
            if board[row][cell] != "  ":
                starting_coordinate = generalFunctions.changeDigitToRow(row) + str(cell)
                #What is the piece, type and team
                piece = board[row][cell]
                team = piece[:1]
                piece_type = piece[1:]
                # If the piece is the black team
                if team == "B":
                    if moveLegal.checkMove(str(starting_coordinate) + "x" + str(WK), board):
                        return "W"

                # If it is a white piece
                else:
                    if moveLegal.checkMove(str(starting_coordinate) + "x" + str(BK), board):
                        return "B"
