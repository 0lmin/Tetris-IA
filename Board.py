import pygame
import numpy as np
import Tetromino
import functools
import time

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

##
level = 0
score = 0
Leaderboard = [["Clément", 9999], ["Axel", -1]]

class Board:
    def __init__(self):
        ## Init pygame environment
        pygame.init()

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.board = np.zeros((10, 20), np.int8)
        self.level = 0
        self.score = 0

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
        levelText = font.render("Level : " +str(level), True, SECONDARY_COLOR, MAIN_COLOR)
        levelTextRect = levelText.get_rect()
        levelTextRect.topleft = (2 * SCREEN_BORDER, int(BOARD_HEIGHT / 4) + SCREEN_BORDER)
        self.screen.blit(levelText, levelTextRect)

        font = pygame.font.Font(FONT, FONT_SIZE)
        scoreText = font.render("Score : " + str(score), True, SECONDARY_COLOR, MAIN_COLOR)
        scoreTextRect = scoreText.get_rect()
        scoreTextRect.topleft = (2 * SCREEN_BORDER, int(BOARD_HEIGHT / 4) + (2 * SCREEN_BORDER + FONT_SIZE))
        self.screen.blit(scoreText, scoreTextRect)

    def drawNext(self):
        # Drax the next Tetrominos
        for i in range(3):
            print(next[i].type)

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

    def deleteFullLine(self):
        test = False
        # Delete full line
        for j in range(20):
            for i in range(10):
                if self.board[i][j] == 0:
                    break
            if i == 9 and self.board[i][j] != 0:
                test = True
                for k in range(10):
                    self.board[k][j] = 8
        if test:
            self.drawBoard(self.board)
            pygame.display.flip()
            pygame.time.delay(200)
        # Delete full line
        for j in range(20):
            for i in range(10):
                if self.board[i][j] == 0:
                    break
            if i == 9 and self.board[i][j] != 0:
                for k in range(10):
                    for l in range(j, 0, -1):
                        self.board[k][l] = self.board[k][l - 1]
