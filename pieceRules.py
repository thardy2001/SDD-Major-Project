from generalFunctions import *

#BEGIN blackPawnMovement(starting coordinate, ending coordinate, board state)
def blackPawnMovement(starting_coordinate, ending_coordinate, board): # --> returns true if the move is legal otherwise false
    #get starting rank, ending rank, starting file and ending file
    starting_rank = starting_coordinate[:1]
    starting_file = int(starting_coordinate[1:])
    ending_rank = ending_coordinate[:1]
    ending_file = int(ending_coordinate[1:])
    #IF ending coordinate is empty THEN
    if pieceTeam(ending_coordinate, board) == "E" and pieceTeam(starting_coordinate, board) == "B":
        #IF starting file == 6 THEN
        if starting_file == 6:
            #IF change in file == -2 AND change in rank == 0 OR change in file == -1 AND change in rank == 0 THEN
            if ending_file - starting_file == -2 and abs(changeRankToDigit(ending_rank) - changeRankToDigit(starting_rank)) == 0 or ending_file - starting_file == -1 and abs(changeRankToDigit(ending_rank) - changeRankToDigit(starting_rank)) == 0:
                # the move is legal
                return True
        #ELSE THEN
        else:
            #IF change in file == -1 AND change in rank == 0 THEN
            if ending_file - starting_file == -1 and abs(changeRankToDigit(ending_rank) - changeRankToDigit(starting_rank)) == 0:
                # the move is legal
                return True
        #IF change in file == -1 AND change in rank == 1 AND end coordinate has a white piece THEN
        if ending_file - starting_file == -1 and abs(changeRankToDigit(ending_rank) - changeRankToDigit(starting_rank)) == 1 and pieceTeam(ending_coordinate, board) == "W":
            # the move is legal
            return True
    # the move is illegal
    return False

#BEGIN whitePawnMovement(starting coordinate, ending coordinate, board state)
def whitePawnMovement(starting_coordinate, ending_coordinate, board): # --> returns true if the move is legal otherwise false
    #get starting rank, ending rank, starting file and ending file

    starting_rank = starting_coordinate[:1]
    starting_file = int(starting_coordinate[1:])
    ending_rank = ending_coordinate[:1]
    ending_file = int(ending_coordinate[1:])
    #IF ending coordinate is empty THEN
    if pieceTeam(ending_coordinate, board) == "E" and pieceTeam(starting_coordinate, board) == "W":
        #IF starting file == 1 THEN
        if starting_file == 1:
            #IF change in file == 2 AND change in rank == 0 OR change in file == 1 AND change in rank == 0 THEN
            if ending_file - starting_file == 2 and abs(changeRankToDigit(ending_rank) - changeRankToDigit(starting_rank)) == 0 or ending_file - starting_file == 1 and abs(changeRankToDigit(ending_rank) - changeRankToDigit(starting_rank)) == 0:
                # the move is legal
                return True
        #ELSE THEN
        else:
            #IF change in file == 1 AND change in rank == 0 THEN
            if ending_file - starting_file == 1 and abs(changeRankToDigit(ending_rank) - changeRankToDigit(starting_rank)) == 0:
                # the move is legal
                return True
        #IF change in file == 1 AND change in rank == 1 AND end coordinate has a black piece THEN
        if ending_file - starting_file == 1 and abs(changeRankToDigit(ending_rank) - changeRankToDigit(starting_rank)) == 1 and pieceTeam(ending_coordinate, board) == "B":
            # the move is legal
            return True
    # the move is illegal
    return False

#BEGIN rookMovement(starting coordinate, ending coordinate, turn, board state)
def rookMovement(starting_coordinate, ending_coordinate, turn, board): # --> returns true if the move is legal otherwise false
    #get starting rank, ending rank, starting file and ending file
    starting_rank = starting_coordinate[:1]
    starting_file = int(starting_coordinate[1:])
    ending_rank = ending_coordinate[:1]
    ending_file = int(ending_coordinate[1:])
    team = pieceTeam(starting_coordinate, board)
    move = starting_coordinate + 'x' + ending_coordinate

    #IF ending coordinate doesn't have a friendly piece THEN
    if pieceTeam(ending_coordinate, board) != team and pieceTeam(starting_coordinate, board) == turn:

        if ending_file - starting_file == 0 and abs(changeRankToDigit(ending_rank) - changeRankToDigit(starting_rank)) != 0:
            bound = findRookBoundaries(move, board)
            print(bound)

            if changeRankToDigit(starting_rank) - changeRankToDigit(ending_rank) < 0:
                print("change in rank cannot be less than:", bound, "Change in rank is:",changeRankToDigit(starting_rank) - changeRankToDigit(ending_rank) )
                if changeRankToDigit(starting_rank) - changeRankToDigit(ending_rank) < bound:
                    return False
                else:
                    return True
            elif changeRankToDigit(starting_rank) - changeRankToDigit(ending_rank) > 0:
                print("change in rank cannot be less than:", bound, "Change in rank is:",changeRankToDigit(starting_rank) - changeRankToDigit(ending_rank) )
                if changeRankToDigit(starting_rank) - changeRankToDigit(ending_rank) < bound:
                    return False
                else:
                    return True
            #the move is legal
            return True

        elif ending_file - starting_file != 0 and abs(changeRankToDigit(ending_rank) - changeRankToDigit(starting_rank)) == 0:
            bound = findRookBoundaries(move, board)
            print(bound)
            if starting_file - ending_file < 0:
                print("change in file cannot be less than:", bound, "Change in file is:", starting_file - ending_file )
                if starting_file - ending_file < bound:
                    return False
                else:
                    return True
            elif starting_file - ending_file > 0:
                print("change in file cannot be less than:", bound, "Change in file is:", starting_file - ending_file )
                if starting_file - ending_file < bound:
                    return False
                else:
                    return True
            # the move is legal
            return True
    # the move is illegal
    return False


#BEGIN knightMovement(starting coordinate, ending coordinate, turn, board state)
def knightMovement(starting_coordinate, ending_coordinate, turn, board): # --> returns true if the move is legal otherwise false
    #get starting rank, ending rank, starting file and ending file
    starting_rank = starting_coordinate[:1]
    #print("Knight Starting Coordinate:", starting_coordinate[0] + str(int(starting_coordinate[1]) + 1), "Ending coordinate:", ending_coordinate[0] + str(int(ending_coordinate[1]) + 1))
    #print("Team of the knight:", pieceTeam(starting_coordinate, board), "Team of destination:", pieceTeam(ending_coordinate, board))
    starting_file = int(starting_coordinate[1:])
    ending_rank = ending_coordinate[:1]
    ending_file = int(ending_coordinate[1:])

    #IF ending coordinate doesn't have a friendly piece THEN
    if pieceTeam(ending_coordinate, board) != pieceTeam(starting_coordinate, board) and pieceTeam(starting_coordinate, board) == turn:
        #IF the change in file == 2 AND the change in rank == 1 THEN
        if abs(ending_file - starting_file) == 2 and abs(changeRankToDigit(ending_rank) - changeRankToDigit(starting_rank)) == 1:
            # the move is legal
            return True
    #ELSE IF the change in file == 1 AND the change in rank == 2 THEN
    elif abs(ending_file - starting_file) == 1 and abs(changeRankToDigit(ending_rank) - changeRankToDigit(starting_rank)) == 2:
        # the move is legal
        return True
    # the move is illegal
    return False

#BEGIN bishopMovement(starting coordinate, ending coordinate, turn, board state)
def bishopMovement(starting_coordinate, ending_coordinate, turn, board): # --> returns true if the move is legal otherwise false
    #get starting rank, ending rank, starting file and ending file
    starting_rank = starting_coordinate[:1]
    starting_file = int(starting_coordinate[1:])
    ending_rank = ending_coordinate[:1]
    ending_file = int(ending_coordinate[1:])
    team = pieceTeam(starting_coordinate, board)
    #IF the ending coordinate doesn't contain a friendly piece THEN
    if pieceTeam(ending_coordinate, board) != team and pieceTeam(starting_coordinate, board) == turn:
        #IF the change in rank == change in file THEN
        if abs(ending_file - starting_file) == abs(changeRankToDigit(ending_rank) - changeRankToDigit(starting_rank)):
            # the move is legal
            return True
    #the move is illegal
    return False

#BEGIN queenMovement(starting coordinate, ending coordinate, turn, board state)
def queenMovement(starting_coordinate, ending_coordinate, turn, board): # --> returns true if the move is legal otherwise false
    #IF the move is legal by bishop movement rules THEN
    if bishopMovement(starting_coordinate, ending_coordinate, turn, board):
        # the move is legal
        return True
    #ELSE IF the move is legal by rook movement rules THEN
    elif rookMovement(starting_coordinate, ending_coordinate, turn, board):
        # the move is legal
        return True
    #the move is illegal
    return False

#BEGIN kingMovement(starting coordinate, ending coordinate, turn, board state)
def kingMovement(starting_coordinate, ending_coordinate, turn, board): # --> returns true if the move is legal otherwise false
    #get starting rank, ending rank, starting file and ending file
    starting_rank = starting_coordinate[:1]
    starting_file = int(starting_coordinate[1:])
    ending_rank = ending_coordinate[:1]
    ending_file = int(ending_coordinate[1:])
    team = pieceTeam(starting_coordinate, board)
    #IF destination square doen't contain a friendly piece and the piece moved is of the correct team THEN
    if pieceTeam(ending_coordinate, board) != team and pieceTeam(starting_coordinate, board) == team:
        #IF ending_coordinate is adjacent to starting_coordinate THEN
        if abs(ending_file - starting_file) < 1 and abs(ending_file - starting_file) > -1 and abs(changeRankToDigit(ending_rank) - changeRankToDigit(starting_rank)) > -1 and abs(changeRankToDigit(ending_rank) - changeRankToDigit(starting_rank)) < 2:
            return True
    return False


def findRookBoundaries(move, board):
    bound = 0
    move = move.split('x')
    starting_coordinate = move[0]
    ending_coordinate = move[1]
    starting_rank = changeRankToDigit(starting_coordinate[0])
    starting_row = int(starting_coordinate[1]) - 1
    ending_rank = changeRankToDigit(ending_coordinate[0])
    ending_row = int(ending_coordinate[1]) - 1
    if starting_rank - ending_rank != 0:
        #Left
        print('0')
        if starting_rank - ending_rank > 0:
            for i in range(starting_rank - ending_rank):
                if board[starting_rank - i][starting_row] != '  ':
                    bound = i
                    break
        #Right

        if starting_rank - ending_rank < 0:
            for i in range(abs(starting_rank - ending_rank)):
                if board[starting_rank + i][starting_row] != '  ':
                    bound = i
                    break
        return bound

    elif starting_row - ending_row != 0:
        print('1')
        #UP
        if starting_rank - ending_rank < 0:
            for i in range(abs(starting_rank - ending_rank)):
                if board[starting_rank + i][starting_row] != '  ':
                    bound = i
                    break
        #Down
        if starting_rank - ending_rank > 0:
            for i in range(starting_rank - ending_rank):
                if board[starting_rank - i][starting_row] != '  ':
                    bound = i
                    break
        return bound