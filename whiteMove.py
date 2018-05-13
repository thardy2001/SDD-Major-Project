from generalFunctions import *
import check
import moveLegal

piece_locations =["a0", 'a1', 'b0', 'b1',"c0", 'c1', 'd0', 'd1',"e0", 'e1', 'f0', 'f1', "g0", 'g1', 'h0', 'h1',]
# --> asks for an inputed move and performs it if it is legal
def makeMove(board):
    print("ENTER Q to QUIT")
    move = input("Make Your Move:") # MUST be in the form 'starting coordinate x ending coordinate' --> example: B1xC1
    if move =='q' or move == "Q":
        quit()
    if len(move) != 5 or move[2] != 'x' or move[0]  not in 'ABCDEFGHabcdefgh' and move[3] not in 'ABCDEFGHabcdefgh' or move[1] not in '12345678' and move[4] not in '12345678':
        print("non-acceptable move attempt - Must be in the form 'starting coordinate x ending coordinate' --> example: B1xC1 ")
        makeMove(board)


    move = convertPlayerMove(move)
    moveMade = False
    moves_list = moveLegal.generateMoveList(board, piece_locations, "W")
    # If the move entered is legal

    print("All moves white can make: (should total to 20 moves) ", moves_list)
    while not moveMade:

        if move in moves_list:

            #Make the move by changing the board
            last_taken_piece = performMove(move, board)
            #If white king is in check then
            if check.isCheck(board) == "W":
                #Undo the move

                undoMove(move,last_taken_piece,  board)
                del moves_list[moves_list.index(move)]
            else:
                moveMade = True


        else:
            print("illegal move, try again")
            makeMove(board)

    move = move.split('x')
    indexOfStartingPosition =  piece_locations.index(move[0])
    del piece_locations[indexOfStartingPosition]
    piece_locations.append(move[1])

def convertPlayerMove(move): # --> converts the inputed player move to a move usable by calculations. (changes the column of all coordinates by - 1)
    move = move.split("x")
    starting_coordinate = move[0]
    starting_column = str(int(starting_coordinate[1:]) - 1)
    starting_coordinate = starting_coordinate[:1] + starting_column
    ending_coordinate = move[1]
    ending_column = str(int(ending_coordinate[1:]) - 1)
    ending_coordinate = ending_coordinate[:1] + ending_column
    new_move = starting_coordinate + "x" + ending_coordinate
    return new_move
