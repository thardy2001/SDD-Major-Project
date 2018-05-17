from generalFunctions import *
import check
import moveLegal

#Set the initial starting locations of all white pieces ,this list is updated after every move 
piece_locations =["A0", 'A1', 'B0', 'B1',"C0", 'C1', 'D0', 'D1',"E0", 'E1', 'F0', 'F1', "G0", 'G1', 'H0', 'H1',]

def makeMove(board): # --> asks for an inputed move and performs it if it is legal
    print("ENTER Q to QUIT")
    move = input("Make Your Move:") # MUST be in the form 'starting coordinate x ending coordinate' --> example: B1xC1
	
	#IF the input is Q or q THEN 
    if move =='q' or move == "Q":
		#exit the program 
        quit()
	#IF the input is not in the correct format THEN
    if len(move) != 5 or move[2] != 'x' or move[0]  not in 'ABCDEFGHabcdefgh' and move[3] not in 'ABCDEFGHabcdefgh' or move[1] not in '12345678' and move[4] not in '12345678':
        print("non-acceptable move attempt - Must be in the form 'starting coordinate x ending coordinate' --> example: B1xC1 ")
		#Retry 
        makeMove(board)

	#Convert the users inputed move bu decreasing column values by 1 (A8 --> A7, B4 --> B3 etc.)
    move = convertPlayerMove(move)
	
	#Set move made to False by default 
    moveMade = False
	
	#generate a list of all legal moves white can make 
    moves_list = moveLegal.generateMoveList(board, piece_locations, "W")
    
    #While a legal move hasn't been made 
    while not moveMade:
		
		#IF the inputed move is legal by move definitions 
        if move in moves_list:

            #Make the move by changing the board
            last_taken_piece = performMove(move, board)
			
            #If white king is in check then
            if check.isCheck(board) == "W":
			
                #Undo the move
                undoMove(move,last_taken_piece,  board)
				
				#Delete the move from the list of legal moves as it is illegal due to check 
                del moves_list[moves_list.index(move)]
				
			#IF it isn't check after the move 
            else:
                moveMade = True

		#ELSE the move is illegal by movement definitions 
        else:
            print("illegal move, try again")
			
			#Try again 
            makeMove(board)
	
	#Separate the move into the starting position and ending positions 
    move = move.split('x')
	
	#After a move is made update the list of white piece locations 
    indexOfStartingPosition =  piece_locations.index(move[0])
    del piece_locations[indexOfStartingPosition]
    piece_locations.append(move[1])

def convertPlayerMove(move): # --> converts the inputed player move to a move usable by calculations. (changes the column of all coordinates by - 1)
	
	#Convert the letters to uppercase 
    move = move.upper()
	
	#Separate the move into beginning and ending coordinates and further into row and column values changing the column values by - 1
    move = move.split("X")
    starting_coordinate = move[0]
    starting_column = str(int(starting_coordinate[1:]) - 1)
    starting_coordinate = starting_coordinate[:1] + starting_column
    ending_coordinate = move[1]
    ending_column = str(int(ending_coordinate[1:]) - 1)
	
	#Rebuild the new converted move 
    ending_coordinate = ending_coordinate[:1] + ending_column
    new_move = starting_coordinate + "x" + ending_coordinate
    return new_move
