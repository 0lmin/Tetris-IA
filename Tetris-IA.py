import sys, pygame
import numpy as np
import copy
import random
import Tetromino

pygame.quit()

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

TETROMINOS_COLOR = [(0, 255, 255), (255, 255, 0), (170, 0, 255), (255, 165, 0), (0, 0, 255), (255, 0, 0), (0, 255, 0)]
TETROMINOS_LIST = ["I", "O", "T", "L", "J", "Z", "S"]

##
level = 0
score = 0
Leaderboard = [["Clément", 9999], ["Axel", -1]]

#Methods
def drawBoard(board):
    for i in range(0, 10):
        for j in range(0, 20):
            cell = board[i][j]
            if(board[i][j]!=0):
                pygame.draw.rect(screen, TETROMINOS_COLOR[cell], pygame.Rect( (BOARD_LEFT + (i * DOT_SPACE_WIDTH), BOARD_TOP + j * DOT_SPACE_HEIGHT),  (DOT_SPACE_WIDTH, DOT_SPACE_HEIGHT)))

def generateTetromino():
    return Tetromino.Tetromino(TETROMINOS_LIST[random.randint(0,6)], 0, [2,0])

# Main code

## Init pygame environment
pygame.init()

## Create surface
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Gravity event
pygame.key.set_repeat(300,100)
pygame.time.set_timer(pygame.USEREVENT,GRAVITY_TICK)

currentT = None

# Game loop
while 1:
    # Enable exit the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.USEREVENT:
            if not(currentT.goDown(board)):
                print("Lock")
        elif event.type == pygame.KEYDOWN:
            if event.key== pygame.K_DOWN:
                if currentT.goDown(board):
                    pygame.time.set_timer(pygame.USEREVENT,GRAVITY_TICK)
            elif event.key == pygame.K_LEFT:
                currentT.goLeft(board)
            elif event.key == pygame.K_RIGHT:
                currentT.goRight(board)
            elif event.key == pygame.K_UP:
                currentT.goUP(board)

    screen.fill(MAIN_COLOR)

    ## Draw board border
    pygame.draw.rect(screen, SECONDARY_COLOR, pygame.Rect((BOARD_LEFT, BOARD_TOP), (BOARD_WIDTH, BOARD_HEIGHT)), 2)
    font = pygame.font.Font(FONT, FONT_SIZE)
    title = font.render("Tetris", True, SECONDARY_COLOR, MAIN_COLOR)
    titleRect = title.get_rect()
    titleRect.center = (BOARD_LEFT + int(BOARD_WIDTH / 2), BOARD_TOP)
    screen.blit(title, titleRect)

    # Draw Stats border
    pygame.draw.rect(screen, SECONDARY_COLOR, pygame.Rect((SCREEN_BORDER, int(BOARD_HEIGHT / 4)), (BOARD_WIDTH - (2 * SCREEN_BORDER), 3 * SCREEN_BORDER + 2 * FONT_SIZE)), 2)# BOARD_HEIGHT / 4)), 2)


    # Draw dots
    for i in range(1, 11):
        for j in range(1, 21):
            pygame.draw.circle(screen, SECONDARY_COLOR,
                (BOARD_LEFT - int(DOT_SPACE_WIDTH / 2) + (i * DOT_SPACE_WIDTH), BOARD_TOP - int(DOT_SPACE_HEIGHT / 2) + j * DOT_SPACE_HEIGHT), DOT_RADIUS)

    # Draw board
    ## To be implemented after GUI
    ##board = [([0] * 21)] * 11 #BUG => same ref, deepcopy needed?
    board = np.zeros((10, 20), np.int8)#access via board[x][y]
    # board[0][2] = 1 #0 empty, [1;7] => colors
    # board[1][3] = 2
    ## Draw board
    # drawBoard(board)
    if(currentT == None):
        currentT = generateTetromino()
    changedBoard = copy.deepcopy(board)
    currentT.applyOnBoard(changedBoard)
    drawBoard(changedBoard)

    # Draw Stats
    font = pygame.font.Font(FONT, FONT_SIZE)
    levelText = font.render("Level : " +str(level), True, SECONDARY_COLOR, MAIN_COLOR)
    levelTextRect = levelText.get_rect()
    levelTextRect.topleft = (2 * SCREEN_BORDER, int(BOARD_HEIGHT / 4) + SCREEN_BORDER)
    screen.blit(levelText, levelTextRect)

    font = pygame.font.Font(FONT, FONT_SIZE)
    scoreText = font.render("Score : " + str(score), True, SECONDARY_COLOR, MAIN_COLOR)
    scoreTextRect = scoreText.get_rect()
    scoreTextRect.topleft = (2 * SCREEN_BORDER, int(BOARD_HEIGHT / 4) + (2 * SCREEN_BORDER + FONT_SIZE))
    screen.blit(scoreText, scoreTextRect)

    pygame.display.flip()
