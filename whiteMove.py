import moveLegal
import generalFunctions
import check

# --> asks for an inputed move and performs it if it is legal
def makeMove(board):
    move = input("Make Your Move:") # MUST be in the form 'starting coordinate x ending coordinate' --> example: B1xC1
    if move =='q' or move == "Q":
        quit()
    if len(move) != 5 or move[2] != 'x' or move[0]  not in 'ABCDEFGHabcdefgh' and move[3] not in 'ABCDEFGHabcdefgh' or move[1] not in '12345678' and move[4] not in '12345678':
        print("non-acceptable move attempt - Must be in the form 'starting coordinate x ending coordinate' --> example: B1xC1 ")
        makeMove(board)


    move = convertPlayerMove(move)

    # If the move entered is legal
    if moveLegal.checkMove(move,board):

        #Make the move by changing the board
        last_taken_piece = generalFunctions.performMove(move, board)
        #If white king is in check then
        if check.isCheck(board) == "W":
            #Undo the move

            generalFunctions.undoMove(move,last_taken_piece,  board)

            print("illegal move, try again")
            makeMove(board)

    else:
        print("illegal move, try again")
        makeMove(board)

def convertPlayerMove(move): # --> converts the inputed player move to a move usable by calculations. (changes the file of all coordinates by - 1)
    move = move.split("x")
    starting_coordinate = move[0]
    starting_file = str(int(starting_coordinate[1:]) - 1)
    starting_coordinate = starting_coordinate[:1] + starting_file
    ending_coordinate = move[1]
    ending_file = str(int(ending_coordinate[1:]) - 1)
    ending_coordinate = ending_coordinate[:1] + ending_file
    new_move = starting_coordinate + "x" + ending_coordinate
    return new_move
