import gameFunctions
import moveRules
import random

def makeAImove(board, RANK):
    legal_moves = []
    for i in range(len(board)):
        for k in range(len(board[i])):
            #Empty Cell
            if board[i][k][:1]  == "W":

                for rank in range(len(board)):
                    for cell in range(len(board[rank])):
                        #Empty Cell
                        if board[rank][cell] != "  ":
                            start_pos = gameFunctions.changeDigitToRank(i) + str(k)
                            end_pos = gameFunctions.changeDigitToRank(rank) + str(cell)
                            move = start_pos + "x" + end_pos
                            piece = board[rank][cell]
                            team = piece[:1]
                            piece_type = piece[1:]
                            if team == "B":
                                if piece_type == "P":
                                    if moveRules.checkMovePawn(gameFunctions.changeDigitToRank(i),k, gameFunctions.changeDigitToRank(rank),cell, team, start_pos, end_pos, board):
                                        legal_moves.append(move)
                                elif piece_type == "B":
                                    if moveRules.checkMoveBishop(gameFunctions.changeDigitToRank(i),k,gameFunctions.changeDigitToRank(rank),cell, team, start_pos, end_pos, board):
                                        legal_moves.append(move)
                                elif piece_type == "Q":
                                    if moveRules.checkMovePawn(gameFunctions.changeDigitToRank(i),k,gameFunctions.changeDigitToRank(rank),cell, team, start_pos, end_pos, board):
                                        legal_moves.append(move)
                                elif piece_type == "K":
                                    if moveRules.checkMoveKing(gameFunctions.changeDigitToRank(i),k,gameFunctions.changeDigitToRank(rank),cell, team, start_pos, end_pos, board):
                                        legal_moves.append(move)
                                elif piece_type == "N":
                                    if moveRules.checkMoveKnight(gameFunctions.changeDigitToRank(i),k, gameFunctions.changeDigitToRank(rank),cell, team, start_pos, end_pos, board):
                                        legal_moves.append(move)
                                elif piece_type == "R":
                                    if moveRules.checkMoveRook(gameFunctions.changeDigitToRank(i),k, gameFunctions.changeDigitToRank(rank),cell, team, start_pos, end_pos, board):
                                        legal_moves.append(move)
    print(legal_moves)
    move = legal_moves[random.randint(0,len(legal_moves) - 1)]
    positions = move.split("x")
    start_pos = positions[0]
    start_rank = start_pos[0]
    start_column = start_pos[1]
    end_pos = positions[1]
    end_rank = end_pos[0]
    end_column = end_pos[1]
    RANK[end_rank.upper()][int(end_column)-1] = RANK[start_rank.upper()][int(start_column)]
    RANK[start_rank][int(start_column)] = '  '
    turn = "W"
    gameFunctions.displayBoard(board)
    gameFunctions.makeMove(RANK, board, turn)





def getAImoves(board,rank, column, RANK, x):
    for rows in range(len(board)):
        for cells in range(len(board)):

            move = gameFunctions.changeDigitToRank(rank) + str(column + 1) + "x" + gameFunctions.changeDigitToRank(rows) + str(cells + 1)
            print(move)
            move_legal = False
            moves = move.split("x")
            start_pos = moves[0]
            end_pos = moves[1]

            start_pos_rank = start_pos[:1]
            start_pos_rank = start_pos_rank.upper()

            end_pos_rank = end_pos[:1]
            end_pos_rank = end_pos_rank.upper()
            end_pos_column = int(end_pos[1:]) -1

            start_pos_column = int(start_pos[1:]) - 1
            piece = RANK[start_pos_rank][start_pos_column]

            piece_team = gameFunctions.checkTeam(start_pos,board)
            if piece_team != "B":

                return False

            if "P" in piece:
                move_legal = moveRules.checkMovePawn(start_pos_rank, start_pos_column, end_pos_rank, end_pos_column, piece_team, start_pos, end_pos, board)
            elif "R" in piece:
                move_legal =  moveRules.checkMoveRook(start_pos_rank, start_pos_column, end_pos_rank, end_pos_column, piece_team, start_pos, end_pos, board)
            elif piece == "WB" or piece == "BB":
                move_legal =  moveRules.checkMoveBishop(start_pos_rank, start_pos_column, end_pos_rank, end_pos_column, piece_team, start_pos, end_pos, board)
            elif "Q" in piece:
                move_legal =  moveRules.checkMoveQueen(start_pos_rank, start_pos_column, end_pos_rank, end_pos_column, piece_team, start_pos, end_pos, board)
            elif "K" in piece:
                move_legal =  moveRules.checkMoveKing(start_pos_rank, start_pos_column, end_pos_rank, end_pos_column, piece_team, start_pos, end_pos, board)
            elif "N" in piece:
                move_legal =  moveRules.checkMoveKnight(start_pos_rank, start_pos_column, end_pos_rank, end_pos_column, piece_team, start_pos, end_pos, board)


            if x == "y":
                if move_legal:
                    return True
                else:
                    return False
            elif x == "n":
                if move_legal:
                    return move
