from generalFunctions import *
import check
piece_locations =["a0", 'a1', 'b0', 'b1',"c0", 'c1', 'd0', 'd1',"e0", 'e1', 'f0', 'f1', "g0", 'g1', 'h0', 'h1',]
# --> asks for an inputed move and performs it if it is legal
def makeMove(board):
    print("ENTER Q to QUIT")
    move = input("Make Your Move:") # MUST be in the form 'starting coordinate x ending coordinate' --> example: B1xC1
    if move =='q' or move == "Q":
        quit()
    if len(move) != 5 or move[2] != 'x' or move[0]  not in 'ABCDEFGHabcdefgh' and move[3] not in 'ABCDEFGHabcdefgh' or move[1] not in '12345678' and move[4] not in '12345678':
        print("non-acceptable move attempt - Must be in the form 'starting coordinate x ending coordinate' --> example: B1xC1 ")
        makeMove(board)


    move = convertPlayerMove(move)

    moves_list = generateMoveList(board, piece_locations)
    # If the move entered is legal
    if move in moves_list:

        #Make the move by changing the board
        last_taken_piece = generalFunctions.performMove(move, board)
        #If white king is in check then
        if check.isCheck(board) == "W":
            #Undo the move

            generalFunctions.undoMove(move,last_taken_piece,  board)

            print("illegal move, try again (CHECK)")
            makeMove(board)

    else:
        print("illegal move, try again")
        makeMove(board)

    move = moves_list[num].split('x')
    indexOfStartingPosition =  startingPositions.index(move[0])
    del startingPositions[indexOfStartingPosition]
    startingPositions.append(move[1])

def convertPlayerMove(move): # --> converts the inputed player move to a move usable by calculations. (changes the column of all coordinates by - 1)
    move = move.split("x")
    starting_coordinate = move[0]
    starting_column = str(int(starting_coordinate[1:]) - 1)
    starting_coordinate = starting_coordinate[:1] + starting_column
    ending_coordinate = move[1]
    ending_column = str(int(ending_coordinate[1:]) - 1)
    ending_coordinate = ending_coordinate[:1] + ending_column
    new_move = starting_coordinate + "x" + ending_coordinate
    return new_move



def generateMoveList(board, startingCoordinates):
    moves_list = []
    for item in range(len(startingCoordinates)):
        piececoordinate = startingCoordinates[item]
        piece = board[changeRowToDigit(piececoordinate[0])][int(piececoordinate[1])]
        piece_type = piece[1]

        #IF the piece is a PAWN THEN
        if piece_type == "P":
            #IF the pawn is moving one down AND the square is empty THEN
            if board[changeRowToDigit(piececoordinate[0])][int(piececoordinate[1] - 1)] == "  ":
                move_list = move_list.append(piececoordinate + 'x' + piececoordinate[0] + str(int(piececoordinate[1] - 1)))
            #IF the pawn is moving down 2 AND both the square infront of the piece and ending destination are empty AND the pawn has yet to move THEN
            if board[changeRowToDigit(piececoordinate[0])][int(piececoordinate[1] - 2)] == "  " and board[changeRowToDigit(piececoordinate[0])][int(piececoordinate[1] - 1)] == "  " and int(piececoordinate[1] - 1) == 6:
                move_list = move_list.append(piececoordinate + 'x' + piececoordinate[0] + str(int(piececoordinate[1] - 2)))
            #IF the pawn is moving down one and across one AND the destination square has a white piece THEN
            if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) + 1) +str(int(piececoordinate[1] - 1)), board) == "B":
                move_list = move_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0] + 1)) + str(int(piececoordinate[1] - 1)))
            #IF the pawn is moving down one and across one AND the destination square has a white piece THEN
            if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) - 1)+ str(int(piececoordinate[1] - 1)), board) == "B":
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
    if pieceTeam(piececoordinate[0] + str(int(piececoordinate[1] - 1)), board) != "W":
        move_list = move_list.append(piececoordinate + 'x' + piececoordinate[0] + str(int(piececoordinate[1] - 1)))
    #UP
    if pieceTeam(piececoordinate[0] + str(int(piececoordinate[1] + 1)), board) != "W":
        move_list = move_list.append(piececoordinate + 'x' + piececoordinate[0] + str(int(piececoordinate[1] + 1)))
    #LEFT
    if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0] - 1)) + piececoordinate[1], board) != "W":
        move_list = move_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0] - 1)) + piececoordinate[1])
    #RIGHT
    if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0] + 1)) + piececoordinate[1], board) != "W":
        move_list = move_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0] + 1)) + piececoordinate[1])
    #TOP RIGHT CORNER
    if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0] + 1)) + str(int(piececoordinate[1] + 1 )), board) != "W":
        move_list = move_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0] + 1)) + str(int(piececoordinate[1] + 1)))
    #TOP LEFT CORNER
    if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0] - 1)) + str(int(piececoordinate[1] + 1 )), board) != "W":
        move_list = move_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0] - 1)) + str(int(piececoordinate[1] + 1)))
    # BOTTOM LEFT CORNER
    if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0] - 1)) + str(int(piececoordinate[1] - 1 )), board) != "W":
        move_list = move_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0] - 1)) + str(int(piececoordinate[1] - 1)))
    #BOTTOM RIGHT CORNER
    if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0] + 1)) + str(int(piececoordinate[1] - 1 )), board) != "W":
        move_list = move_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0] + 1)) + str(int(piececoordinate[1] - 1)))

    return moves_list

def generateMovesKnight(board, moves_list, piececoordinate):
    #lEFT 2 DOWN 1
    if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) - 2) + str(int(piececoordinate[1]) - 1 ), board) != "W":
        move_list = move_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0] - 2)) + str(int(piececoordinate[1]) - 1))
    #RIGHT 2 DOWN 1
    if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) + 2) + str(int(piececoordinate[1]) - 1 ), board) != "W":
        move_list = move_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0] + 2)) + str(int(piececoordinate[1]) - 1))
    #LEFT 2 UP 1
    if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) - 2) + str(int(piececoordinate[1]) + 1 ), board) != "W":
        move_list = move_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0] - 2)) + str(int(piececoordinate[1]) + 1))
    #RIGHT 2 UP 1
    if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) + 2) + str(int(piececoordinate[1]) + 1 ), board) != "W":
        move_list = move_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0] + 2)) + str(int(piececoordinate[1]) + 1))
    #DOWN 2 LEFT 1
    if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) - 1) + str(int(piececoordinate[1]) - 2 ), board) != "W":
        move_list = move_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0] - 1)) + str(int(piececoordinate[1]) - 2))
    #UP 2 LEFT 1
    if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) - 1) + str(int(piececoordinate[1]) + 2 ), board) != "W":
        move_list = move_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0] - 1)) + str(int(piececoordinate[1]) + 2))
    #DOWN 2 RIGHT 1
    if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) + 1) + str(int(piececoordinate[1]) - 2 ), board) != "W":
        move_list = move_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0] + 1)) + str(int(piececoordinate[1]) - 2))
    #UP 2 RIGHT 1
    if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) + 1) + str(int(piececoordinate[1]) + 2 ), board) != "W":
        move_list = move_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0] + 1)) + str(int(piececoordinate[1]) + 2))

    return moves_list

def generateMovesBishop(board, moves_list, piececoordinate):

    count = 0
    #UP LEFT
    while changeRowToDigit(piececoordinate[0]) - count > -1 and  int(piececoordinate[1]) + count < 8:
        count+=1
        if board[changeRowToDigit(piececoordinate[0] ) - count][int(piececoordinate[1]) + count] == "  ":
            move_list = move_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) - count) + str(int(piececoordinate[1] ) + count))
        elif pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0] ) - count) + str(int(piececoordinate[1]) + count), board)== "B":
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
        elif pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0] ) + count) + str(int(piececoordinate[1]) + count), board) == "B":
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
        elif pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0] ) - count) + str(int(piececoordinate[1]) - count), board) == "B":
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
        elif pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0] ) + count) + str(int(piececoordinate[1]) - count), board)== "B":
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
            if board[changeRowToDigit(piececoordinate[0])][int(piececoordinate[1]) + squares] == "  ":
                move_list = move_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0])) + str(int(piececoordinate[1] + squares)))
            elif pieceTeam(piececoordinate[0] + str(int(piececoordinate[1]) + squares), board)== "B":
                move_list = move_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0])) + str(int(piececoordinate[1] + squares)))
                break
            else:
                break
    #RIGHT
    for squares in range (8 - changeRowToDigit(piececoordinate[0])):
        if squares != 0:
            if board[changeRowToDigit(piececoordinate[0]) + squares][int(piececoordinate[1])] == "  ":
                move_list = move_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) + squares) + str(int(piececoordinate[1] )))
            elif pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) + squares) + piececoordinate[1], board) == "B":
                move_list = move_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) + squares) + str(int(piececoordinate[1] )))
                break
            else:
                break
    #DOWN
    for squares in range(int(piececoordinate[1])):
        if squares != 0:
            if board[changeRowToDigit(piececoordinate[0])][int(piececoordinate[1]) - squares] == "  ":
                move_list = move_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0])) + str(int(piececoordinate[1]) - squares))
            elif pieceTeam(piececoordinate[0] + str(int(piececoordinate[1] - squares)), board) == "B":
                move_list = move_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0])) + str(int(piececoordinate[1]) - squares))
                break
            else:
                break
    #LEFT
    for squares in range(changeRowToDigit(piececoordinate[0])):
        if squares != 0:
            if board[changeRowToDigit(piececoordinate[0]) - squares][int(piececoordinate[1])] == "  ":
                move_list = move_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) - squares) + str(int(piececoordinate[1] )))
            elif pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) - squares) + piececoordinate[1], board)== "B":
                move_list = move_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) - squares) + str(int(piececoordinate[1] )))
                break
            else:
                break
    print("All moves white can make: (should total to 20 moves) ", moves_list)
    return moves_list
