


def changeRankToDigit(rank):
    """
    Changes a specific rank into a digit, beginning at 0
    e.g.
    A => 0,
    B => 1,
    """
    conversion = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7,
    'I': 8,
    'J': 9,
    'K': 10,
    'L': 11,
    'M': 12,
    'N': 13,
    'O': 14,
    'P': 15,
    'Q':16,
    'R':17,
    'S':18,
    'T':19,
    'U':20,
    'V':21,
    'W':22,
    'X':23,
    'Y':24,
    'Z':25
    }
    digit = conversion[rank.upper()]
    return digit

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
