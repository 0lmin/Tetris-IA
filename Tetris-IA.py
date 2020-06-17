import sys, pygame
import numpy as np

# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

#  Variables

## Can be configured by the user
MAIN_COLOR = WHITE
SECONDARY_COLOR = BLACK

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

##
level = 0
score = 0
Leaderboard = [["Clément", 9999], ["Axel", -1]]

#Methods
def drawBoard(board):
    for i in range(0, 10):
        for j in range(0, 20):
            if(board[i][j]==1):
                pygame.draw.rect(screen, GREEN,
                pygame.Rect(
                (BOARD_LEFT + (i * DOT_SPACE_WIDTH), BOARD_TOP + j * DOT_SPACE_HEIGHT),
                (DOT_SPACE_WIDTH, DOT_SPACE_HEIGHT)
                )
                )


# Main code

## Init pygame environment
pygame.init()

## Create surface
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
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

# Game loop
while 1:
    # Enable exit the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    # Draw dots
    for i in range(1, 11):
        for j in range(1, 21):
            pygame.draw.circle(screen, SECONDARY_COLOR,
                (BOARD_LEFT - int(DOT_SPACE_WIDTH / 2) + (i * DOT_SPACE_WIDTH), BOARD_TOP - int(DOT_SPACE_HEIGHT / 2) + j * DOT_SPACE_HEIGHT), DOT_RADIUS)

    # Draw board
    ## To be implemented after GUI
    ##board = [([0] * 21)] * 11 #BUG => same ref, deepcopy needed?
    board = np.zeros((10, 20), np.int8)#access via board[x][y]
    board[0][2] = 1
    ## Draw board
    drawBoard(board)

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
