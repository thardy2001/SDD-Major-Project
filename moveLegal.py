from generalFunctions import *

def generateMoveList(board, startingCoordinates, team):
    moves_list = []
    for item in range(len(startingCoordinates)):
        piececoordinate = startingCoordinates[item]

        piece = board[int(piececoordinate[1])][changeRowToDigit(piececoordinate[0])]
        piece_type = piece[1]

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


def generateMovesPawnWhite(board, moves_list, piececoordinate):
    #IF the pawn is moving one up AND the square is empty THEN
    if board[int(piececoordinate[1]) + 1][changeRowToDigit(piececoordinate[0])] == "  ":

        moves_list.append(piececoordinate + 'x' + piececoordinate[0] + str(int(piececoordinate[1]) + 1))
    #IF the pawn is moving up 2 AND both the square infront of the piece and ending destination are empty AND the pawn has yet to move THEN
    if board[int(piececoordinate[1]) + 2][changeRowToDigit(piececoordinate[0])] == "  " and board[int(piececoordinate[1]) + 1][changeRowToDigit(piececoordinate[0])] == "  " and int(piececoordinate[1]) == 1:

        moves_list.append(piececoordinate + 'x' + piececoordinate[0] + str(int(piececoordinate[1]) + 2))
    #IF the pawn is moving up one and across one AND the destination square has a black piece THEN
    if onBoard(str(changeRowToDigit(piececoordinate[0]) + 1) + str(int(piececoordinate[1]) + 1)):
        if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) + 1) +str(int(piececoordinate[1]) + 1), board) == "B":

            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) + 1) + str(int(piececoordinate[1]) + 1))
    #IF the pawn is moving up one and across one AND the destination square has a black piece THEN
    if onBoard(str(changeRowToDigit(piececoordinate[0]) - 1)+ str(int(piececoordinate[1]) + 1)):
        if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) - 1)+ str(int(piececoordinate[1]) + 1), board) == "B":

            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) - 1) + str(int(piececoordinate[1]) + 1))



def generateMovesPawnBlack(board, moves_list, piececoordinate):
    #IF the pawn is moving one up AND the square is empty THEN
    if board[int(piececoordinate[1]) - 1][changeRowToDigit(piececoordinate[0])] == "  ":

        moves_list.append(piececoordinate + 'x' + piececoordinate[0] + str(int(piececoordinate[1]) - 1))
    #IF the pawn is moving up 2 AND both the square infront of the piece and ending destination are empty AND the pawn has yet to move THEN
    if board[int(piececoordinate[1]) - 2][changeRowToDigit(piececoordinate[0])] == "  " and board[int(piececoordinate[1]) - 1][changeRowToDigit(piececoordinate[0])] == "  " and int(piececoordinate[1]) == 6:

        moves_list.append(piececoordinate + 'x' + piececoordinate[0] + str(int(piececoordinate[1]) - 2))
    #IF the pawn is moving up one and across one AND the destination square has a black piece THEN
    if onBoard(str(changeRowToDigit(piececoordinate[0]) + 1) + str(int(piececoordinate[1]) - 1)):
        if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) + 1) +str(int(piececoordinate[1]) - 1), board) == "W":

            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) + 1) + str(int(piececoordinate[1]) - 1))
    #IF the pawn is moving up one and across one AND the destination square has a black piece THEN
    if onBoard(str(changeRowToDigit(piececoordinate[0]) - 1)+ str(int(piececoordinate[1]) + 1)):
        if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) - 1)+ str(int(piececoordinate[1]) + 1), board) == "W":

            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) - 1) + str(int(piececoordinate[1]) - 1))

def generateMovesKingWhite(board, moves_list, piececoordinate):
    #DOWN
    if onBoard(piececoordinate[0] + str(int(piececoordinate[1]) - 1)):
        if pieceTeam(piececoordinate[0] + str(int(piececoordinate[1] - 1)), board) != "W":
             moves_list.append(piececoordinate + 'x' + piececoordinate[0] + str(int(piececoordinate[1]) - 1))
    #UP
    if onBoard(piececoordinate[0] + str(int(piececoordinate[1]) + 1)):
        if pieceTeam(piececoordinate[0] + str(int(piececoordinate[1]) + 1), board) != "W":
             moves_list.append(piececoordinate + 'x' + piececoordinate[0] + str(int(piececoordinate[1]) + 1))
    #LEFT
    if onBoard(str(changeRowToDigit(piececoordinate[0]) - 1) + piececoordinate[1]):
        if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) - 1) + piececoordinate[1], board) != "W":
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) - 1) + piececoordinate[1])
    #RIGHT
    if onBoard(str(changeRowToDigit(piececoordinate[0]) + 1) + piececoordinate[1]):
        if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) + 1) + piececoordinate[1], board) != "W":
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) + 1) + piececoordinate[1])
    #TOP RIGHT CORNER
    if onBoard(str(changeRowToDigit(piececoordinate[0]) + 1) + str(int(piececoordinate[1]) + 1 )):
        if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) + 1) + str(int(piececoordinate[1]) + 1 ), board) != "W":
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) + 1) + str(int(piececoordinate[1]) + 1))
    #TOP LEFT CORNER
    if onBoard(str(changeRowToDigit(piececoordinate[0]) - 1) + str(int(piececoordinate[1]) + 1 )):
        if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) - 1) + str(int(piececoordinate[1]) + 1 ), board) != "W":
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) - 1) + str(int(piececoordinate[1]) + 1))
    # BOTTOM LEFT CORNER
    if onBoard(str(changeRowToDigit(piececoordinate[0]) - 1) + str(int(piececoordinate[1]) - 1 )):
        if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) - 1) + str(int(piececoordinate[1]) - 1 ), board) != "W":
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) - 1) + str(int(piececoordinate[1]) - 1))
    #BOTTOM RIGHT CORNER
    if onBoard(str(changeRowToDigit(piececoordinate[0]) + 1) + str(int(piececoordinate[1]) - 1 )):
        if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) + 1) + str(int(piececoordinate[1]) - 1 ), board) != "W":
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) + 1) + str(int(piececoordinate[1]) - 1))



def generateMovesKnightWhite(board, moves_list, piececoordinate):

    #lEFT 2 DOWN 1
    if onBoard(str(changeRowToDigit(piececoordinate[0]) - 2) + str(int(piececoordinate[1]) - 1 )):
        if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) - 2) + str(int(piececoordinate[1]) - 1 ), board) != "W":
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) - 2) + str(int(piececoordinate[1]) - 1))
    #RIGHT 2 DOWN 1
    if onBoard(str(changeRowToDigit(piececoordinate[0]) + 2) + str(int(piececoordinate[1]) - 1 )):
        if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) + 2) + str(int(piececoordinate[1]) - 1 ), board) != "W":
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) + 2) + str(int(piececoordinate[1]) - 1))
    #LEFT 2 UP 1
    if onBoard(str(changeRowToDigit(piececoordinate[0]) - 2) + str(int(piececoordinate[1]) + 1 )):
        if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) - 2) + str(int(piececoordinate[1]) + 1 ), board) != "W":
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) - 2) + str(int(piececoordinate[1]) + 1))
    #RIGHT 2 UP 1
    if onBoard(str(changeRowToDigit(piececoordinate[0]) + 2) + str(int(piececoordinate[1]) + 1 )):
        if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) + 2) + str(int(piececoordinate[1]) + 1 ), board) != "W":
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) + 2) + str(int(piececoordinate[1]) + 1))
    #DOWN 2 LEFT 1
    if onBoard(str(changeRowToDigit(piececoordinate[0]) - 1) + str(int(piececoordinate[1]) - 2 )):
        if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) - 1) + str(int(piececoordinate[1]) - 2 ), board) != "W":
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) - 1) + str(int(piececoordinate[1]) - 2))
    #UP 2 LEFT 1
    if onBoard(str(changeRowToDigit(piececoordinate[0]) - 1) + str(int(piececoordinate[1]) + 2 )):
        if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) - 1) + str(int(piececoordinate[1]) + 2 ), board) != "W":
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) - 1) + str(int(piececoordinate[1]) + 2))
    #DOWN 2 RIGHT 1
    if onBoard(str(changeRowToDigit(piececoordinate[0]) + 1) + str(int(piececoordinate[1]) - 2 )):
        if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) + 1) + str(int(piececoordinate[1]) - 2 ), board) != "W":
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) + 1) + str(int(piececoordinate[1]) - 2))
    #UP 2 RIGHT 1
    if onBoard(str(changeRowToDigit(piececoordinate[0]) + 1) + str(int(piececoordinate[1]) + 2 )):
        if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) + 1) + str(int(piececoordinate[1]) + 2 ), board) != "W":
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) + 1) + str(int(piececoordinate[1]) + 2))



def generateMovesBishopWhite(board, moves_list, piececoordinate):

    count = 0
    #UP LEFT
    while changeRowToDigit(piececoordinate[0]) - count > -1 and  int(piececoordinate[1]) + count < 8:
        if board[int(piececoordinate[1]) + count][changeRowToDigit(piececoordinate[0] ) - count] == "  ":
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) - count) + str(int(piececoordinate[1] ) + count))
            count+=1
        elif pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0] ) - count) + str(int(piececoordinate[1]) + count), board)== "B":
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) - count) + str(int(piececoordinate[1] ) + count))
            count = 0
            break
        count = 0
        break
    #UP RIGHT
    while changeRowToDigit(piececoordinate[0]) + count < 8 and  int(piececoordinate[1]) + count < 8:
        if board[int(piececoordinate[1]) + count][changeRowToDigit(piececoordinate[0] ) + count] == "  ":
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) + count) + str(int(piececoordinate[1] ) + count))
            count+=1
        elif pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0] ) + count) + str(int(piececoordinate[1]) + count), board) == "B":
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) + count) + str(int(piececoordinate[1] ) + count))
            count = 0
            break
        count = 0
        break
    #DOWN LEFT
    while changeRowToDigit(piececoordinate[0]) - count > -1 and  int(piececoordinate[1]) - count > -1:
        if board[int(piececoordinate[1]) - count][changeRowToDigit(piececoordinate[0] ) - count] == "  ":
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) - count) + str(int(piececoordinate[1] ) - count))
            count+=1
        elif pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0] ) - count) + str(int(piececoordinate[1]) - count), board) == "B":
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) - count) + str(int(piececoordinate[1] ) - count))
            count = 0
            break
        count = 0
        break
    #DOWN RIGHT
    while changeRowToDigit(piececoordinate[0]) + count < 8 and  int(piececoordinate[1]) - count > -1:
        if board[int(piececoordinate[1]) - count][changeRowToDigit(piececoordinate[0] ) + count] == "  ":
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) + count) + str(int(piececoordinate[1] ) - count))
            count+=1
        elif pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0] ) + count) + str(int(piececoordinate[1]) - count), board)== "B":
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) + count) + str(int(piececoordinate[1] ) - count))
            count = 0
            break
        count = 0
        break

    return moves_list
def generateMovesRookWhite(board, moves_list, piececoordinate):
    #UP
    for squares in range( 8 - int(piececoordinate[1]) ):
        if squares != 0:
            if board[int(piececoordinate[1]) + squares][changeRowToDigit(piececoordinate[0])] == "  ":
                moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0])) + str(int(piececoordinate[1]) + squares))
            elif pieceTeam(piececoordinate[0] + str(int(piececoordinate[1]) + squares), board)== "B":
                moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0])) + str(int(piececoordinate[1]) + squares))
                break
            else:
                break
    #RIGHT
    for squares in range (8 - changeRowToDigit(piececoordinate[0])):
        if squares != 0:
            if board[int(piececoordinate[1])][changeRowToDigit(piececoordinate[0]) + squares] == "  ":
                moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) + squares) + str(int(piececoordinate[1]) ))
            elif pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) + squares) + piececoordinate[1], board) == "B":
                moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) + squares) + str(int(piececoordinate[1]) ))
                break
            else:
                break
    #DOWN
    for squares in range(int(piececoordinate[1])):
        if squares != 0:
            if board[int(piececoordinate[1]) - squares][changeRowToDigit(piececoordinate[0])] == "  ":
                moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0])) + str(int(piececoordinate[1]) - squares))
            elif pieceTeam(piececoordinate[0] + str(int(piececoordinate[1]) - squares), board) == "B":
                moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0])) + str(int(piececoordinate[1]) - squares))
                break
            else:
                break
    #LEFT
    for squares in range(changeRowToDigit(piececoordinate[0])):
        if squares != 0:
            if board[int(piececoordinate[1])][changeRowToDigit(piececoordinate[0]) - squares] == "  ":
                moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) - squares) + str(int(piececoordinate[1] )))
            elif pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) - squares) + piececoordinate[1], board)== "B":
                moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) - squares) + str(int(piececoordinate[1] )))
                break
            else:
                break





def generateMovesKingBlack(board, moves_list, piececoordinate):
    #DOWN
    if onBoard(piececoordinate[0] + str(int(piececoordinate[1]) - 1)):
        if pieceTeam(piececoordinate[0] + str(int(piececoordinate[1] - 1)), board) != "B":
             moves_list.append(piececoordinate + 'x' + piececoordinate[0] + str(int(piececoordinate[1]) - 1))
    #UP
    if onBoard(piececoordinate[0] + str(int(piececoordinate[1]) + 1)):
        if pieceTeam(piececoordinate[0] + str(int(piececoordinate[1]) + 1), board) != "B":
             moves_list.append(piececoordinate + 'x' + piececoordinate[0] + str(int(piececoordinate[1]) + 1))
    #LEFT
    if onBoard(str(changeRowToDigit(piececoordinate[0]) - 1) + piececoordinate[1]):
        if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) - 1) + piececoordinate[1], board) != "B":
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) - 1) + piececoordinate[1])
    #RIGHT
    if onBoard(str(changeRowToDigit(piececoordinate[0]) + 1) + piececoordinate[1]):
        if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) + 1) + piececoordinate[1], board) != "B":
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) + 1) + piececoordinate[1])
    #TOP RIGHT CORNER
    if onBoard(str(changeRowToDigit(piececoordinate[0]) + 1) + str(int(piececoordinate[1]) + 1 )):
        if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) + 1) + str(int(piececoordinate[1]) + 1 ), board) != "B":
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) + 1) + str(int(piececoordinate[1]) + 1))
    #TOP LEFT CORNER
    if onBoard(str(changeRowToDigit(piececoordinate[0]) - 1) + str(int(piececoordinate[1]) + 1 )):
        if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) - 1) + str(int(piececoordinate[1]) + 1 ), board) != "B":
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) - 1) + str(int(piececoordinate[1]) + 1))
    # BOTTOM LEFT CORNER
    if onBoard(str(changeRowToDigit(piececoordinate[0]) - 1) + str(int(piececoordinate[1]) - 1 )):
        if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) - 1) + str(int(piececoordinate[1]) - 1 ), board) != "B":
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) - 1) + str(int(piececoordinate[1]) - 1))
    #BOTTOM RIGHT CORNER
    if onBoard(str(changeRowToDigit(piececoordinate[0]) + 1) + str(int(piececoordinate[1]) - 1 )):
        if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) + 1) + str(int(piececoordinate[1]) - 1 ), board) != "B":
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) + 1) + str(int(piececoordinate[1]) - 1))



def generateMovesKnightBlack(board, moves_list, piececoordinate):

    #lEFT 2 DOWN 1
    if onBoard(str(changeRowToDigit(piececoordinate[0]) - 2) + str(int(piececoordinate[1]) - 1 )):
        if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) - 2) + str(int(piececoordinate[1]) - 1 ), board) != "B":
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) - 2) + str(int(piececoordinate[1]) - 1))
    #RIGHT 2 DOWN 1
    if onBoard(str(changeRowToDigit(piececoordinate[0]) + 2) + str(int(piececoordinate[1]) - 1 )):
        if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) + 2) + str(int(piececoordinate[1]) - 1 ), board) != "B":
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) + 2) + str(int(piececoordinate[1]) - 1))
    #LEFT 2 UP 1
    if onBoard(str(changeRowToDigit(piececoordinate[0]) - 2) + str(int(piececoordinate[1]) + 1 )):
        if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) - 2) + str(int(piececoordinate[1]) + 1 ), board) != "B":
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) - 2) + str(int(piececoordinate[1]) + 1))
    #RIGHT 2 UP 1
    if onBoard(str(changeRowToDigit(piececoordinate[0]) + 2) + str(int(piececoordinate[1]) + 1 )):
        if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) + 2) + str(int(piececoordinate[1]) + 1 ), board) != "B":
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) + 2) + str(int(piececoordinate[1]) + 1))
    #DOWN 2 LEFT 1
    if onBoard(str(changeRowToDigit(piececoordinate[0]) - 1) + str(int(piececoordinate[1]) - 2 )):
        if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) - 1) + str(int(piececoordinate[1]) - 2 ), board) != "B":
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) - 1) + str(int(piececoordinate[1]) - 2))
    #UP 2 LEFT 1
    if onBoard(str(changeRowToDigit(piececoordinate[0]) - 1) + str(int(piececoordinate[1]) + 2 )):
        if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) - 1) + str(int(piececoordinate[1]) + 2 ), board) != "B":
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) - 1) + str(int(piececoordinate[1]) + 2))
    #DOWN 2 RIGHT 1
    if onBoard(str(changeRowToDigit(piececoordinate[0]) + 1) + str(int(piececoordinate[1]) - 2 )):
        if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) + 1) + str(int(piececoordinate[1]) - 2 ), board) != "B":
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) + 1) + str(int(piececoordinate[1]) - 2))
    #UP 2 RIGHT 1
    if onBoard(str(changeRowToDigit(piececoordinate[0]) + 1) + str(int(piececoordinate[1]) + 2 )):
        if pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) + 1) + str(int(piececoordinate[1]) + 2 ), board) != "B":
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) + 1) + str(int(piececoordinate[1]) + 2))



def generateMovesBishopBlack(board, moves_list, piececoordinate):

    count = 0
    #UP LEFT
    while changeRowToDigit(piececoordinate[0]) - count > -1 and  int(piececoordinate[1]) + count < 8:
        if board[int(piececoordinate[1]) + count][changeRowToDigit(piececoordinate[0] ) - count] == "  ":
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) - count) + str(int(piececoordinate[1] ) + count))
            count+=1
        elif pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0] ) - count) + str(int(piececoordinate[1]) + count), board)== "W":
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) - count) + str(int(piececoordinate[1] ) + count))
            count = 0
            break
        count = 0
        break
    #UP RIGHT
    while changeRowToDigit(piececoordinate[0]) + count < 8 and  int(piececoordinate[1]) + count < 8:
        if board[int(piececoordinate[1]) + count][changeRowToDigit(piececoordinate[0] ) + count] == "  ":
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) + count) + str(int(piececoordinate[1] ) + count))
            count+=1
        elif pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0] ) + count) + str(int(piececoordinate[1]) + count), board) == "W":
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) + count) + str(int(piececoordinate[1] ) + count))
            count = 0
            break
        count = 0
        break
    #DOWN LEFT
    while changeRowToDigit(piececoordinate[0]) - count > -1 and  int(piececoordinate[1]) - count > -1:
        if board[int(piececoordinate[1]) - count][changeRowToDigit(piececoordinate[0] ) - count] == "  ":
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) - count) + str(int(piececoordinate[1] ) - count))
            count+=1
        elif pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0] ) - count) + str(int(piececoordinate[1]) - count), board) == "W":
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) - count) + str(int(piececoordinate[1] ) - count))
            count = 0
            break
        count = 0
        break
    #DOWN RIGHT
    while changeRowToDigit(piececoordinate[0]) + count < 8 and  int(piececoordinate[1]) - count > -1:
        if board[int(piececoordinate[1]) - count][changeRowToDigit(piececoordinate[0] ) + count] == "  ":
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) + count) + str(int(piececoordinate[1] ) - count))
            count+=1
        elif pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0] ) + count) + str(int(piececoordinate[1]) - count), board)== "W":
            moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) + count) + str(int(piececoordinate[1] ) - count))
            count = 0
            break
        count = 0
        break

def generateMovesRookBlack(board, moves_list, piececoordinate):
    #UP
    for squares in range( 8 - int(piececoordinate[1]) ):
        if squares != 0:
            if board[int(piececoordinate[1]) + squares][changeRowToDigit(piececoordinate[0])] == "  ":
                moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0])) + str(int(piececoordinate[1] + squares)))
            elif pieceTeam(piececoordinate[0] + str(int(piececoordinate[1]) + squares), board)== "W":
                moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0])) + str(int(piececoordinate[1] + squares)))
                break
            else:
                break
    #RIGHT
    for squares in range (8 - changeRowToDigit(piececoordinate[0])):
        if squares != 0:
            if board[int(piececoordinate[1])][changeRowToDigit(piececoordinate[0]) + squares] == "  ":
                moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) + squares) + str(int(piececoordinate[1] )))
            elif pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) + squares) + piececoordinate[1], board) == "W":
                moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) + squares) + str(int(piececoordinate[1] )))
                break
            else:
                break
    #DOWN
    for squares in range(int(piececoordinate[1])):
        if squares != 0:
            if board[int(piececoordinate[1]) - squares][changeRowToDigit(piececoordinate[0])] == "  ":
                moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0])) + str(int(piececoordinate[1]) - squares))
            elif pieceTeam(piececoordinate[0] + str(int(piececoordinate[1]) - squares), board) == "W":
                moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0])) + str(int(piececoordinate[1]) - squares))
                break
            else:
                break
    #LEFT
    for squares in range(changeRowToDigit(piececoordinate[0])):
        if squares != 0:
            if board[int(piececoordinate[1])][changeRowToDigit(piececoordinate[0]) - squares] == "  ":
                moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) - squares) + str(int(piececoordinate[1] )))
            elif pieceTeam(changeDigitToRow(changeRowToDigit(piececoordinate[0]) - squares) + piececoordinate[1], board)== "W":
                moves_list.append(piececoordinate + 'x' + changeDigitToRow(changeRowToDigit(piececoordinate[0]) - squares) + str(int(piececoordinate[1] )))
                break
            else:
                break
