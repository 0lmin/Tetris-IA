import numpy as np

T_TYPE=0
T_COLOR=1
T_MATRICE=2


# class TetrominoStatic:
#     name
#     color
#     matrices [...]
#
# TETROMINO_I = TetrominoStatic()
# TETROMINO_I.name = "I"
# TETROMINO_I.color = ...

TETROMINO_I = [1, (0, 255, 255), [np.array([[0,0,0,0],
                                              [1,1,1,1],
                                              [0,0,0,0],
                                              [0,0,0,0]]), np.array([[0,1,0,0],
                                                                     [0,1,0,0],
                                                                     [0,1,0,0],
                                                                     [0,1,0,0]]), np.array([[0,0,0,0],
                                                                                            [0,0,0,0],
                                                                                            [1,1,1,1],
                                                                                            [0,0,0,0]]), np.array([[0,0,1,0],
                                                                                                                   [0,0,1,0],
                                                                                                                   [0,0,1,0],
                                                                                                                   [0,0,1,0]])]]
TETROMINO_O = [2, (255, 255, 0), [np.array([[0,0,0,0],
                                            [1,1,0,0],
                                            [1,1,0,0],
                                            [0,0,0,0]]), np.array([[0,0,0,0],
                                                                   [1,1,0,0],
                                                                   [1,1,0,0],
                                                                   [0,0,0,0]]), np.array([[0,0,0,0],
                                                                                          [1,1,0,0],
                                                                                          [1,1,0,0],
                                                                                          [0,0,0,0]]), np.array([[0,0,0,0],
                                                                                                                 [1,1,0,0],
                                                                                                                 [1,1,0,0],
                                                                                                                 [0,0,0,0]])]]
TETROMINO_T = [3, (170, 0, 255), [np.array([[0,1,0],
                                              [1,1,1],
                                              [0,0,0]]),np.array([[0,1,0],
                                                                 [0,1,1],
                                                                 [0,1,0]]), np.array([[0,0,0],
                                                                                      [1,1,1],
                                                                                      [0,1,0]]), np.array([[0,1,0],
                                                                                                           [1,1,0],
                                                                                                           [0,1,0]])]]
TETROMINO_L = [4, (255, 165, 0), [np.array([[0,0,1],
                                              [1,1,1],
                                              [0,0,0]]),np.array([[0,1,0],
                                                                 [0,1,0],
                                                                 [0,1,1]]), np.array([[0,0,0],
                                                                                      [1,1,1],
                                                                                      [1,0,0]]), np.array([[1,1,0],
                                                                                                           [0,1,0],
                                                                                                           [0,1,0]])]]
TETROMINO_J = [5, (0, 0, 255), [np.array([[1,0,0],
                                            [1,1,1],
                                            [0,0,0]]),np.array([[0,1,1],
                                                               [0,1,0],
                                                               [0,1,0]]), np.array([[0,0,0],
                                                                                    [1,1,1],
                                                                                    [0,0,1]]), np.array([[0,1,0],
                                                                                                         [0,1,0],
                                                                                                         [1,1,0]])]]
TETROMINO_Z = [6, (255, 0, 0), [np.array([[1,1,0],
                                            [0,1,1],
                                            [0,0,0]]),np.array([[0,0,1],
                                                               [0,1,1],
                                                               [0,1,0]]), np.array([[0,0,0],
                                                                                    [1,1,0],
                                                                                    [0,1,1]]), np.array([[0,1,0],
                                                                                                         [1,1,0],
                                                                                                         [1,0,0]])]]
TETROMINO_S = [7, (0, 255, 0), [np.array([[0,1,1],
                                            [1,1,0],
                                            [0,0,0]]),np.array([[0,1,0],
                                                                 [0,1,1],
                                                                 [0,0,1]]), np.array([[0,0,0],
                                                                                      [0,1,1],
                                                                                      [1,1,0]]), np.array([[1,0,0],
                                                                                                           [1,1,0],
                                                                                                           [0,1,0]])]]

TETROMINOS = {"I":TETROMINO_I, "O":TETROMINO_O, "T":TETROMINO_T, "L":TETROMINO_L, "J":TETROMINO_J, "Z":TETROMINO_Z, "S":TETROMINO_S}

class Tetromino:
    def __init__(self, type, rotation, position):
        self.color = TETROMINOS.get(type)[T_COLOR] # TETROMINOS[type].color TETROMINOS.get(type)[T_COLOR]
        self.type = type #between 0 and 7
        self.rotation = rotation
        self.position = position #topleft corner
        self.color = TETROMINOS.get(type)[T_COLOR]
        self.matrice = TETROMINOS.get(type)[T_MATRICE][rotation] #matrice

    def applyOnBoard(self, board):#fonction appelé à chaque (affichage) + placement de la piece
        for j in range(len(self.matrice)):
            for i in range(len(self.matrice)):
                if self.matrice[i][j] == 1:
                    board[self.position[0] + i][self.position[1] + j] = TETROMINOS.get(self.type)[T_TYPE]

    def __envCollision(self, board, dir, rotation):
        matrice = TETROMINOS.get(self.type)[T_MATRICE][(self.rotation + rotation) % 4]
        for j in range(len(self.matrice)):
            for i in range(len(self.matrice)):
                if ((self.position[1] + j + dir[1] < 0 or self.position[1] + j + dir[1] > 19) or
                    (self.position[0] + i + dir[0] < 0 or self.position[0] + i + dir[0] > 9)) and (matrice[i][j] > 0):
                    return True
        return False

    def __boardCollision(self, board, dir, rotation):
        matrice = TETROMINOS.get(self.type)[T_MATRICE][(self.rotation + rotation) % 4]
        for j in range(len(self.matrice)):
            for i in range(len(self.matrice)):
                if ((self.position[1] + j +  dir[1] >= 0 and self.position[1] + j + dir[1] <= 19) and
                    (self.position[0] + i + dir[0] >= 0 and self.position[0] + i + dir[0] <= 9)) and (matrice[i][j] > 0) and board[self.position[0] + i + dir[0], self.position[1] + j + dir[1]] > 0:
                    return True
        return False

    def goDown(self, board):
        # Board is used to see if the move is possible
        if self.__envCollision(board, [0,1], 0):
            return False
        if self.__boardCollision(board, [0,1], 0):
            return False
        self.position[1] = self.position[1] + 1
        return True

    def goLeft(self, board):
        # Board is used to see if the move is possible
        if self.__envCollision(board, [-1,0], 0):
            return False
        if self.__boardCollision(board, [-1,0], 0):
            return False
        self.position[0] = self.position[0] - 1

    def goRight(self, board):
        # Board is used to see if the move is possible
        if self.__envCollision(board, [1,0], 0):
            return False
        if self.__boardCollision(board, [1,0], 0):
            return False
        self.position[0] = self.position[0] + 1

    def goUP(self, board):
        # Board is used to see if the move is possible
        while self.goDown(board):
            pass

    def rotateLeft(self, board):
        # Board is used to see if the move is possible
        if self.__envCollision(board, [0,0], -1):
            return False
        if self.__boardCollision(board, [0,0], -1):
            return False
        self.rotation = (self.rotation - 1) % 4
        self.matrice = TETROMINOS.get(self.type)[T_MATRICE][self.rotation]

    def rotateRight(self, board):
        # Board is used to see if the move is possible
        if self.__envCollision(board, [0,0], 1):
            return False
        if self.__boardCollision(board, [0,0], 1):
            return False
        self.rotation = (self.rotation + 1) % 4
        self.matrice = TETROMINOS.get(self.type)[T_MATRICE][self.rotation]



# Chaque affichage
# toDrawBoard = deepcopy(board)
# playedTetromino.applyOnBoard(toDrawBoard)
# drawBoard(toDrawBoard)
