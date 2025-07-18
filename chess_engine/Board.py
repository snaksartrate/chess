import pieces

def create_board():
    board = ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
    for _ in range(8):
        board.append('p')
    for _ in range(32):
        board.append('_')
    for _ in range(8):
        board.append('P')
    rank1 = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
    for i in rank1:
        board.append(i)
    return board

def print_board(board):
    for i in range(8):
        s = ''
        for j in range(8):
            s += board[i * 8 + j]
            s += ' '
        print(s)

def make_move(board, initial, final):
    # initial is the piece to be moved along with the square it is on
    # final is the destination
    # something like - make_move("Bb3", "Bc4") 
    if len(final) == 3:
        piece = final[0]
        i_final = final[2]
        j_final = final[1]
        i_initial = initial[2]
        j_initial = initial[1]
        possible_moves = pieces.get_moves(initial)
        if final not in possible_moves:
            return board
        board[i_final * 8 + j_final] = board[i_initial * 8 + j_initial]
        board[i_initial * 8 + j_initial] = '_'
        return board
    if len(final) == 2:
        j_final = final[1]
        i_final = final[2]
        j_initial = initial[1]
        i_initial = initial[2]