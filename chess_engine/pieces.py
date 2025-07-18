class Bishop:
    def __init__(self):
        self.value = 3
    
    def get_moves(self, position):
        j = int(position[1])
        i = int(position[2])
        # j is the rank, i is the file
        moves = []
        for k in range(1, 9):
            if i + k > 0 and i + k < 9 and j + k > 0 and j + k < 9:
                move = 'B' + str(j + k) + str(i + k)
                moves.append(move)
            if i + k > 0 and i + k < 9 and j - k > 0 and j - k < 9:
                move = 'B' + str(j - k) + str(i + k)
                moves.append(move)
            if i - k > 0 and i - k < 9 and j + k > 0 and j + k < 9:
                move = 'B' + str(j + k) + str(i - k)
                moves.append(move)
            if i - k > 0 and i - k < 9 and j - k > 0 and j - k < 9:
                move = 'B' + str(j - k) + str(i - k)
                moves.append(move)
        key = ['', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        for index, move in enumerate(moves):
            moves[index] = move[0] + key[int(move[1])] + move[2]
        return moves

class Rook:
    def __init__(self):
        self.value = 5
    
    def get_moves(self, position):
        j = int(position[1])
        i = int(position[2])
        # j is the rank, i is the file
        moves = []
        for k in range(1, 9):
            if i + k > 0 and i + k < 9:
                move = 'R' + str(j) + str(i + k)
                moves.append(move)
            if j - k > 0 and j - k < 9:
                move = 'R' + str(j - k) + str(i)
                moves.append(move)
            if j + k > 0 and j + k < 9:
                move = 'R' + str(j + k) + str(i)
                moves.append(move)
            if i - k > 0 and i - k < 9:
                move = 'R' + str(j) + str(i - k)
                moves.append(move)
        key = ['', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        for index, move in enumerate(moves):
            moves[index] = move[0] + key[int(move[1])] + move[2]
        return moves

class Queen:
    def __init__(self, colour):
        self.value = 9
    
    def get_moves(self, position):
        j = int(position[1])
        i = int(position[2])
        # j is the rank, i is the file
        moves = []
        for k in range(1, 9):
            if i + k > 0 and i + k < 9:
                move = 'Q' + str(j) + str(i + k)
                moves.append(move)
                if j + k > 0 and j + k < 9:
                    move = 'Q' + str(j + k) + str(i + k)
                    moves.append(move)
            if i - k > 0 and i - k < 9:
                move = 'Q' + str(j) + str(i - k)
                moves.append(move)
                if j - k > 0 and j - k < 9:
                    move = 'Q' + str(j - k) + str(i - k)
                    moves.append(move)
            if j + k > 0 and j + k < 9:
                move = 'Q' + str(j + k) + str(i)
                moves.append(move)
                if i - k > 0 and i - k < 9:
                    move = 'Q' + str(j + k) + str(i - k)
                    moves.append(move)
            if j - k > 0 and j - k < 9:
                move = 'Q' + str(j - k) + str(i)
                moves.append(move)
                if i + k > 0 and i + k < 9:
                    move = 'Q' + str(j - k) + str(i + k)
                    moves.append(move)
        key = ['', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        for index, move in enumerate(moves):
            moves[index] = move[0] + key[int(move[1])] + move[2]
        return moves

class King:
    def __init__(self, colour):
        self.value = 255
    
    def get_moves(self, position):
        j = int(position[1])
        i = int(position[2])
        # j is the rank, i is the file
        moves = []
        if i > 1 and i < 8 and j > 1 and j < 8:
            moves.append('K' + str(j - 1) + str(i - 1))
            moves.append('K' + str(j - 1) + str(i))
            moves.append('K' + str(j - 1) + str(i + 1))
            moves.append('K' + str(j) + str(i - 1))
            moves.append('K' + str(j) + str(i + 1))
            moves.append('K' + str(j + 1) + str(i - 1))
            moves.append('K' + str(j + 1) + str(i))
            moves.append('K' + str(j + 1) + str(i + 1))
        elif i == 1:
            if j == 1:
                moves.append('Ka7')
                moves.append('Kb8')
                moves.append('Kb7')
            elif j == 8:
                moves.append('Kh7')
                moves.append('Kg8')
                moves.append('Kg7')
            else:
                moves.append('Kh' + str(i - 1))
                for k in range(3):
                    s = 'Kg' + str(i - 1 + k)
                    moves.append(s)
                moves.append('Kh' + str(i + 1))
        elif i == 8:
            if j == 1:
                moves.append('Ka2')
                moves.append('Kb1')
                moves.append('Kb2')
            elif j == 8:
                moves.append('Kh2')
                moves.append('Kg1')
                moves.append('Kg2')
            else:
                moves.append('K' + str(j - 1) + '8')
                for k in range(3):
                    s = 'Kb' + str(i - 1 + k)
                    moves.append(s)
                moves.append('K' + str(i + 1) + '8')
        key = ['', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        for index, move in enumerate(moves):
            moves[index] = move[0] + key[int(move[1])] + move[2]
        return moves

class pawn:
    def __init__(self, colour):
        self.value  = 1
        self.colour = colour
    
    def get_moves():
        pass

def get_moves(notation):
    key = { 'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6', 'g': '7', 'h': '8'}
    notation = notation[0] + key[notation[1]] + notation[2]
    if notation[0] == 'B':
        B = Bishop("white")
        return B.get_moves(notation)
    if notation[0] == 'R':
        R = Rook("white")
        return R.get_moves(notation)
    if notation[0] == 'Q':
        Q = Queen("white")
        return Q.get_moves(notation)
    if notation[0] == 'b':
        b = Bishop("white")
        return b.get_moves(notation)
    if notation[0] == 'r':
        r = Rook("white")
        return r.get_moves(notation)
    if notation[0] == 'q':
        q = Queen("white")
        return q.get_moves(notation)
    return None

# B = Bishop("white")
# R = Rook("white")
# Q = Queen("white")
# print("if a piece were at b3 alone on a chessboad, it would have the following moves:")
# print(get_moves("Bb3"))
# print(get_moves("Rb3"))
# print(get_moves("Qb3"))

print(get_moves(input("enter a position: ")))