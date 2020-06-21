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

TETROMINO_I = [0, (0, 255, 255), [np.array([[0,0,0,0],
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
TETROMINO_O = [1, (255, 255, 0), [np.array([[0,1,1,0],
                                              [0,1,1,0],
                                              [0,0,0,0],
                                              [0,0,0,0]]), np.array([[0,1,1,0],
                                                                     [0,1,1,0],
                                                                     [0,0,0,0],
                                                                     [0,0,0,0]]), np.array([[0,1,1,0],
                                                                                            [0,1,1,0],
                                                                                            [0,0,0,0],
                                                                                            [0,0,0,0]]), np.array([[0,1,1,0],
                                                                                                                   [0,1,1,0],
                                                                                                                   [0,0,0,0],
                                                                                                                   [0,0,0,0]])]]
TETROMINO_T = [2, (170, 0, 255), [np.array([[0,1,0],
                                              [1,1,1],
                                              [0,0,0]]),np.array([[0,1,0],
                                                                 [0,1,1],
                                                                 [0,1,0]]), np.array([[0,0,0],
                                                                                      [1,1,1],
                                                                                      [0,1,0]]), np.array([[0,1,0],
                                                                                                           [1,1,0],
                                                                                                           [0,1,0]])]]
TETROMINO_L = [3, (255, 165, 0), [np.array([[0,0,1],
                                              [1,1,1],
                                              [0,0,0]]),np.array([[0,1,0],
                                                                 [0,1,0],
                                                                 [0,1,1]]), np.array([[0,0,0],
                                                                                      [1,1,1],
                                                                                      [1,0,0]]), np.array([[1,1,0],
                                                                                                           [0,1,0],
                                                                                                           [0,1,0]])]]
TETROMINO_J = [4, (0, 0, 255), [np.array([[1,0,0],
                                            [1,1,1],
                                            [0,0,0]]),np.array([[0,1,1],
                                                               [0,1,0],
                                                               [0,1,0]]), np.array([[0,0,0],
                                                                                    [1,1,1],
                                                                                    [0,0,1]]), np.array([[0,1,0],
                                                                                                         [0,1,0],
                                                                                                         [1,1,0]])]]
TETROMINO_Z = [5, (255, 0, 0), [np.array([[1,1,0],
                                            [0,1,1],
                                            [0,0,0]]),np.array([[0,0,1],
                                                               [0,1,1],
                                                               [0,1,0]]), np.array([[0,0,0],
                                                                                    [1,1,0],
                                                                                    [0,1,1]]), np.array([[0,1,0],
                                                                                                         [1,1,0],
                                                                                                         [1,0,0]])]]
TETROMINO_S = [6, (0, 255, 0), [np.array([[0,1,1],
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
        self.position = position #topleft corner
        self.color = TETROMINOS.get(type)[T_COLOR]
        self.matrice = TETROMINOS.get(type)[T_MATRICE][rotation] #matrice

    def applyOnBoard(self, board):#fonction appelé à chaque (affichage) + placement de la piece
        for i in range(len(self.matrice)):
            for j in range(len(self.matrice)):
                board[self.position[0] + i][self.position[1] + j] = self.matrice[i,j] * TETROMINOS.get(self.type)[T_TYPE]

    def goDown(self, board):
        # Board is used to see if the move is possible
        for i in range(len(self.matrice)):
            for j in range(len(self.matrice)):
                # Env colisions
                if (self.position[0] + i < 0 or self.position[0] + i > 9) and self.matrice[i][j] > 0:
                    return False
                if (self.position[1] + j + 1< 0 or self.position[1] + j + 1 > 19) and self.matrice[i][j] > 0:
                    return False
                # Board colisions
                if board[self.position[0], self.position[1] + 1] == 1:
                    return False
        self.position[1] = self.position[1] + 1
        return True

    def goLeft(self, board):
        # Board is used to see if the move is possible
        self.position[0] = self.position[0] - 1

    def goRight(self, board):
        # Board is used to see if the move is possible
        self.position[0] = self.position[0] + 1

    def goUP(self, board):
        # Board is used to see if the move is possible
        self.position[1] = self.position[1] + 1 # to be changed



# Chaque affichage
# toDrawBoard = deepcopy(board)
# playedTetromino.applyOnBoard(toDrawBoard)
# drawBoard(toDrawBoard)
