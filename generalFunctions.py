def reset_board(board): # --> Restart The game, put all pieces back in their starting positions

    #For every "Cell" on the board
    for i in range(len(board)):
        for k in range(len(board[i])):
            #Empty Cell
            board[i][k] = '  '
    #Place All Pawns
    for i in range(8):
        board[1][i] = "WP"
        board[6][i] = "BP"
    #Place the rest of the pieces
        #White
    board[0][0] = "WR"
    board[0][1] = "WN"
    board[0][2] = "WB"
    board[0][3] = "WQ"
    board[0][4] = "WK"
    board[0][5] = "WB"
    board[0][6] = "WN"
    board[0][7] = "WR"
        #Black
    board[7][0] = "BR"
    board[7][1] = "BN"
    board[7][2] = "BB"
    board[7][3] = "BQ"
    board[7][4] = "BK"
    board[7][5] = "BB"
    board[7][6] = "BN"
    board[7][7] = "BR"


def displayBoard(board): # --> Displays the current state of the board
    for i in range(8):
        print(8-i, board[7-i])
    print("    A     B     C     D     E     F     G     H")

def performMove(move, board): # --> takes in a move and performs it. takes item of start coordinate and places it in end coordinate then clears start coordinate
    move = move.split("x")
    starting_coordinate = move[0]
    starting_rank = starting_coordinate[:1].upper()
    starting_file = starting_coordinate[1:]
    ending_coordinate = move[1]
    ending_rank = ending_coordinate[:1].upper()
    ending_file = ending_coordinate[1:]
    last_taken_piece = board[int(ending_file)][changeRankToDigit(ending_rank)]
    board[int(ending_file)][changeRankToDigit(ending_rank)] = board[int(starting_file)][changeRankToDigit(starting_rank)]
    board[int(starting_file)][changeRankToDigit(starting_rank)] = "  "
    return last_taken_piece

def undoMove(move, last_known_piece, board): # --> takes in a move and performs it. takes item of start coordinate and places it in end coordinate then clears start coordinate
    if not ( len(move) != 5 or move[2] != 'x' or move[0]  not in 'ABCDEFGHabcdefgh' and move[3] not in 'ABCDEFGHabcdefgh' or move[1] not in '12345678' and move[4] not in '12345678') :
        move = move.split("x")
        starting_coordinate = move[0]
        starting_rank = starting_coordinate[:1].upper()
        starting_file = starting_coordinate[1:]
        ending_coordinate = move[1]
        ending_rank = ending_coordinate[:1].upper()
        ending_file = ending_coordinate[1:]

        board[int(starting_file)][changeRankToDigit(starting_rank)] = board[int(ending_file)][changeRankToDigit(ending_rank)]
        board[int(ending_file)][changeRankToDigit(ending_rank)] = last_known_piece

def pieceTeam(coordinate, board): # --> Returns "W" or "B" or "E" based on the content of the coordinate provided
    coordinate_rank = changeRankToDigit(coordinate[:1])
    coordinate_file = int(coordinate[1:])
    square_content = board[coordinate_file][coordinate_rank]
    if square_content[:1] == "W":
        return "W"
    elif square_content[:1] == "B":
        return "B"
    else:
        return "E"

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

    }
    digit = conversion[rank.upper()]
    return digit


def changeDigitToRank(rank):
    conversion = {
    0 :'A',
    1 :'B',
    2 :'C',
    3 :'D',
    4 :'E',
    5 :'F',
    6 :'G',
    7 :'H',

    }
    r = conversion[rank]
    return r
