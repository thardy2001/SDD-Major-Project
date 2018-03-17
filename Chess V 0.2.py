#         H                          G                          F                          E                          D             
board = [['','','','','','','',''], ['','','','','','','',''], ['','','','','','','',''], ['','','','','','','',''], ['','','','','','','',''],
      #   C                          B                          A
         ['','','','','','','',''], ['','','','','','','',''], ['','','','','','','','']]
RANK = {"A":board[7], "B":board[6], "C":board[5], "D":board[4], "E":board[3], "F":board[2], "G":board[1], "H":board[0]}


def reset_board():

    for i in range(len(board)):
        for k in range(len(board[i])):
            board[i][k] = '  '

    for i in range(8):
        RANK["B"][i] = "WP"
        RANK["G"][i] = "BP"

    RANK["A"][0] = "WR"
    RANK["A"][1] = "WN"
    RANK["A"][2] = "WB"
    RANK["A"][3] = "WQ"
    RANK["A"][4] = "WK"
    RANK["A"][5] = "WB"
    RANK["A"][6] = "WN"
    RANK["A"][7] = "WR"
    
    RANK["H"][0] = "BR"
    RANK["H"][1] = "BN"
    RANK["H"][2] = "BB"
    RANK["H"][3] = "BQ"
    RANK["H"][4] = "BK"
    RANK["H"][5] = "BB"
    RANK["H"][6] = "BN"
    RANK["H"][7] = "BR"

 
    
            
def displayBoard():
    for i in range(len(board)):
        print(board[i])

reset_board()

displayBoard()

