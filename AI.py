import generalFunctions
import random


piece_locations =["a7", 'a6', 'b7', 'b6',"c7", 'c6', 'd7', 'd6',"e7", 'e6', 'f7', 'f6', "g7", 'g6', 'h7', 'h6',]
#Black makes a move
def makeMove(board):
    #check the board for all black piece coordinates
    startingPositions = piece_locations[]

    #generate a list of all legal moves black can make
    moves_list = generateMoveList(board, startingPositions)
    #Organise the list based on quality of the moves
    num = random.randint(0, len(moves_list) -1)
    #Perform a move
    last_taken_piece = generalFunctions.performMove(moves_list[num], board)

    #Update the locations of black pieces
    del startingPositions[num]
    move = moves_list[num].split('x')
    startingPositions.append(move[1])

'''
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
    print("Moves the AI can make:",displayed_moves)
    #print("All found legal destinations:", displayed_moves)
    return legal_moves
'''
def generateMoveList(board, startingCoordinates):
    for piececoordinate in range(len(startingCoordinates)):
        piece_type = board[changeRowToDigit(piececoordinate[0])][piececoordinate[1]][1]

        #IF the piece is a PAWN THEN
        if piece_type == "P":
            #IF the pawn is moving one down AND the square is empty THEN
            if board[changeRowToDigit(piececoordinate[0])][int(piececoordinate[1] - 1)] == "  ":
                move_list = move_list.append(piececoordinate + 'x' + piececoordinate[0] + str(int(piececoordinate[1] - 1)))
            #IF the pawn is moving down 2 AND both the square infront of the piece and ending destination are empty AND the pawn has yet to move THEN
            if board[changeRowToDigit(piececoordinate[0])][int(piececoordinate[1] - 2)] == "  " and board[changeRowToDigit(piececoordinate[0])][int(piececoordinate[1] - 1)] == "  " and int(piececoordinate[1] - 1) == 6:
                move_list = move_list.append(piececoordinate + 'x' + piececoordinate[0] + str(int(piececoordinate[1] - 2)))
            #IF the pawn is moving down one and across one AND the destination square has a white piece THEN
            if board[changeRowToDigit(piececoordinate[0]) + 1][int(piececoordinate[1] - 1)][0] == "W":
                move_list = move_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0] + 1)) + str(int(piececoordinate[1] - 1)))
            #IF the pawn is moving down one and across one AND the destination square has a white piece THEN
            if board[changeRowToDigit(piececoordinate[0]) - 1][int(piececoordinate[1] - 1)][0] == "W":
                move_list = move_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0] - 1)) + str(int(piececoordinate[1] - 1)))
        #KING
        if piece_type == "K":
            moves_list = generateMovesKing(board, moves_list, piececoordinate)
        #KNIGHT
        if piece_type == "N":
            moves_list = generateMovesKnight(board, moves_list, piececoordinate)
        #ROOK
        if piece_type == "R":
            moves_list = generateMovesRook(board, moves_list, piececoordinate)
        #BISHOP
        if piece_type == "B":
            moves_list = generateMovesBishop(board, moves_list, piececoordinate)
        #QUEEN
        if piece_type == "Q":
            moves_list = generateMovesBishop(board, moves_list, piececoordinate)
            moves_list = generateMovesRook(board, moves_list, piececoordinate)


def generateMovesKing(board, moves_list, piececoordinate):
    #DOWN
    if board[changeRowToDigit(piececoordinate[0])][int(piececoordinate[1] - 1)][0] != "B":
        move_list = move_list.append(piececoordinate + 'x' + piececoordinate[0] + str(int(piececoordinate[1] - 1)))
    #UP
    if board[changeRowToDigit(piececoordinate[0])][int(piececoordinate[1] + 1)][0] != "B":
        move_list = move_list.append(piececoordinate + 'x' + piececoordinate[0] + str(int(piececoordinate[1] + 1)))
    #LEFT
    if board[changeRowToDigit(piececoordinate[0] - 1)][int(piececoordinate[1])][0] != "B":
        move_list = move_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0] - 1)) + piececoordinate[1])
    #RIGHT
    if board[changeRowToDigit(piececoordinate[0] + 1)][int(piececoordinate[1])][0] != "B":
        move_list = move_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0] + 1)) + piececoordinate[1])
    #TOP RIGHT CORNER
    if board[changeRowToDigit(piececoordinate[0] + 1)][int(piececoordinate[1] + 1 )][0] != "B":
        move_list = move_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0] + 1)) + str(int(piececoordinate[1] + 1)))
    #TOP LEFT CORNER
    if board[changeRowToDigit(piececoordinate[0] - 1)][int(piececoordinate[1] + 1 )][0] != "B":
        move_list = move_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0] - 1)) + str(int(piececoordinate[1] + 1)))
    # BOTTOM LEFT CORNER
    if board[changeRowToDigit(piececoordinate[0] - 1)][int(piececoordinate[1] - 1 )][0] != "B":
        move_list = move_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0] - 1)) + str(int(piececoordinate[1] - 1)))
    #BOTTOM RIGHT CORNER
    if board[changeRowToDigit(piececoordinate[0] + 1)][int(piececoordinate[1] - 1 )][0] != "B":
        move_list = move_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0] + 1)) + str(int(piececoordinate[1] - 1)))

    return moves_list

def generateMovesKnight(board, moves_list, piececoordinate):
    #lEFT 2 DOWN 1
    if board[changeRowToDigit(piececoordinate[0] - 2)][int(piececoordinate[1] - 1 )][0] != "B":
        move_list = move_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0] - 2)) + str(int(piececoordinate[1] - 1)))
    #RIGHT 2 DOWN 1
    if board[changeRowToDigit(piececoordinate[0] + 2)][int(piececoordinate[1] - 1 )][0] != "B":
        move_list = move_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0] + 2)) + str(int(piececoordinate[1] - 1)))
    #LEFT 2 UP 1
    if board[changeRowToDigit(piececoordinate[0] - 2)][int(piececoordinate[1] + 1 )][0] != "B":
        move_list = move_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0] - 2)) + str(int(piececoordinate[1] + 1)))
    #RIGHT 2 UP 1
    if board[changeRowToDigit(piececoordinate[0] + 2)][int(piececoordinate[1] + 1 )][0] != "B":
        move_list = move_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0] + 2)) + str(int(piececoordinate[1] + 1)))
    #DOWN 2 LEFT 1
    if board[changeRowToDigit(piececoordinate[0] - 1)][int(piececoordinate[1] - 2 )][0] != "B":
        move_list = move_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0] - 1)) + str(int(piececoordinate[1] - 2)))
    #UP 2 LEFT 1
    if board[changeRowToDigit(piececoordinate[0] - 1)][int(piececoordinate[1] + 2 )][0] != "B":
        move_list = move_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0] - 1)) + str(int(piececoordinate[1] + 2)))
    #DOWN 2 RIGHT 1
    if board[changeRowToDigit(piececoordinate[0] + 1)][int(piececoordinate[1] - 2 )][0] != "B":
        move_list = move_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0] + 1)) + str(int(piececoordinate[1] - 2)))
    #UP 2 RIGHT 1
    if board[changeRowToDigit(piececoordinate[0] + 1)][int(piececoordinate[1] + 2 )][0] != "B":
        move_list = move_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0] + 1)) + str(int(piececoordinate[1] + 2)))

    return moves_list

def generateMovesBishop(board, moves_list, piececoordinate):

    count = 0
    #UP LEFT
    while changeRowToDigit(piececoordinate[0]) - count > -1 and  int(piececoordinate[1]) + count < 8:
        count+=1
        if board[changeRowToDigit(piececoordinate[0] ) - count][int(piececoordinate[1]) + count] == "  ":
            move_list = move_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) - count) + str(int(piececoordinate[1] ) + count))
        elif board[changeRowToDigit(piececoordinate[0] ) - count][int(piececoordinate[1]) + count][0] == "W":
            move_list = move_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) - count) + str(int(piececoordinate[1] ) + count))
            count = 0
            break
        count = 0
        break
    #UP RIGHT
    while changeRowToDigit(piececoordinate[0]) + count < 8 and  int(piececoordinate[1]) + count < 8:
        count+=1
        if board[changeRowToDigit(piececoordinate[0] ) + count][int(piececoordinate[1]) + count] == "  ":
            move_list = move_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) + count) + str(int(piececoordinate[1] ) + count))
        elif board[changeRowToDigit(piececoordinate[0] ) + count][int(piececoordinate[1]) + count][0] == "W":
            move_list = move_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) + count) + str(int(piececoordinate[1] ) + count))
            count = 0
            break
        count = 0
        break
    #DOWN LEFT
    while changeRowToDigit(piececoordinate[0]) - count > -1 and  int(piececoordinate[1]) - count > -1:
        count+=1
        if board[changeRowToDigit(piececoordinate[0] ) - count][int(piececoordinate[1]) - count] == "  ":
            move_list = move_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) - count) + str(int(piececoordinate[1] ) - count))
        elif board[changeRowToDigit(piececoordinate[0] ) - count][int(piececoordinate[1]) - count][0] == "W":
            move_list = move_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) - count) + str(int(piececoordinate[1] ) - count))
            count = 0
            break
        count = 0
        break
    #DOWN RIGHT
    while changeRowToDigit(piececoordinate[0]) + count < 8 and  int(piececoordinate[1]) - count > -1:
        count+=1
        if board[changeRowToDigit(piececoordinate[0] ) + count][int(piececoordinate[1]) - count] == "  ":
            move_list = move_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) + count) + str(int(piececoordinate[1] ) - count))
        elif board[changeRowToDigit(piececoordinate[0] ) + count][int(piececoordinate[1]) - count][0] == "W":
            move_list = move_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) + count) + str(int(piececoordinate[1] ) - count))
            count = 0
            break
        count = 0
        break

    return moves_list
def generateMovesRook(board, moves_list, piececoordinate):
    #UP
    for squares in range( 8 - int(piececoordinate[1]) ):
        if squares != 0:
            if board[changeRowToDigit(piececoordinate[0])][int(piececoordinate[1] + squares)] == "  ":
                move_list = move_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0])) + str(int(piececoordinate[1] + squares)))
            elif board[changeRowToDigit(piececoordinate[0])][int(piececoordinate[1] + squares)][0] == "W":
                move_list = move_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0])) + str(int(piececoordinate[1] + squares)))
                break
            else:
                break
    #RIGHT
    for squares in range (8 - changeRowToDigit(piececoordinate[0])):
        if squares != 0:
            if board[changeRowToDigit(piececoordinate[0]) + squares][int(piececoordinate[1])] == "  ":
                move_list = move_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) + squares) + str(int(piececoordinate[1] )))
            elif board[changeRowToDigit(piececoordinate[0]) + squares][int(piececoordinate[1])][0] == "W":
                move_list = move_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) + squares) + str(int(piececoordinate[1] )))
                break
            else:
                break
    #DOWN
    for squares in range(int(piececoordinate[1])):
        if squares != 0:
            if board[changeRowToDigit(piececoordinate[0])][int(piececoordinate[1] - squares)] == "  ":
                move_list = move_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0])) + str(int(piececoordinate[1] - squares)))
            elif board[changeRowToDigit(piececoordinate[0])][int(piececoordinate[1] - squares)][0] == "W":
                move_list = move_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0])) + str(int(piececoordinate[1] - squares)))
                break
            else:
                break
    #LEFT
    for squares in range(changeRowToDigit(piececoordinate[0])):
        if squares != 0:
            if board[changeRowToDigit(piececoordinate[0]) - squares][int(piececoordinate[1])] == "  ":
                move_list = move_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) - squares) + str(int(piececoordinate[1] )))
            elif board[changeRowToDigit(piececoordinate[0]) - squares][int(piececoordinate[1])][0] == "W":
                move_list = move_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) - squares) + str(int(piececoordinate[1] )))
                break
            else:
                break

    return move_list
