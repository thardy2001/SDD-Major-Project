from gameFunctions import *

def checkMovePawn(start_rank, start_column, end_rank, end_column, team ,start_pos, end_pos, board):
    print("start_rank:", start_rank, "start_rank as digit:",changeRankToDigit(start_rank))
    print("start_column:",start_column)
    print("end_rank:", end_rank, "end_rank as digit:",changeRankToDigit(end_rank))
    print("end_column:", end_column)
    print("team:", team)
    print("start_pos:", start_pos)
    print("end_pos:", end_pos)

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
    print(team, checkTeam(end_pos, board))
    if start_pos != end_pos:
        if abs(changeRankToDigit(start_rank) - changeRankToDigit(end_rank)) == 2 and  abs(start_column - end_column) == 1:
            if checkTeam(end_pos, board) == team:
                return False
            else:
                return True
        if abs(changeRankToDigit(start_rank) - changeRankToDigit(end_rank)) == 1 and  abs(start_column - end_column) == 2 :
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
