#         H                          G                          F                          E                          D             
board = [['','','','','','','',''], ['','','','','','','',''], ['','','','','','','',''], ['','','','','','','',''], ['','','','','','','',''],
      #   C                          B                          A
         ['','','','','','','',''], ['','','','','','','',''], ['','','','','','','','']]
RANK = {"A":board[7], "B":board[6], "C":board[5], "D":board[4], "E":board[3], "F":board[2], "G":board[1], "H":board[0]}


def reset_board():

    for i in range(len(board)):
        for k in range(len(board[i])):
            board[i][k] = ''

    for i in range(8):
        RANK["B"][i] = "WP"
        RANK["G"][i] = "BP"



reset_board()
for i in range(len(board)):
    print(board[i])
