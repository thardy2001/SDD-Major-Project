
def checkMovePawn(start_rank, start_column, end_rank, end_column, team):
    return True

def checkMoveRook(start_rank, start_column, end_rank, end_column, team):

    if start_pos != end_pos:
        if rank_to_digit[start_rank] != rank_to_digit[end_rank] and start_column == end_column:
            if checkSquareContent(end_pos) != team:
                return True
        elif rank_to_digit[start_rank] == rank_to_digit[end_rank] and start_column != end_column:
            if checkSquareContent(end_pos) != team:
                return True


    return False


def checkMoveKnight(start_rank, start_column, end_rank, end_column, team):
    return True

def checkMoveBishop(start_rank, start_column, end_rank, end_column, team):
    return True

def checkMoveKing(start_rank, start_column, end_rank, end_column, team):
    return True

def checkMoveQueen(start_rank, start_column, end_rank, end_column, team):
    return True
