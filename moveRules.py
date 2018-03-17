from  Main import checkSquareContent
def checkMovePawn(start_rank, start_column, end_rank, end_column, team ,start_pos, end_pos):
    return True

def checkMoveRook(start_rank, start_column, end_rank, end_column, team, start_pos, end_pos):

    if start_pos != end_pos:
        if changeRankToDigit(start_rank) != changeRankToDigit(end_rank) and start_column == end_column:
            if checkSquareContent(end_pos) != team:
                return True
        elif changeRankToDigit(start_rank) == changeRankToDigit(end_rank) and start_column != end_column:
            if checkSquareContent(end_pos) != team:
                return True


    return False


def checkMoveKnight(start_rank, start_column, end_rank, end_column, team,start_pos, end_pos):
    return True

def checkMoveBishop(start_rank, start_column, end_rank, end_column, team,start_pos, end_pos):
    return True

def checkMoveKing(start_rank, start_column, end_rank, end_column, team,start_pos, end_pos):
    return True

def checkMoveQueen(start_rank, start_column, end_rank, end_column, team,start_pos, end_pos):
    if checkMoveRook(start_rank, start_column, end_rank, end_column, team,start_pos, end_pos):
        return True
    elif checkMoveBishop(start_rank, start_column, end_rank, end_column, team,start_pos, end_pos):
        return True
    return False
