from gameFunctions import *

def checkMovePawnW(start_rank, start_column, end_rank, end_column,start_pos, end_pos, board): # Returns True or false based on the legality of a move
    start_column = int(start_column)
    end_column = int(end_column)

    start_rank = changeRankToDigit(start_rank)
    end_rank = changeRankToDigit(end_rank)
    print("Start Rank:", start_rank)
    print("End Rank:", end_rank)
    print("Start Column:", start_column)
    print("End Column:", end_column)
    #IF starting position is different to ending position THEN
    if start_pos != end_pos:
        #IF the piece starting location is on rank B THEN
        if start_rank == "B" or start_rank == 2:
            #IF change in rank == 2 AND change in column == 0 AND end squre is empty OR change in rank == 1 AND change in column == 0 AND end squre is empty THEN
            if end_rank - start_rank == 2 and end_column - start_column == 0 and board[end_rank][end_column] == "  " or end_rank - start_rank == 1 and end_column - start_column == 0 and board[end_rank][end_column] == "  ":
                #the move is legal
                return True
            #ELSE IF change in rank == 1 AND change in column == 1 AND end square contains an enemy piece THEN
            elif end_rank - start_rank == 1 and abs(end_column - start_column) == 1 and board[end_rank][end_column][:1] == "B":
                #the move is legal
                return True
        #ELSE THEN
        else:
            #IF change in rank == 1 AND chagne in column == 0 AND end square is empty THEN
            if end_rank - start_rank == 1 and start_column - end_column == 0 and board[end_rank][end_column] == "  ":
                #the move is legal
                return True
            #ELSE IF change in rank == 1 AND change in column == 1 AND end square has an enemy piece THEN
            elif end_rank - start_rank == 1 and abs(end_column - start_column) == 1 and board[end_rank][end_column][:1] == "B":
                #the move is legal
                return True

    return False

def checkMovePawnB(start_rank, start_column, end_rank, end_column,start_pos, end_pos, board):# Returns True or false based on the legality of a move
    start_column = int(start_column)
    end_column = int(end_column)

    start_rank = changeRankToDigit(start_rank)
    end_rank = changeRankToDigit(end_rank)
    #IF starting position is different to ending position THEN
    if start_pos != end_pos:
        #IF the piece starting location is on rank G THEN
        if start_rank == "G" or 6:
            #IF change in rank == -2 AND change in column == 0 AND end squre is empty OR change in rank == -1 AND change in column == 0 AND end squre is empty THEN
            if end_rank - start_rank == -2 and end_column - start_column == 0 and board[end_rank][end_column] == "  " or end_rank - start_rank == -1 and end_column - start_column == 0 and board[end_rank][end_column] == "  ":
                #the move is legal
                return True
            #ELSE IF change in rank == -1 AND change in column == 1 AND end square contains an enemy piece THEN
            elif end_rank - start_rank == -1 and abs(end_column - start_column) == 1 and board[end_rank][end_column][:1] == "W":
                #the move is legal
                return True
        #ELSE THEN
        else:
            #IF change in rank == -1 AND chagne in column == 0 AND end square is empty THEN
            if end_rank - start_rank == -1 and end_column - start_column == 0 and board[end_rank][end_column] == "  ":
                #the move is legal
                return True
            #ELSE IF change in rank == -1 AND change in column == 1 AND end square has an enemy piece THEN
            elif end_rank - start_rank == -1 and abs(end_rank - start_rank) == 1 and board[end_rank][end_column][:1] == "W":
                #the move is legal
                return True

    return False

def checkMoveRook(start_rank, start_column, end_rank, end_column, team, start_pos, end_pos, board): # Returns True or false based on the legality of a move
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


def checkMoveKnight(start_rank, start_column, end_rank, end_column, team,start_pos, end_pos, board):# Returns True or false based on the legality of a move

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

def checkMoveBishop(start_rank, start_column, end_rank, end_column, team,start_pos, end_pos, board):# Returns True or false based on the legality of a move
    # has the piece moved ?
    if start_pos != end_pos:
        # Is the change in x coordinate the same as the change in y coordinate ? (Diagonal movement)
        if abs(changeRankToDigit(start_rank) - changeRankToDigit(end_rank)) == abs(start_column - end_column):
            # Does the square contatain a friendly piece ?
            if checkTeam(end_pos, board) != team:
                return True
    return False

def checkMoveKing(start_rank, start_column, end_rank, end_column, team,start_pos, end_pos, board):# Returns True or false based on the legality of a move
    # Has the piece moved ?
    if start_pos != end_pos:
        # Is the end position adjacent to the starting position ? (1 square away vertically, horazontally or diagonally)
        if abs(changeRankToDigit(start_rank) - changeRankToDigit(end_rank)) == 1 or abs(start_column - end_column) == 1 or abs(changeRankToDigit(start_rank) - changeRankToDigit(end_rank)) == 1 and abs(start_column - end_column) == 1 :
            if checkTeam(end_pos, board) != team:
                return True
    return False

def checkMoveQueen(start_rank, start_column, end_rank, end_column, team,start_pos, end_pos, board):# Returns True or false based on the legality of a move
    # Is the move legal by rook standard rules ?
    if checkMoveRook(start_rank, start_column, end_rank, end_column, team,start_pos, end_pos, board):
        return True
    # Is the move legal by normal bishop rules ?
    elif checkMoveBishop(start_rank, start_column, end_rank, end_column, team,start_pos, end_pos, board):
        return True
    return False
