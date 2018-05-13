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
    #Break the move up into the starting coordinate and the destination coordinate ["letter number" ]  ["letter number" ]
    move = move.split("x")
    #store the starting coordinate and break it down into the row and column (letter and number)
    starting_coordinate = move[0]
    starting_row = starting_coordinate[:1].upper()
    starting_column = starting_coordinate[1:]
    #store the ending coordinate and break it down into the row and column (letter and number)
    ending_coordinate = move[1]
    ending_row = ending_coordinate[:1].upper()
    ending_column = ending_coordinate[1:]
    #store any piece that may have been taken
    last_taken_piece = board[int(ending_column)][changeRowToDigit(ending_row)]
    #Take contence of starting square and place in in the destination / ending square
    board[int(ending_column)][changeRowToDigit(ending_row)] = board[int(starting_column)][changeRowToDigit(starting_row)]
    #empty the starting square
    board[int(starting_column)][changeRowToDigit(starting_row)] = "  "
    return last_taken_piece

def undoMove(move, last_known_piece, board): # --> takes in a move and performs it. takes item of start coordinate and places it in end coordinate then clears start coordinate
    #IF the move in in correct format and the coordinates provided exist THEN
    if not ( len(move) != 5 or move[2] != 'x' or move[0]  not in 'ABCDEFGHabcdefgh' and move[3] not in 'ABCDEFGHabcdefgh' or move[1] not in '12345678' and move[4] not in '12345678') :
        #Seperate the move into starting and ending coordinates
        move = move.split("x")
        #Seperate starting coordinates into row and column
        starting_coordinate = move[0]
        starting_row = starting_coordinate[:1].upper()
        starting_column = starting_coordinate[1:]
        #Seperate ending coordinates into row and column
        ending_coordinate = move[1]
        ending_row = ending_coordinate[:1].upper()
        ending_column = ending_coordinate[1:]
        #Take contence of starting square and place in in the destination / ending square
        board[int(starting_column)][changeRowToDigit(starting_row)] = board[int(ending_column)][changeRowToDigit(ending_row)]
        #Place whatever piece may have been taken back into its original position before it was taken
        board[int(ending_column)][changeRowToDigit(ending_row)] = last_known_piece

def pieceTeam(coordinate, board): # --> Returns "W" or "B" or "E" based on the content of the coordinate provided
    coordinate_row = changeRowToDigit(coordinate[:1])
    coordinate_column = int(coordinate[1:])
    square_content = board[coordinate_column][coordinate_row]
    #IF piece is on the white team THEN
    if square_content[:1] == "W":
        return "W"
    #IF piece is n the black team THEN
    elif square_content[:1] == "B":
        return "B"
    #IF the square doesn't have a team i.e. doesn't have a piece THEN
    else:
        return "E"

def onBoard(move):
    values = ['0','1', '2', '3', '4', '5', '6', '7']
    row = move[0]
    column = move[1]
    if row in values and column in values:
        return True
    else:
        return False

def changeRowToDigit(row):
    """changeRow
    Changes a specific row into a digit, beginning at 0
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
    digit = conversion[row.upper()]
    return digit


def changeDigitToRow(row):
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
    r = conversion[row]
    return r
