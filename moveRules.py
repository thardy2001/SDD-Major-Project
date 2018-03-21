from gameFunctions import *

def checkMovePawn(start_rank, start_column, end_rank, end_column, team ,start_pos, end_pos, board):
    if team == "W":
        if changeRankToDigit(start_rank) == 1:
            if changeRankToDigit(end_rank)- changeRankToDigit(start_rank) == 2 and board[changeRankToDigit(end_rank)][end_column] == "  " and abs(start_column - end_column) == 0 or changeRankToDigit(end_rank)- changeRankToDigit(start_rank) == 1 and board[changeRankToDigit(end_rank)][end_column] == "  " and abs(start_column - end_column) == 0:
                return True
            elif changeRankToDigit(end_rank)- changeRankToDigit(start_rank) == 1 and checkTeam(end_pos, board) == "B" and abs(start_column - end_column) == 1:
                return True

        elif changeRankToDigit(start_rank) != 1:
            if changeRankToDigit(end_rank)- changeRankToDigit(start_rank) == 1 and board[changeRankToDigit(end_rank)][end_column] == "  " and abs(start_column - end_column) == 0:
                return True
            elif changeRankToDigit(end_rank)- changeRankToDigit(start_rank) == 1 and checkTeam(end_pos, board) == "B" and abs(start_column - end_column) == 1:
                return True
    elif team == "B":
        if changeRankToDigit(start_rank) == 6:
            if changeRankToDigit(end_rank)- changeRankToDigit(start_rank) == -2 and board[changeRankToDigit(end_rank)][end_column] == "  " and abs(start_column - end_column) == 0 or changeRankToDigit(end_rank)- changeRankToDigit(start_rank) == -1 and board[changeRankToDigit(end_rank)][end_column] == "  " and abs(start_column - end_column) == 0:
                return True
            elif changeRankToDigit(end_rank)- changeRankToDigit(start_rank) == -1 and checkTeam(end_pos, board) == "W" and abs(start_column - end_column) == 1:
                return True

        elif changeRankToDigit(start_rank) != 6 :
            if changeRankToDigit(end_rank)- changeRankToDigit(start_rank) == -1 and board[changeRankToDigit(end_rank)][end_column] == "  " and abs(start_column - end_column) == 0:
                return True
            elif changeRankToDigit(end_rank)- changeRankToDigit(start_rank) == -1 and checkTeam(end_pos, board) == "W" and abs(start_column - end_column) == 1:
                return True
    else:
        return False
    return False

def checkMoveRook(start_rank, start_column, end_rank, end_column, team, start_pos, end_pos, board):

    if start_pos != end_pos:
        if changeRankToDigit(start_rank) != changeRankToDigit(end_rank) and start_column == end_column:
            if checkTeam(end_pos, board) != team:
                return True
        elif changeRankToDigit(start_rank) == changeRankToDigit(end_rank) and start_column != end_column:
            if checkTeam(end_pos, board) != team:
                return True


    return False


def checkMoveKnight(start_rank, start_column, end_rank, end_column, team,start_pos, end_pos, board):

    if abs(changeRankToDigit(start_rank) - changeRankToDigit(end_rank)) == 2 and  abs(start_column - end_column) == 1  or abs(changeRankToDigit(start_rank) - changeRankToDigit(end_rank)) == 1 and  abs(start_column - end_column) == 2 :
        print("The piece in the square:",end_rank, end_column, board[changeRankToDigit(end_rank)][end_column][:1])
        if checkTeam(end_pos, board) == team:
            return False
        else:
            return True
    else:
        return False
    return False
def checkMoveBishop(start_rank, start_column, end_rank, end_column, team,start_pos, end_pos, board):
    if start_pos != end_pos:
        if abs(changeRankToDigit(start_rank) - changeRankToDigit(end_rank)) == abs(start_column - end_column):
            if checkTeam(end_pos, board) != team:
                return True
    return False

def checkMoveKing(start_rank, start_column, end_rank, end_column, team,start_pos, end_pos, board):
    if start_pos != end_pos:
        if abs(changeRankToDigit(start_rank) - changeRankToDigit(end_rank)) == 1 or abs(start_column - end_column) == 1 or abs(changeRankToDigit(start_rank) - changeRankToDigit(end_rank)) == 1 and abs(start_column - end_column) == 1 :
            if checkTeam(end_pos, board) != team:
                return True
    return False

def checkMoveQueen(start_rank, start_column, end_rank, end_column, team,start_pos, end_pos, board):
    if checkMoveRook(start_rank, start_column, end_rank, end_column, team,start_pos, end_pos, board):
        return True
    elif checkMoveBishop(start_rank, start_column, end_rank, end_column, team,start_pos, end_pos, board):
        return True
    return False
