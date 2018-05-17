from generalFunctions import *

def generateMoveList(board, startingCoordinates, team): # --> Generates a list of all legal moves the given team can make
    #Initialise an empty list
    moves_list = []
    #FOR every coordinate in the list of starting coordinates (piece locations of a given team)
    for item in range(len(startingCoordinates)):
        #Get the location of the current piece
        piececoordinate = startingCoordinates[item]

        #Get the piece
        piece = board[int(piececoordinate[1])][changeRowToDigit(piececoordinate[0])]

        #Get the piece type
        piece_type = piece[1]

        #IF it is whites turn
        if team == "W":

            #WHITE PAWN
            if piece_type == "P":
                generateMovesPawnWhite(board, moves_list, piececoordinate)

            #WHITE KING
            if piece_type == "K":
                generateMovesKingWhite(board, moves_list, piececoordinate)

            #WHITE KNIGHT
            if piece_type == "N":
                generateMovesKnightWhite(board, moves_list, piececoordinate)

            #WHITE ROOK
            if piece_type == "R":
                generateMovesRookWhite(board, moves_list, piececoordinate)

            #WHITE BISHOP
            if piece_type == "B":
                generateMovesBishopWhite(board, moves_list, piececoordinate)

            #WHITE QUEEN
            if piece_type == "Q":
                generateMovesBishopWhite(board, moves_list, piececoordinate)
                generateMovesRookWhite(board, moves_list, piececoordinate)

        else:
            #BLACK PAWN
            if piece_type == "P":
                generateMovesPawnBlack(board, moves_list, piececoordinate)

            #BLACK KING
            if piece_type == "K":
                generateMovesKingBlack(board, moves_list, piececoordinate)

            #BLACK KNIGHT
            if piece_type == "N":
                generateMovesKnightBlack(board, moves_list, piececoordinate)

            #BLACK ROOK
            if piece_type == "R":
                generateMovesRookBlack(board, moves_list, piececoordinate)

            #BLACK BISHOP
            if piece_type == "B":
                generateMovesBishopBlack(board, moves_list, piececoordinate)

            #BLACK QUEEN
            if piece_type == "Q":
                generateMovesBishopBlack(board, moves_list, piececoordinate)
                generateMovesRookBlack(board, moves_list, piececoordinate)

    return moves_list


def generateMovesPawnWhite(board, moves_list, piececoordinate): # --> Adds all of the PAWNS legal moves to the overall move list

    if int(piececoordinate[1]) <7:

    #IF the pawn is moving one up AND the square is empty THEN
        if board[int(piececoordinate[1]) + 1][changeRowToDigit(piececoordinate[0])] == "  ":

            #Add the move to the list
            moves_list.append(piececoordinate + 'x' + piececoordinate[0] + str(int(piececoordinate[1]) + 1))

            if int(piececoordinate[1])+ 2 < 8:

                #IF the pawn is moving up 2 AND both the square infront of the piece and ending destination are empty AND the pawn has yet to move THEN
                if board[int(piececoordinate[1]) + 2][changeRowToDigit(piececoordinate[0])] == "  "  and int(piececoordinate[1]) == 1:

                    #Add the move to the list
                    moves_list.append(piececoordinate + 'x' + piececoordinate[0] + str(int(piececoordinate[1]) + 2))

    #IF the coordinate UP 1 and RIGHT 1 is on the board THEN
    if onBoard(str(changeRowToDigit(piececoordinate[0]) + 1) + str(int(piececoordinate[1]) + 1)):

        #IF the square UP 1 and RIGHT 1 has a black piece THEN
        if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) + 1) +str(int(piececoordinate[1]) + 1), board) == "B":

            #Add the move to the list
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) + 1) + str(int(piececoordinate[1]) + 1))

    #IF the coordinate UP 1 and LEFT 1 is on the board THEN
    if onBoard(str(changeRowToDigit(piececoordinate[0]) - 1)+ str(int(piececoordinate[1]) + 1)):

        #IF the square UP 1 and LEFT 1 has a black piece THEN
        if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) - 1)+ str(int(piececoordinate[1]) + 1), board) == "B":

            #Add the move to the list
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) - 1) + str(int(piececoordinate[1]) + 1))



def generateMovesPawnBlack(board, moves_list, piececoordinate): # --> Adds all of the PAWNS legal moves to the overall move list
    #IF the piece is higher on the board than the first row THEN
    if int(piececoordinate[1]) > 0:
        #IF the pawn is moving one up AND the square is empty THEN
        if board[int(piececoordinate[1]) - 1][changeRowToDigit(piececoordinate[0])] == "  ":

            #Add the move to the list
            moves_list.append(piececoordinate + 'x' + piececoordinate[0] + str(int(piececoordinate[1]) - 1))


            if int(piececoordinate[1]) - 2 < 8:

                #IF the square DOWN 2 is empty AND the piece is on the 6th row
                if board[int(piececoordinate[1]) - 2][changeRowToDigit(piececoordinate[0])] == "  " and int(piececoordinate[1]) == 6:

                    #Add the move to the list
                    moves_list.append(piececoordinate + 'x' + piececoordinate[0] + str(int(piececoordinate[1]) - 2))

    #IF the coordinate RIGHT 1 and DOWN 1 is on the board THEN
    if onBoard(str(changeRowToDigit(piececoordinate[0]) + 1) + str(int(piececoordinate[1]) - 1)):

        #IF the square RIGHT 1 and DOWN 1 has a white piece THEN
        if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) + 1) +str(int(piececoordinate[1]) - 1), board) == "W":

            #Add the move to the list
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) + 1) + str(int(piececoordinate[1]) - 1))

    #IF the coordinate LEFT 1 and DOWN 1 is on the board THEN
    if onBoard(str(changeRowToDigit(piececoordinate[0]) - 1)+ str(int(piececoordinate[1]) + 1)):

        #IF the square LEFT 1 and DOWN 1 has a white piece THEN
        if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) - 1)+ str(int(piececoordinate[1]) + 1), board) == "W":

            #Add the move to the list
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) - 1) + str(int(piececoordinate[1]) - 1))

def generateMovesKingWhite(board, moves_list, piececoordinate):# --> Adds all of the KINGS legal moves to the overall move list

    '''DOWN 1'''
    #IF the coordinate DOWN 1 is on the board THEN
    if onBoard(piececoordinate[0] + str(int(piececoordinate[1]) - 1)):

        #IF the square DOWN 1 doesn't have a white piece THEN
        if pieceTeam(piececoordinate[0] + str(int(piececoordinate[1] - 1)), board) != "W":

            #Add move to the list
             moves_list.append(piececoordinate + 'x' + piececoordinate[0] + str(int(piececoordinate[1]) - 1))

    '''UP 1'''
    #IF the coordinate UP 1 is on the board THEN
    if onBoard(piececoordinate[0] + str(int(piececoordinate[1]) + 1)):

        #IF the square UP 1 doesn't have a white piece THEN
        if pieceTeam(piececoordinate[0] + str(int(piececoordinate[1]) + 1), board) != "W":

            #Add move to the list
             moves_list.append(piececoordinate + 'x' + piececoordinate[0] + str(int(piececoordinate[1]) + 1))

    '''LEFT 1'''
    #IF the coordinate LEFT 1 is on the board THEN
    if onBoard(str(changeRowToDigit(piececoordinate[0]) - 1) + piececoordinate[1]):

        #IF the square LEFT 1 doesn't have a white piece THEN
        if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) - 1) + piececoordinate[1], board) != "W":

            #Add move to the list
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) - 1) + piececoordinate[1])

    '''RIGHT 1'''
    #IF the coordinate RIGHT 1 is on the board THEN
    if onBoard(str(changeRowToDigit(piececoordinate[0]) + 1) + piececoordinate[1]):

        #IF the square RIGHT 1 doesn't have a white piece THEN
        if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) + 1) + piececoordinate[1], board) != "W":

            #Add move to the list
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) + 1) + piececoordinate[1])

    '''TOP RIGHT CORNER'''
    #IF the coordinate RIGHT 1 and UP 1 is on the board THEN
    if onBoard(str(changeRowToDigit(piececoordinate[0]) + 1) + str(int(piececoordinate[1]) + 1 )):

        #IF the square RIGHT 1 and UP 1 doesn't have a white piece THEN
        if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) + 1) + str(int(piececoordinate[1]) + 1 ), board) != "W":

            #Add move to the list
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) + 1) + str(int(piececoordinate[1]) + 1))

    '''TOP LEFT CORNER'''
    #IF the coordinate LEFT 1 and UP 1 is on the board THEN
    if onBoard(str(changeRowToDigit(piececoordinate[0]) - 1) + str(int(piececoordinate[1]) + 1 )):

        #IF the square LEFT 1 and UP 1 doesn't have a white piece THEN
        if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) - 1) + str(int(piececoordinate[1]) + 1 ), board) != "W":

            #Add move to the list
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) - 1) + str(int(piececoordinate[1]) + 1))

     '''BOTTOM LEFT CORNER'''
     #IF the coordinate LEFT ! and DOWN 1 is on the board THEN
    if onBoard(str(changeRowToDigit(piececoordinate[0]) - 1) + str(int(piececoordinate[1]) - 1 )):

        #IF the square LEFT 1 and DOWN 1 doesn't have a white piece THEN
        if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) - 1) + str(int(piececoordinate[1]) - 1 ), board) != "W":

            #Add the move to the list
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) - 1) + str(int(piececoordinate[1]) - 1))

    '''BOTTOM RIGHT CORNER'''
    #IF the coordinate RIGHT 1 and DOWN 1 is on the board THEN
    if onBoard(str(changeRowToDigit(piececoordinate[0]) + 1) + str(int(piececoordinate[1]) - 1 )):

        #IF the square RIGHT 1 and DOWN 1 doesn't have a white piece THEN
        if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) + 1) + str(int(piececoordinate[1]) - 1 ), board) != "W":

            #Add move to the list
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) + 1) + str(int(piececoordinate[1]) - 1))



def generateMovesKnightWhite(board, moves_list, piececoordinate):# --> Adds all of the KNIGHTS legal moves to the overall move list

    '''lEFT 2 DOWN 1'''
    #IF the coordinate LEFT 2 and DOWN 1 is on the board THEN
    if onBoard(str(changeRowToDigit(piececoordinate[0]) - 2) + str(int(piececoordinate[1]) - 1 )):

        #IF the square LEFT 2 and DOWN 1 doesn't have a white piece THEN
        if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) - 2) + str(int(piececoordinate[1]) - 1 ), board) != "W":

            #Add the move to the list
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) - 2) + str(int(piececoordinate[1]) - 1))

    '''RIGHT 2 DOWN 1'''
    #IF the coordinate RIGHT 2 and DOWN 1 is on the board THEN
    if onBoard(str(changeRowToDigit(piececoordinate[0]) + 2) + str(int(piececoordinate[1]) - 1 )):

        #IF the square RIGHT 2 and DOWN 1 doesn't have a white piece THEN
        if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) + 2) + str(int(piececoordinate[1]) - 1 ), board) != "W":

            #Add move to the list
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) + 2) + str(int(piececoordinate[1]) - 1))

    '''LEFT 2 UP 1'''
    #IF the coordinate LEFT 2 and UP 1 is on the board THEN
    if onBoard(str(changeRowToDigit(piececoordinate[0]) - 2) + str(int(piececoordinate[1]) + 1 )):

        #IF the square LEFT 2 and UP 1 doesn't have a white piece THEN
        if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) - 2) + str(int(piececoordinate[1]) + 1 ), board) != "W":

            #Add the move to the list
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) - 2) + str(int(piececoordinate[1]) + 1))

    '''RIGHT 2 UP 1'''
    #IF the coordinate RIGHT 2 and UP 1 is on the board THEN
    if onBoard(str(changeRowToDigit(piececoordinate[0]) + 2) + str(int(piececoordinate[1]) + 1 )):

        #IF the square RIGHT 2 and UP 1 doesn't have a white piece THEN
        if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) + 2) + str(int(piececoordinate[1]) + 1 ), board) != "W":

            #Add the move to the list
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) + 2) + str(int(piececoordinate[1]) + 1))

    '''DOWN 2 LEFT 1'''
    #IF the coordinate DOWN 2 and LEFT 1 is on the board THEN
    if onBoard(str(changeRowToDigit(piececoordinate[0]) - 1) + str(int(piececoordinate[1]) - 2 )):

        #IF the square DOWN 2 and LEFT 1 doesn't have a white piece THEN
        if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) - 1) + str(int(piececoordinate[1]) - 2 ), board) != "W":

            #Add the move to the list
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) - 1) + str(int(piececoordinate[1]) - 2))

    '''UP 2 LEFT 1'''
    #IF the coordinate UP 2 and LEFT 1 is on the board THEN
    if onBoard(str(changeRowToDigit(piececoordinate[0]) - 1) + str(int(piececoordinate[1]) + 2 )):

        #IF the square UP 2 and left 1 doesn't have awhite piece THEN
        if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) - 1) + str(int(piececoordinate[1]) + 2 ), board) != "W":

            #Add the move to the list
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) - 1) + str(int(piececoordinate[1]) + 2))

    '''DOWN 2 RIGHT 1'''
    #IF the coordinate DOWN 2 and RIGHT 1 is on the board THEN
    if onBoard(str(changeRowToDigit(piececoordinate[0]) + 1) + str(int(piececoordinate[1]) - 2 )):

        #IF the square DOWN 2 and RIGHT 1 doesn't have a white piece THEN
        if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) + 1) + str(int(piececoordinate[1]) - 2 ), board) != "W":

            #Add the move to the list
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) + 1) + str(int(piececoordinate[1]) - 2))

    '''UP 2 RIGHT 1'''
    #IF the coordinate UP 2 and RIGHT 1 is on the board THEN
    if onBoard(str(changeRowToDigit(piececoordinate[0]) + 1) + str(int(piececoordinate[1]) + 2 )):

        #IF the square UP 1 and RIGHT 1 doesn't have a white piece THEN
        if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) + 1) + str(int(piececoordinate[1]) + 2 ), board) != "W":

            #Add the move to the list
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) + 1) + str(int(piececoordinate[1]) + 2))



def generateMovesBishopWhite(board, moves_list, piececoordinate):# --> Adds all of the BISHOPS legal moves to the overall move list

    #SET count to 0
    count = 0
    '''UP LEFT'''
    #WHILE the row - the count is > -1 AND the column + th count is < 0
    while changeRowToDigit(piececoordinate[0]) - count > -1 and  int(piececoordinate[1]) + count < 8:

        #IF the square UP count and LEFT count is empty THEN
        if board[int(piececoordinate[1]) + count][changeRowToDigit(piececoordinate[0] ) - count] == "  ":

            #Add the move to the list
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) - count) + str(int(piececoordinate[1] ) + count))

            #Increment count by 1
            count+=1

        #ELSE IF the square  UP count and LEFT count has a black piece THEN
        elif pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0] ) - count) + str(int(piececoordinate[1]) + count), board)== "B":

            #Add the move to the list
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) - count) + str(int(piececoordinate[1] ) + count))

            #Reset count to zero
            count = 0

            #END WHILE
            break

        #Reset count to 0
        count = 0

        #END WHILE
        break

    '''UP RIGHT'''
    #WHILE the the row + the count < 8 AND the column + the count is < 8
    while changeRowToDigit(piececoordinate[0]) + count < 8 and  int(piececoordinate[1]) + count < 8:

        #IF the square UP count and RIGHT count is empty THEN
        if board[int(piececoordinate[1]) + count][changeRowToDigit(piececoordinate[0] ) + count] == "  ":

            #Add the move to the list
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) + count) + str(int(piececoordinate[1] ) + count))

            #Increment count by 1
            count+=1

        #ELSE IF the square UP count and RIGHT count has a black piece THEN
        elif pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0] ) + count) + str(int(piececoordinate[1]) + count), board) == "B":

            #Add the move to the list
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) + count) + str(int(piececoordinate[1] ) + count))

            #Reset count to 0
            count = 0

            #END WHILE
            break

        #RESET count to 0
        count = 0

        #END WHILE
        break

    '''DOWN LEFT'''
    #WHILE column - count > -1  AND row - count > -1
    while changeRowToDigit(piececoordinate[0]) - count > -1 and  int(piececoordinate[1]) - count > -1:

        #IF the square DOWN count and LEFT count is empty THEN
        if board[int(piececoordinate[1]) - count][changeRowToDigit(piececoordinate[0] ) - count] == "  ":

            #Add the move to the list
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) - count) + str(int(piececoordinate[1] ) - count))

            #Increment count by 1
            count+=1

        #ELSE IF the square DOWN count and LEFT count has a black piece THEN
        elif pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0] ) - count) + str(int(piececoordinate[1]) - count), board) == "B":

            #Add the move to the list
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) - count) + str(int(piececoordinate[1] ) - count))

            #Reset count to 0
            count = 0

            #END WHILE
            break

        #Reset count to 0
        count = 0

        #END WHILE
        break

    '''DOWN RIGHT'''
    #WHILE row + count < 8 AND column - count > -1
    while changeRowToDigit(piececoordinate[0]) + count < 8 and  int(piececoordinate[1]) - count > -1:

        #IF the square DOWN count and RIGHT count is empty THEN
        if board[int(piececoordinate[1]) - count][changeRowToDigit(piececoordinate[0] ) + count] == "  ":

            #Add the move to the list
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) + count) + str(int(piececoordinate[1] ) - count))

            #Increment count by 1
            count+=1

        #ELSE IF the square DOWN count and RIGHT count has a black piece THEN
        elif pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0] ) + count) + str(int(piececoordinate[1]) - count), board)== "B":

            #Add the move to the list
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) + count) + str(int(piececoordinate[1] ) - count))

            #Reset count to 0
            count = 0

            #END WHILE
            break

        #Reset count to 0
        count = 0

        #END WHILE
        break


def generateMovesRookWhite(board, moves_list, piececoordinate):# --> Adds all of the ROOKS legal moves to the overall move list

    '''UP'''
    #FOR the squares in the range 8 - column of rook location
    for squares in range( 8 - int(piececoordinate[1]) ):

        #IF column + square != column THEN
        if squares != 0:

            #IF the square UP squares is empty THEN
            if board[int(piececoordinate[1]) + squares][changeRowToDigit(piececoordinate[0])] == "  ":

                #Add the move to the list
                moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0])) + str(int(piececoordinate[1]) + squares))

            #ELSE IF the square UP squares has a black piece THEN
            elif pieceTeam(piececoordinate[0] + str(int(piececoordinate[1]) + squares), board)== "B":

                #Add the move to the list
                moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0])) + str(int(piececoordinate[1]) + squares))

                #END FOR
                break
            #ELSE
            else:
                #END FOR
                break

    '''RIGHT'''
    #FOR squares in the range 8 - row of the rooks location
    for squares in range (8 - changeRowToDigit(piececoordinate[0])):

        #IF squares != 0
        if squares != 0:

            #IF the square RIGHT squares is empty THEN
            if board[int(piececoordinate[1])][changeRowToDigit(piececoordinate[0]) + squares] == "  ":

                #Add the move to the list
                moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) + squares) + str(int(piececoordinate[1]) ))

            #ELSE IF the square RIGHT squares has a black peice THEN
            elif pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) + squares) + piececoordinate[1], board) == "B":

                #Add the move to the list
                moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) + squares) + str(int(piececoordinate[1]) ))

                #END FOR
                break

            #ELSE
            else:

                #END FOR
                break

    '''DOWN'''
    #FOR squares in range the rooks height on the board
    for squares in range(int(piececoordinate[1])):

        #IF squares != 0 THEN
        if squares != 0:

            #IF the square DOWN squares is empty THEN
            if board[int(piececoordinate[1]) - squares][changeRowToDigit(piececoordinate[0])] == "  ":

                #Add the move to the list
                moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0])) + str(int(piececoordinate[1]) - squares))

            #ELSE IF the square DOWN squares has a black piece THEN
            elif pieceTeam(piececoordinate[0] + str(int(piececoordinate[1]) - squares), board) == "B":

                #Add the move to the list
                moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0])) + str(int(piececoordinate[1]) - squares))

                #END FOR
                break

            #ELSE
            else:

                #END FOR
                break

    '''LEFT'''
    #FOR squares in range right-ness of rooks location
    for squares in range(changeRowToDigit(piececoordinate[0])):

        #IF squares != 0 THEN
        if squares != 0:

            #IF the square LEFT squares is empty THEN
            if board[int(piececoordinate[1])][changeRowToDigit(piececoordinate[0]) - squares] == "  ":

                #Add the move to the list
                moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) - squares) + str(int(piececoordinate[1] )))

            #ELSE IF the square LEFT squares has a black piece THEN
            elif pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) - squares) + piececoordinate[1], board)== "B":

                #Add the move to the list
                moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) - squares) + str(int(piececoordinate[1] )))

                #END FOR
                break

            #ELSE
            else:

                #END FOR 
                break





def generateMovesKingBlack(board, moves_list, piececoordinate):# --> Adds all of the KINGS legal moves to the overall move list

    '''DOWN'''
	#IF coordinate DOWN 1 is on the board THEN 
    if onBoard(piececoordinate[0] + str(int(piececoordinate[1]) - 1)):
	
		#IF the square DOWN 1 doesn't have a black peice THEN 
        if pieceTeam(piececoordinate[0] + str(int(piececoordinate[1] - 1)), board) != "B":

            #Add the move to the list
             moves_list.append(piececoordinate + 'x' + piececoordinate[0] + str(int(piececoordinate[1]) - 1))
			 
    '''UP'''
	#IF the coordinate UP 1 is on the board THEN 
    if onBoard(piececoordinate[0] + str(int(piececoordinate[1]) + 1)):
	
		#IF the square UP 1 doesn't have a black piece THEN 
        if pieceTeam(piececoordinate[0] + str(int(piececoordinate[1]) + 1), board) != "B":

            #Add the move to the list
             moves_list.append(piececoordinate + 'x' + piececoordinate[0] + str(int(piececoordinate[1]) + 1))
			 
    '''LEFT'''
	#IF the coordinate LEFT 1 is on the board THEN 
    if onBoard(str(changeRowToDigit(piececoordinate[0]) - 1) + piececoordinate[1]):
	
		#IF the square LEFT 1 doesn't have a black piece THEN 
        if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) - 1) + piececoordinate[1], board) != "B":

            #Add the move to the list
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) - 1) + piececoordinate[1])
			
    '''RIGHT'''
	#IF the coordinate RIGHT 1 is on the board THEN 
    if onBoard(str(changeRowToDigit(piececoordinate[0]) + 1) + piececoordinate[1]):
	
		#IF the square RIGHT 1 doesn't have a black piece THEN 
        if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) + 1) + piececoordinate[1], board) != "B":

            #Add the move to the list
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) + 1) + piececoordinate[1])
			
    '''TOP RIGHT CORNER'''
	#IF the coordinate UP 1 and RIGHT 1 is on the board THEN 
    if onBoard(str(changeRowToDigit(piececoordinate[0]) + 1) + str(int(piececoordinate[1]) + 1 )):
	
		#IF the square UP 1 and RIGHT 1 doesn't have a black piece THEN 
        if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) + 1) + str(int(piececoordinate[1]) + 1 ), board) != "B":

            #Add the move to the list
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) + 1) + str(int(piececoordinate[1]) + 1))
			
    '''TOP LEFT CORNER'''
	#IF the coordinate UP 1 and LEFT 1 is on the board THEN 
    if onBoard(str(changeRowToDigit(piececoordinate[0]) - 1) + str(int(piececoordinate[1]) + 1 )):
	
		#IF the square UP 1 and LEFT 1 doesn't have a black piece THEN 
        if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) - 1) + str(int(piececoordinate[1]) + 1 ), board) != "B":

            #Add the move to the list
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) - 1) + str(int(piececoordinate[1]) + 1))
			
    '''BOTTOM LEFT CORNER'''
	#IF the coordinate DOWN 1 and LEFT 1 is on the board THEN 
    if onBoard(str(changeRowToDigit(piececoordinate[0]) - 1) + str(int(piececoordinate[1]) - 1 
	
		#IF the square DOWN 1 and LEFT 1 doesn't have a black piece THEN 
        if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) - 1) + str(int(piececoordinate[1]) - 1 ), board) != "B":

            #Add the move to the list
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) - 1) + str(int(piececoordinate[1]) - 1))
		
    '''BOTTOM RIGHT CORNER'''
	#IF the coordinate DOWN 1 and RIGHT 1 is on the board THEN 
    if onBoard(str(changeRowToDigit(piececoordinate[0]) + 1) + str(int(piececoordinate[1]) - 1 )):
	
		#IF the square DOWN 1 and RIGHT 1 doesn't have a black piece THEN 
        if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) + 1) + str(int(piececoordinate[1]) - 1 ), board) != "B":

            #Add the move to the list
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) + 1) + str(int(piececoordinate[1]) - 1))



def generateMovesKnightBlack(board, moves_list, piececoordinate):# --> Adds all of the KNIGHTS legal moves to the overall move list

    '''lEFT 2 DOWN 1'''
	#IF the coordinate LEFT 2 and DOWN 1 is on the board THEN 
    if onBoard(str(changeRowToDigit(piececoordinate[0]) - 2) + str(int(piececoordinate[1]) - 1 )):
	
		#IF the square LEFT 2 and DOWN 1 doesn't have a black piece THEN 
        if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) - 2) + str(int(piececoordinate[1]) - 1 ), board) != "B":

            #Add the move to the list
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) - 2) + str(int(piececoordinate[1]) - 1))
			
    '''RIGHT 2 DOWN 1'''
	#IF the coordinate RIGHT 2 and DOWN 1 is on the board THEN 
    if onBoard(str(changeRowToDigit(piececoordinate[0]) + 2) + str(int(piececoordinate[1]) - 1 )):
	
		#IF the square RIGHT 2 and DOWN 1 doesn't have a black piece THEN 
        if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) + 2) + str(int(piececoordinate[1]) - 1 ), board) != "B":

            #Add the move to the list
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) + 2) + str(int(piececoordinate[1]) - 1))
		
    '''LEFT 2 UP 1'''
	#IF the coordinate LEFT 2 and UP 1 is on the board THEN 
    if onBoard(str(changeRowToDigit(piececoordinate[0]) - 2) + str(int(piececoordinate[1]) + 1 )):
	
		#IF the square LEFT 2 and UP 1 doesn't have a black piece THEN 
        if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) - 2) + str(int(piececoordinate[1]) + 1 ), board) != "B":

            #Add the move to the list
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) - 2) + str(int(piececoordinate[1]) + 1
			
    '''RIGHT 2 UP 1'''
	#IF the coordinate RIGHT 2 and UP 1 is on the board THEN 
    if onBoard(str(changeRowToDigit(piececoordinate[0]) + 2) + str(int(piececoordinate[1]) + 1 )):
	
		#IF the square RIGHT 2 and UP 1 doesn't have a black piece THEN 
        if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) + 2) + str(int(piececoordinate[1]) + 1 ), board) != "B":

            #Add the move to the list
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) + 2) + str(int(piececoordinate[1]) + 1))
			
    '''DOWN 2 LEFT 1'''
	#IF the coordinate DOWN 2 and LEFT 1 is on the board THEN 
    if onBoard(str(changeRowToDigit(piececoordinate[0]) - 1) + str(int(piececoordinate[1]) - 2 )):
	
		#IF the square DOWN 2 and LEFT 1 doesn't have a black piece THEN 
        if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) - 1) + str(int(piececoordinate[1]) - 2 ), board) != "B":

            #Add the move to the list
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) - 1) + str(int(piececoordinate[1]) - 2))
			
    '''UP 2 LEFT 1'''
	#IF the coordinate UP 2 and LEFT 1 is on the board THEN 
    if onBoard(str(changeRowToDigit(piececoordinate[0]) - 1) + str(int(piececoordinate[1]) + 2 )):
	
		#IF the square UP 2 and LEFT 1 doesn't have a black piece THEN 
        if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) - 1) + str(int(piececoordinate[1]) + 2 ), board) != "B":

            #Add the move to the list
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) - 1) + str(int(piececoordinate[1]) + 2))
			
    '''DOWN 2 RIGHT 1'''
	#IF the coordinate DOWN 2 and RIGHT 1 is on the board THEN 
    if onBoard(str(changeRowToDigit(piececoordinate[0]) + 1) + str(int(piececoordinate[1]) - 2 )):
	
		#IF the square DOWN 2 and RIGHT 1 doesn't have a black piece THEN 
        if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) + 1) + str(int(piececoordinate[1]) - 2 ), board) != "B":

            #Add the move to the list
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) + 1) + str(int(piececoordinate[1]) - 2))
			
    '''UP 2 RIGHT 1'''
	#IF the coordinate UP 2 and RIGHT 1 is on the board THEN 
    if onBoard(str(changeRowToDigit(piececoordinate[0]) + 1) + str(int(piececoordinate[1]) + 2 )):
	
		#IF the square UP 2 and RIGHT 1 doesn't have a black piece THEN 
        if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) + 1) + str(int(piececoordinate[1]) + 2 ), board) != "B":

            #Add the move to the list
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) + 1) + str(int(piececoordinate[1]) + 2))



def generateMovesBishopBlack(board, moves_list, piececoordinate):# --> Adds all of the BISHOPS legal moves to the overall move list
	
	#Set count to 0 
    count = 0
	
    '''UP LEFT'''
	#WHILE the row - count is > -1 AND the column + count < 8
    while changeRowToDigit(piececoordinate[0]) - count > -1 and  int(piececoordinate[1]) + count < 8:
		
		#IF the square UP cound and LEFT count is empty THEN 
        if board[int(piececoordinate[1]) + count][changeRowToDigit(piececoordinate[0] ) - count] == "  ":

            #Add the move to the list
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) - count) + str(int(piececoordinate[1] ) + count))

            #Increment count by 1
            count+=1
		
		#ELSE IF the square UP count and LEFT count has a white piece THEN 
        elif pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0] ) - count) + str(int(piececoordinate[1]) + count), board)== "W":

            #Add the move to the list
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) - count) + str(int(piececoordinate[1] ) + count))
			
			#Reset count to 0
            count = 0
			
			#END WHILE 
            break
			
		#Reset count to 0
        count = 0
		
		#END WHILE 
        break
		
   ''' UP RIGHT ''' 
   #WHILE the row + count < 8 AND the column + count < 8
    while changeRowToDigit(piececoordinate[0]) + count < 8 and  int(piececoordinate[1]) + count < 8:
	
		#IF the square UP count and RIGHT count is empty THEN 
        if board[int(piececoordinate[1]) + count][changeRowToDigit(piececoordinate[0] ) + count] == "  ":

            #Add the move to the list
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) + count) + str(int(piececoordinate[1] ) + count))

            #Increment count by 1
            count+=1
		
		#IF the square UP count and RIGHT count has a white piece THEN 
        elif pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0] ) + count) + str(int(piececoordinate[1]) + count), board) == "W":

            #Add the move to the list
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) + count) + str(int(piececoordinate[1] ) + count))
			
			#Reset count to 0
            count = 0
			
			#END WHILE 
            break
		
		#Reset count to 0
        count = 0
		
		#END WHILE 
        break
		
    '''DOWN LEFT'''
	#WHILE row - count > -1 AND column - count > -1
    while changeRowToDigit(piececoordinate[0]) - count > -1 and  int(piececoordinate[1]) - count > -1:
		
		#IF the square DOWN count and LEFT count is empty THEN 
        if board[int(piececoordinate[1]) - count][changeRowToDigit(piececoordinate[0] ) - count] == "  ":

            #Add the move to the list
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) - count) + str(int(piececoordinate[1] ) - count))

            #Increment count by 1
            count+=1
			
		#IF the square DOWN count and LEFT count has a white piece THEN 
        elif pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0] ) - count) + str(int(piececoordinate[1]) - count), board) == "W":

            #Add the move to the list
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) - count) + str(int(piececoordinate[1] ) - count))
			
			#Reset count to 0
            count = 0
			
			#END WHILE 
            break
		
		#Reset count to 0
        count = 0
		
		#END WHILE 
        break
		
    '''DOWN RIGHT'''
	#WHILE the row + count < 8 AND the column - count > -1
    while changeRowToDigit(piececoordinate[0]) + count < 8 and  int(piececoordinate[1]) - count > -1
		
		#IF the square DOWN count and RIGHT count is empty THEN 
        if board[int(piececoordinate[1]) - count][changeRowToDigit(piececoordinate[0] ) + count] == "  ":

            #Add the move to the list
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) + count) + str(int(piececoordinate[1] ) - count))

            #Increment count by 1
            count+=1
		
		#IF the square DOWN count and RIGHT count has a white piece THEN 
        elif pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0] ) + count) + str(int(piececoordinate[1]) - count), board)== "W":

            #Add the move to the list
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) + count) + str(int(piececoordinate[1] ) - count))
			
			#Reset count to 0 
            count = 0
			
			#END WHILE 
            break
			
		#Reset count to 0 
        count = 0
		
		#END WHILE 
        break

def generateMovesRookBlack(board, moves_list, piececoordinate):# --> Adds all of the ROOKS legal moves to the overall move list

    '''UP'''
	#FOR squares in range 8 - column of rook location 
    for squares in range( 8 - int(piececoordinate[1]) ):
	
		#IF squares !=  THEN 
        if squares != 0:
		
			#IF the square UP squares is empty THEN 
            if board[int(piececoordinate[1]) + squares][changeRowToDigit(piececoordinate[0])] == "  ":

                #Add the move to the list
                moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0])) + str(int(piececoordinate[1]) + squares))
				
			#ELSE IF the square UP squares has a white piece THEN 
            elif pieceTeam(piececoordinate[0] + str(int(piececoordinate[1]) + squares), board)== "W":

                #Add the move to the list
                moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0])) + str(int(piececoordinate[1]) + squares))
				
				#END FOR 
                break
			
			#ELSE
            else:
			
				#END FOR 
                break
				
    '''RIGHT'''
	#FOR squares in range 8 - row of rook location 
    for squares in range (8 - changeRowToDigit(piececoordinate[0])):
		
		#IF squares != 0 THEN
        if squares != 0:
			
			#IF the square RIGHT squares is empty THEN 
            if board[int(piececoordinate[1])][changeRowToDigit(piececoordinate[0]) + squares] == "  ":

                #Add the move to the list
                moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) + squares) + str(int(piececoordinate[1] )))
			
			#ELSE IF the square RIGHT squares has a white piece THEN 
            elif pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) + squares) + piececoordinate[1], board) == "W":

                #Add the move to the list
                moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) + squares) + str(int(piececoordinate[1] )))
				
				#END FOR 
                break
			
			#ELSE 
            else:
			
				#END FOR 
                break
				
    '''DOWN'''
	#FOR squares in range of the rooks height 
    for squares in range(int(piececoordinate[1])):
	
		#IF squares != 0 THEN 
        if squares != 0:
		
			#IF the square DOWN squares is empty THEN 
            if board[int(piececoordinate[1]) - squares][changeRowToDigit(piececoordinate[0])] == "  ":

                #Add the move to the list
                moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0])) + str(int(piececoordinate[1]) - squares))
			
			#ELSE IF the square DOWN squares has a white white piece THEN 
            elif pieceTeam(piececoordinate[0] + str(int(piececoordinate[1]) - squares), board) == "W":

                #Add the move to the list
                moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0])) + str(int(piececoordinate[1]) - squares))
				
				#END FOR 
                break
			
			#ELSE
            else:
			
				#END FOR 
                break
				
    '''LEFT'''
	#FOR squares in range of the right-ness of rook location 
    for squares in range(changeRowToDigit(piececoordinate[0])):
	
		#IF squares != 0 THEN 
        if squares != 0:
		
			#IF the square LEFT squares is empty THEN 
            if board[int(piececoordinate[1])][changeRowToDigit(piececoordinate[0]) - squares] == "  ":

                #Add the move to the list
                moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) - squares) + str(int(piececoordinate[1] )))
				
			#ELSE IF the square LEFT square has a white piece THEN 
            elif pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) - squares) + piececoordinate[1], board)== "W":

                #Add the move to the list
                moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) - squares) + str(int(piececoordinate[1] )))
				
				#END FOR 
                break
			
			#ELSE
            else:
			
				#END FOR 
                break
