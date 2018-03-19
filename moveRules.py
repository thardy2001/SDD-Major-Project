from gameFunctions import *

def checkMovePawn(start_rank, start_column, end_rank, end_column, team ,start_pos, end_pos, board):
    return True

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
    return True

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
