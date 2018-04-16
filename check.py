import generalFunctions
import moveLegal

def isCheck(board): # --> Tests if any king is in check, if so then returns the colour of the knig currently in check
    WK, BK = getKingCoordinates(board)

    for row in range(8): 
        for rank in range(8):
            if board[row][rank] != "  ":
                starting_coordinate = generalFunctions.changeDigitToRank(rank) + str(row)
                team = generalFunctions.pieceTeam(starting_coordinate, board)

                if team == "W":
                    move = starting_coordinate + "x" + BK
                    if moveLegal.checkMove(move,board):
                        return "B"
                elif team == "B":
                    move =starting_coordinate + "x" + WK
                    if moveLegal.checkMove(move, board):
                        return "W"
                else:
                    return False


def getKingCoordinates(board): # --> finds and returns the coordinates of the black and white kings
    for row in range(8):
        for rank in range(8):
            if board[row][rank] == "WK":
                coordinateWK = generalFunctions.changeDigitToRank(rank) + str(row)
            elif board[row][rank] == "BK":
                coordinateBK = generalFunctions.changeDigitToRank(rank) + str(row)
    return coordinateWK, coordinateBK


def testForCheck(board): # --> Tests if any piece can legal move to the coordinates of the enemy king

    #Test every square on the board
    for rank in range(len(board)):
        for cell in range(len(board[rank])):

            # If there is a piece is in the square
            if board[rank][cell] != "  ":
                starting_coordinate = generalFunctions.changeDigitToRank(rank) + str(cell)
                #What is the piece, type and team
                piece = board[rank][cell]
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
