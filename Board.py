import pygame
import numpy as np
import Tetromino
import functools
import time
import copy
import sys

# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

#  Variables

## Can be configured by the user
MAIN_COLOR = BLACK
SECONDARY_COLOR = WHITE

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

FONT = "freesansbold.ttf" # Give a list ?
FONT_SIZE = 32 # Confirable ?

## Can't be configured
BOARD_LEFT = int(SCREEN_WIDTH / 3)
BOARD_TOP = int(SCREEN_HEIGHT / 20)
BOARD_WIDTH = int(SCREEN_WIDTH / 3)
BOARD_HEIGHT = int(SCREEN_HEIGHT - (2 * SCREEN_HEIGHT / 20))

DOT_SPACE_WIDTH = int(BOARD_WIDTH / 10)
DOT_SPACE_HEIGHT = int(BOARD_HEIGHT / 20)
DOT_RADIUS = int(BOARD_LEFT / 100)

SCREEN_BORDER = 15
GRAVITY_TICK = 500

TETROMINOS_COLOR = [(255,255,255),(0, 255, 255), (255, 255, 0), (170, 0, 255), (255, 165, 0), (0, 0, 255), (255, 0, 0), (0, 255, 0),(255,255,255)]
TETROMINOS_LIST = ["I", "O", "T", "L", "J", "Z", "S"]

T_TYPE=0
T_COLOR=1
T_MATRICE=2

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

##
SCORE = [0, 40, 100, 300, 1200]
Leaderboard = [["Clément", 9999], ["Axel", -1]]

class Board:
    def __init__(self):
        ## Init pygame environment
        pygame.init()

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.board = np.zeros((10, 20), np.int8)
        self.level = 0
        self.score = 0
        self.nbLine = 0

        self.isStoreOpen = True
        self.store = None

        self.next = [None, None, None]

        # Gravity event
        pygame.key.set_repeat(300,100)
        pygame.time.set_timer(pygame.USEREVENT,GRAVITY_TICK)

    def fillStore(self):
        self.next[0] = Tetromino.Tetromino().generateTetromino()
        self.next[1] = Tetromino.Tetromino().generateTetromino()
        self.next[2] = Tetromino.Tetromino().generateTetromino()

    def nextT(self):
        self.isStoreOpen = True
        t = self.next[0]
        self.next[0] = self.next[1]
        self.next[1] = self.next[2]
        self.next[2] = Tetromino.Tetromino().generateTetromino()
        return t

    def draw(self):
        ## Draw board border
        self.screen.fill(MAIN_COLOR)
        pygame.draw.rect(self.screen, SECONDARY_COLOR, pygame.Rect((BOARD_LEFT, BOARD_TOP), (BOARD_WIDTH, BOARD_HEIGHT)), 2)
        font = pygame.font.Font(FONT, FONT_SIZE)
        title = font.render("Tetris", True, SECONDARY_COLOR, MAIN_COLOR)
        titleRect = title.get_rect()
        titleRect.center = (BOARD_LEFT + int(BOARD_WIDTH / 2), BOARD_TOP)
        self.screen.blit(title, titleRect)

        # Draw Stats border
        pygame.draw.rect(self.screen, SECONDARY_COLOR, pygame.Rect((SCREEN_BORDER, int(BOARD_HEIGHT / 4)), (BOARD_WIDTH - (2 * SCREEN_BORDER), 3 * SCREEN_BORDER + 2 * FONT_SIZE)), 2)# BOARD_HEIGHT / 4)), 2)

        # Draw dots
        for i in range(1, 11):
            for j in range(1, 21):
                pygame.draw.circle(self.screen, SECONDARY_COLOR,
                    (BOARD_LEFT - int(DOT_SPACE_WIDTH / 2) + (i * DOT_SPACE_WIDTH), BOARD_TOP - int(DOT_SPACE_HEIGHT / 2) + j * DOT_SPACE_HEIGHT), DOT_RADIUS)

        # Draw Stats border
        pygame.draw.rect(self.screen, SECONDARY_COLOR, pygame.Rect((SCREEN_BORDER, int(BOARD_HEIGHT / 4)), (BOARD_WIDTH - (2 * SCREEN_BORDER), 3 * SCREEN_BORDER + 2 * FONT_SIZE)), 2)# BOARD_HEIGHT / 4)), 2)

        # Draw Stats
        font = pygame.font.Font(FONT, FONT_SIZE)
        levelText = font.render("Level : " +str(self.level), True, SECONDARY_COLOR, MAIN_COLOR)
        levelTextRect = levelText.get_rect()
        levelTextRect.topleft = (2 * SCREEN_BORDER, int(BOARD_HEIGHT / 4) + SCREEN_BORDER)
        self.screen.blit(levelText, levelTextRect)

        font = pygame.font.Font(FONT, FONT_SIZE)
        scoreText = font.render("Score : " + str(self.score), True, SECONDARY_COLOR, MAIN_COLOR)
        scoreTextRect = scoreText.get_rect()
        scoreTextRect.topleft = (2 * SCREEN_BORDER, int(BOARD_HEIGHT / 4) + (2 * SCREEN_BORDER + FONT_SIZE))
        self.screen.blit(scoreText, scoreTextRect)

    def drawNext(self):
        # Drax the next Tetrominos
        for k in range(3):
            for i in range(len(self.next[k].matrice)):
                for j in range(len(self.next[k].matrice)):
                    cell = self.next[k].matrice[i][j]
                    if(cell != 0):
                        rectOrigin = (int(2 * SCREEN_WIDTH / 3) + k * int(SCREEN_WIDTH / 10) + SCREEN_BORDER + (i * DOT_SPACE_WIDTH) +1, BOARD_TOP + j * DOT_SPACE_HEIGHT +1)
                        rectSize = (DOT_SPACE_WIDTH -2, DOT_SPACE_HEIGHT -2)
                        rectToDraw = pygame.Rect( rectOrigin, rectSize )
                        pygame.draw.rect(self.screen, TETROMINOS.get(self.next[k].type)[T_COLOR], rectToDraw)

    def drawStore(self):
        if self.store == None:
            return
        # Drax the next Tetrominos
        for i in range(len(self.store.matrice)):
            for j in range(len(self.store.matrice)):
                cell = self.store.matrice[i][j]
                if(cell != 0):
                    rectOrigin = (SCREEN_BORDER + (i * DOT_SPACE_WIDTH) +1, BOARD_TOP + j * DOT_SPACE_HEIGHT +1)
                    rectSize = (DOT_SPACE_WIDTH -2, DOT_SPACE_HEIGHT -2)
                    rectToDraw = pygame.Rect( rectOrigin, rectSize )
                    pygame.draw.rect(self.screen, TETROMINOS.get(self.store.type)[T_COLOR], rectToDraw)

    def drawBoard(self,board):
        self.draw()
        for i in range(0, 10):
            for j in range(0, 20):
                cell = board[i][j]
                if(cell != 0):
                    rectOrigin = (BOARD_LEFT + (i * DOT_SPACE_WIDTH) +1, BOARD_TOP + j * DOT_SPACE_HEIGHT +1)
                    rectSize = (DOT_SPACE_WIDTH -2, DOT_SPACE_HEIGHT -2)
                    rectToDraw = pygame.Rect( rectOrigin, rectSize )
                    pygame.draw.rect(self.screen, TETROMINOS_COLOR[cell], rectToDraw) ##2nd argument should be replaced by color
        self.drawNext()
        self.drawStore()

    def nextLevel(self):
        # Update gravity tick
        self.level += 1

    def deleteFullLine(self):
        test = 0
        # Delete full line
        for j in range(20):
            for i in range(10):
                if self.board[i][j] == 0:
                    break
            if i == 9 and self.board[i][j] != 0:
                test += 1
                for k in range(10):
                    self.board[k][j] = 8
        if test > 0:
            self.drawBoard(self.board)
            pygame.display.flip()
            pygame.time.delay(200)
        # Delete full line
        for j in range(20):
            for i in range(10):
                if self.board[i][j] == 0:
                    break
            if i == 9 and self.board[i][j] != 0:
                self.nbLine += 1
                for k in range(10):
                    for l in range(j, 0, -1):
                        self.board[k][l] = self.board[k][l - 1]
                if self.nbLine % 10 == 0:
                    self.nextLevel()
        self.score += SCORE[test] * (self.level + 1)

    def goStore(self, currentT):
        if self.isStoreOpen:
            currentT.position = [2,0]
            self.isStoreOpen = False
            if self.store == None:
                self.store = currentT
                return self.nextT()
            else:
                tmp = copy.deepcopy(self.store)
                self.store = currentT
                return tmp
        return currentT

    def drawPause(self):
        self.screen.fill(MAIN_COLOR)
        font = pygame.font.Font(FONT, 100)
        pauseText = font.render("PAUSE", True, SECONDARY_COLOR, MAIN_COLOR)
        pauseTextRect = pauseText.get_rect()
        pauseTextRect.center = (SCREEN_WIDTH / 2, 100)
        self.screen.blit(pauseText, pauseTextRect)

        def drawKeyBinding(self, height_origin):
            lines = ["left and right : move lateraly tetromino", "down : fast forward", "up : place the tetromino", "n and b : rotate left and right", "space : store/swap", "escape : pause"]
            for i in range(len(lines)):
                font = pygame.font.Font(FONT, 30)
                helpText = font.render(lines[i], True, SECONDARY_COLOR, MAIN_COLOR)
                helpTextRect = helpText.get_rect()
                helpTextRect.center = (SCREEN_WIDTH / 2, height_origin + i*50 + 100)
                self.screen.blit(helpText, helpTextRect)
        drawKeyBinding(self, SCREEN_HEIGHT / 2 - 200)

        pygame.display.flip()

    def pause(self):
        pygame.time.set_timer(pygame.USEREVENT,0)
        while True:
            self.drawPause()
            e = pygame.event.get()
            for event in e:
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    print("OUI")
                    if event.key == pygame.K_ESCAPE:
                        pygame.time.set_timer(pygame.USEREVENT,GRAVITY_TICK)
                        return
