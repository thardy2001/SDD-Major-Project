import generalFunctions
import random
import moveLegal
import check

#Location of all black pieces
piece_locations =["A7", 'A6', 'B7', 'B6',"C7", 'C6', 'D7', 'D6',"E7", 'E6', 'F7', 'F6', "G7", 'G6', 'H7', 'H6',]
#Black makes a move
def makeMove(board): # --> Handle Blacks turn
    #check the board for all black piece coordinates
    startingPositions = piece_locations
    moveMade = False
    #generate a list of all legal moves black can make
    moves_list = moveLegal.generateMoveList(board, startingPositions, "B")

    #WHILE black hasn't made their move
    while not moveMade:
        #Choose a random number in the range of the length of the list of all their moves
        num = random.randint(0, len(moves_list) -1)

        print(moves_list)
        print("  ")
        print("Move chosen",moves_list[num])
        #Perform move
        last_taken_piece = generalFunctions.performMove(moves_list[num], board)
        print('Who is in check', check.isCheck(board))
        #IF black is in check after their move is done
        if check.isCheck(board) == "B":
            #Undo the move
            undoMove(move,last_taken_piece,  board)
            #Delete the move that puts them in check from the list of legal moves
            del moves_list[num]
        else:
            moveMade = True

    #Update the locations of black pieces
    move = moves_list[num]
    move = move.split('x')
    del startingPositions[startingPositions.index(move[0])]
    startingPositions.append(move[1])
