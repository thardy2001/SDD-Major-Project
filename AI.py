import generalFunctions
import random
import moveLegal

#Black makes a move
def makeMove(board):
    #check the board for all black piece coordinates
    startingPositions = generateStartingCoordinates(board)

    #generate a list of all legal moves black can make
    moves_list = generateMoveList(board, startingPositions)
    #Organise the list based on quality of the moves

    #Perform a move
    last_taken_piece = generalFunctions.performMove(moves_list[random.randint(0, len(moves_list) -1)], board)


#BEGIN generateStartingCoordinates(board)
def generateStartingCoordinates(board): # --> Returns a list of all coordinates containing black pieces
    coordinate_list = []
    displayed_coordinates = []
    #FOR every file on the board
    for row in range(8):
        #FOR every row on the board
        for row in range(8):
            # IF the square has a black piece THEN
            coordinate = generalFunctions.changeDigitToRow(row) + str(row)
            if generalFunctions.pieceTeam(coordinate, board) == "B":
                displayed_coordinates.append(str(coordinate[0]) + str(int(coordinate[1]) + 1))
                #add the coordinate to a list
                coordinate_list.append(coordinate)
    #return the list of starting coordinates

    return coordinate_list




# BEGIN generateMoveList(board, starting coordinates )
def generateMoveList(board, startingCoordinates): # --> Returns a list of all legal moves that black can make.
    legal_moves = []
    displayed_moves = []
    #For every black piece on the board
    for coordinates in range(len(startingCoordinates)):
        #print("Testing For legal moves for piece in coordinate:", startingCoordinates[coordinates][0] + str(int(startingCoordinates[coordinates][1]) + 1))
        #For every square on the board
        for row in range(8):
            for row in range(8):
                #ending coordinate == current coordinate being tested
                end_coordinate = generalFunctions.changeDigitToRow(row) + str(row)

                #generate a move by combining the starting cordinate and endiong coordinate
                tested_move = startingCoordinates[coordinates] + "x" + end_coordinate
                #IF piece in starting coordinate can legally move there THEN

                if moveLegal.checkMove(tested_move, board):
                    #print("Found:", end_coordinate[0] + str(int(end_coordinate[1]) + 1), "As a legal Move")
                    displayed_moves.append(startingCoordinates[coordinates][0] + str(int(startingCoordinates[coordinates][1]) + 1)+ "x" + end_coordinate[0] + str(int(end_coordinate[1]) + 1))
                    # add move to list of legal moves
                    legal_moves.append(tested_move)
    #Return the list of legal moves
    print(displayed_moves)
    #print("All found legal destinations:", displayed_moves)
    return legal_moves
