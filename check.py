from gameFunctions import *
from pieceRules import *
from playerMove import *
from AI import *

def isCheck(board): # --> Tests if any king is in check, if so then returns the colour of the knig currently in check
    WK, BK = getKingCoordinates(board)
    for file in range(8):
        for rank in range(8):
            if board[file][rank] != "  ":
                starting_coordinate = changeDigitToRank(rank) + str(file)
                team = squareContent(starting_coordinate, board)

                if team == "W":
                    move = starting_coordinate + "x" + BK
                    if playerCheckMove(move, board):
                        return "B"
                elif team == "B":
                    move = starting_coordinate + "X" + WK
                    if checkMove(board, move):
                        return "W"
                else:
                    return False




def getKingCoordinates(board): # --> finds and returns the coordinates of the black and white kings
    for file in range(8):
        for rank in range(8):
            if board[file][rank] == "WK":
                coordinateWK = changeDigitToRank(rank) + str(file)
            elif board[file][rank] == "BK":
                coordinateBK = changeDigitToRank(rank) + str(file)
    return coordinateWK, coordinateBK


def testForCheck(board): # --> Tests if any piece can legal move to the coordinates of the enemy king

    #Test every square on the board
    for rank in range(len(board)):
        for cell in range(len(board[rank])):

            # If there is a piece is in the square
            if board[rank][cell] != "  ":
                start_pos = changeDigitToRank(rank) + str(cell)
                #What is the piece, type and team
                piece = board[rank][cell]
                team = piece[:1]
                piece_type = piece[1:]
                # If the piece is the black team
                if team == "B":
                    #If the piece is a Black Pawn
                    if piece_type == "P":
                        if moveRules.checkMovePawnB(changeDigitToRank(rank),cell, WK_pos_rank,WK_pos_column, start_pos, WK_pos, board):
                            return "W"
                    #If the piece is a Bishop
                    elif piece_type == "B":
                        if moveRules.checkMoveBishop(changeDigitToRank(rank),cell, WK_pos_rank,WK_pos_column, team, start_pos, WK_pos, board):
                            return "W"
                    #If the piece is a Queen
                    elif piece_type == "Q":
                        if moveRules.checkMoveQueen(changeDigitToRank(rank),cell, WK_pos_rank,WK_pos_column, team, start_pos, WK_pos, board):
                            return "W"
                    #If the piece is a King
                    elif piece_type == "K":
                        if moveRules.checkMoveKing(changeDigitToRank(rank),cell, WK_pos_rank,WK_pos_column, team, start_pos, WK_pos, board):
                            return "W"
                    #If the piece is a Knight
                    elif piece_type == "N":
                        if moveRules.checkMoveKnight(changeDigitToRank(rank),cell, WK_pos_rank,WK_pos_column, team, start_pos, WK_pos, board):
                            return "W"
                    #If the piece is a Rook
                    elif piece_type == "R":
                        if moveRules.checkMoveRook(changeDigitToRank(rank),cell, WK_pos_rank,WK_pos_column, team, start_pos, WK_pos, board):
                            return "W"
                # If it is a white piece
                else:
                    #If the piece is a Pawn
                    if piece_type == "P":
                        if moveRules.checkMovePawnW(changeDigitToRank(rank),cell, BK_pos_rank,BK_pos_column, start_pos, BK_pos, board):
                            return "B"
                    #If the piece is a Bishop
                    elif piece_type == "B":
                        if moveRules.checkMoveBishop(changeDigitToRank(rank),cell, BK_pos_rank,BK_pos_column, team, start_pos, BK_pos, board):
                            return "B"
                    #If the piece is a Queen
                    elif piece_type == "Q":
                        if moveRules.checkMoveQueen(changeDigitToRank(rank),cell, BK_pos_rank,BK_pos_column, team, start_pos, BK_pos, board):
                            return "B"
                    #If the piece is a King
                    elif piece_type == "K":
                        if moveRules.checkMoveKing(changeDigitToRank(rank),cell, BK_pos_rank,BK_pos_column, team, start_pos, BK_pos, board):
                            return "B"
                    #If the piece is a Knight
                    elif piece_type == "N":
                        if moveRules.checkMoveKnight(changeDigitToRank(rank),cell, BK_pos_rank,BK_pos_column, team, start_pos, BK_pos, board):
                            return "B"
                    #If the piece is a Rook
                    elif piece_type == "R":
                        if moveRules.checkMoveRook(changeDigitToRank(rank),cell, BK_pos_rank,BK_pos_column, team, start_pos, BK_pos, board):
                            return "B"
