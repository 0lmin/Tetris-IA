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

TETROMINO_I = ["I", (0, 255, 255), [np.array([[0,0,0,0],
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
TETROMINO_O = ["O", (255, 255, 0), [np.array([[0,1,1,0],
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
TETROMINO_T = ["T", (170, 0, 255), [np.array([[0,1,0],
                                              [1,1,1],
                                              [0,0,0]]),np.array([[0,1,0],
                                                                 [0,1,1],
                                                                 [0,1,0]]), np.array([[0,0,0],
                                                                                      [1,1,1],
                                                                                      [0,1,0]]), np.array([[0,1,0],
                                                                                                           [1,1,0],
                                                                                                           [0,1,0]])]]
TETROMINO_L = ["L", (255, 165, 0), [np.array([[0,0,1],
                                              [1,1,1],
                                              [0,0,0]]),np.array([[0,1,0],
                                                                 [0,1,0],
                                                                 [0,1,1]]), np.array([[0,0,0],
                                                                                      [1,1,1],
                                                                                      [1,0,0]]), np.array([[1,1,0],
                                                                                                           [0,1,0],
                                                                                                           [0,1,0]])]]
TETROMINO_J = ["J", (0, 0, 255), [np.array([[1,0,0],
                                            [1,1,1],
                                            [0,0,0]]),np.array([[0,1,1],
                                                               [0,1,0],
                                                               [0,1,0]]), np.array([[0,0,0],
                                                                                    [1,1,1],
                                                                                    [0,0,1]]), np.array([[0,1,0],
                                                                                                         [0,1,0],
                                                                                                         [1,1,0]])]]
TETROMINO_Z = ["Z", (255, 0, 0), [np.array([[1,1,0],
                                            [0,1,1],
                                            [0,0,0]]),np.array([[0,0,1],
                                                               [0,1,1],
                                                               [0,1,0]]), np.array([[0,0,0],
                                                                                    [1,1,0],
                                                                                    [0,1,1]]), np.array([[0,1,0],
                                                                                                         [1,1,0],
                                                                                                         [1,0,0]])]]
TETROMINO_S = ["S", (0, 255, 0), [np.array([[0,1,1],
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
        for i in range(4):
            for j in range(4):
                board[self.position[0] + i][self.position[1] + j] = self.matrice[i][j]



# Chaque affichage
# toDrawBoard = deepcopy(board)
# playedTetromino.applyOnBoard(toDrawBoard)
# drawBoard(toDrawBoard)
