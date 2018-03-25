from gameFunctions import *

def checkMovePawn(start_rank, start_column, end_rank, end_column, team ,start_pos, end_pos, board):
    return False
'''
    if team == "W":
        if start_pos != end_pos:
            if start_rank == "B":
                if changeRankToDigit(end_rank) - changeRankToDigit(start_rank) == 2 and board[changeRankToDigit(end_rank)][end_column] == "  " and start_column - end_column == 0:
                    return True
                elif changeRankToDigit(end_rank) - changeRankToDigit(start_rank) == 1 and board[changeRankToDigit(end_rank)][end_column] == "  " and start_column - end_column == 0:
                    return True
                elif changeRankToDigit(end_rank) - changeRankToDigit(start_rank) == 1 and checkTeam(end_pos,board) == "B" and abs(start_column - end_column) == 1:
                    return True
            if start_rank != "B":
                if changeRankToDigit(end_rank) - changeRankToDigit(start_rank) == 1 and board[changeRankToDigit(end_rank)][end_column] == "  " and start_column - end_column == 0:
                    return True
                elif changeRankToDigit(end_rank) - changeRankToDigit(start_rank) == 1 and checkTeam(end_pos,board) == "B" and abs(start_column - end_column) == 1:
                    return True

    if team == "B":
        if start_pos != end_pos:
            if start_rank == "G":
                if changeRankToDigit(start_rank) - changeRankToDigit(end_rank) == 2 and board[7-changeRankToDigit(end_rank)][end_column] == "  " and start_column - end_column == 0:
                    return True
                elif changeRankToDigit(start_rank) - changeRankToDigit(end_rank) == 1 and board[7-changeRankToDigit(end_rank)][end_column] == "  " and start_column - end_column == 0:
                    return True
                elif changeRankToDigit(start_rank) - changeRankToDigit(end_rank) == 1 and checkTeam(end_pos,board) == "W" and abs(start_column - end_column) == 1:
                    return True
            if start_rank != "G":
                if changeRankToDigit(start_rank) - changeRankToDigit(end_rank) == 1 and board[7-changeRankToDigit(end_rank)][end_column] == "  " and start_column - end_column == 0:
                    return True
                elif changeRankToDigit(start_rank) - changeRankToDigit(end_rank) == 1 and checkTeam(end_pos,board) == "W" and abs(start_column - end_column) == 1:
                    return True

        return False
'''

def checkMoveRook(start_rank, start_column, end_rank, end_column, team, start_pos, end_pos, board):
    # If the piece has acctually moved
    if start_pos != end_pos:
        # If the rank has stayed the same but column has changed (horazontal straight line)
        if changeRankToDigit(start_rank) != changeRankToDigit(end_rank) and start_column == end_column:
            # Does the square contatain a friendly piece
            if checkTeam(end_pos, board) != team:
                return True
        #If there is a change in rank but the column is the same (vertical straight line)
        elif changeRankToDigit(start_rank) == changeRankToDigit(end_rank) and start_column != end_column:
            # Does the square contain a friendly piece
            if checkTeam(end_pos, board) != team:
                return True


    return False


def checkMoveKnight(start_rank, start_column, end_rank, end_column, team,start_pos, end_pos, board):

    #Has the piece changed Position?
    if start_pos != end_pos:
        # Is the new square up / down 2 squares and across 1 square (L shape)
        if abs(changeRankToDigit(start_rank) - changeRankToDigit(end_rank)) == 2 and  abs(start_column - end_column) == 1:
            # Does the square contain a friendly piece
            if checkTeam(end_pos, board) == team:
                return False
            else:
                return True
        # is the destination square up / down one square and across 2 squares from the starting position (L shape)
        if abs(changeRankToDigit(start_rank) - changeRankToDigit(end_rank)) == 1 and  abs(start_column - end_column) == 2 :
            # Does the destination contatin a firendly piece ?
            if checkTeam(end_pos, board) == team:
                return False
            else:
                return True
        else:
            return False

    return False

def checkMoveBishop(start_rank, start_column, end_rank, end_column, team,start_pos, end_pos, board):
    # has the piece moved ?
    if start_pos != end_pos:
        # Is the change in x coordinate the same as the change in y coordinate ? (Diagonal movement)
        if abs(changeRankToDigit(start_rank) - changeRankToDigit(end_rank)) == abs(start_column - end_column):
            # Does the square contatain a friendly piece ?
            if checkTeam(end_pos, board) != team:
                return True
    return False

def checkMoveKing(start_rank, start_column, end_rank, end_column, team,start_pos, end_pos, board):
    # Has the piece moved ?
    if start_pos != end_pos:
        # Is the end position adjacent to the starting position ? (1 square away vertically, horazontally or diagonally)
        if abs(changeRankToDigit(start_rank) - changeRankToDigit(end_rank)) == 1 or abs(start_column - end_column) == 1 or abs(changeRankToDigit(start_rank) - changeRankToDigit(end_rank)) == 1 and abs(start_column - end_column) == 1 :
            if checkTeam(end_pos, board) != team:
                return True
    return False

def checkMoveQueen(start_rank, start_column, end_rank, end_column, team,start_pos, end_pos, board):
    # Is the move legal by rook standard rules ?
    if checkMoveRook(start_rank, start_column, end_rank, end_column, team,start_pos, end_pos, board):
        return True
    # Is the move legal by normal bishop rules ?
    elif checkMoveBishop(start_rank, start_column, end_rank, end_column, team,start_pos, end_pos, board):
        return True
    return False
