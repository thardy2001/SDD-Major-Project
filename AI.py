import generalFunctions
import random
import moveLegal
import check
piece_locations =["a7", 'a6', 'b7', 'b6',"c7", 'c6', 'd7', 'd6',"e7", 'e6', 'f7', 'f6', "g7", 'g6', 'h7', 'h6',]
#Black makes a move
def makeMove(board):
    #check the board for all black piece coordinates
    startingPositions = piece_locations
    moveMade = False
    #generate a list of all legal moves black can make
    moves_list = moveLegal.generateMoveList(board, startingPositions, "B")
    print("All black legal moves: ", moves_list)
    #Organise the list based on quality of the moves
    while not moveMade:
        num = random.randint(0, len(moves_list) -1)
        #Perform a move
        last_taken_piece = generalFunctions.performMove(moves_list[num], board)
        if check.isCheck(board) == "B":
            #Undo the move

            undoMove(move,last_taken_piece,  board)
            del moves_list[num]
        else:
            moveMade = True

    #Update the locations of black pieces
    move = moves_list[num]
    move = move.split('x')
    del startingPositions[startingPositions.index(move[0])]
    startingPositions.append(move[1])
