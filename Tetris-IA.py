import copy
import pygame
import random
import Tetromino
import Board
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

TETROMINOS_COLOR = [(0,0,0),(0, 255, 255), (255, 255, 0), (170, 0, 255), (255, 165, 0), (0, 0, 255), (255, 0, 0), (0, 255, 0)]
TETROMINOS_LIST = ["I", "O", "T", "L", "J", "Z", "S"]

# Main code

mainBoard = Board.Board()

currentT = Tetromino.Tetromino().generateTetromino()

# Game loop
while 1:
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.USEREVENT:
            if not(currentT.goDown(mainBoard.board)):
                currentT.applyOnBoard(mainBoard.board) #lock
                currentT = currentT.generateTetromino()
        elif event.type == pygame.KEYDOWN:
            if event.key== pygame.K_DOWN:
                if currentT.goDown(mainBoard.board):
                    pygame.time.set_timer(pygame.USEREVENT,GRAVITY_TICK)
            elif event.key == pygame.K_LEFT:
                currentT.goLeft(mainBoard.board)
            elif event.key == pygame.K_RIGHT:
                currentT.goRight(mainBoard.board)
            elif event.key == pygame.K_UP:
                currentT.goUP(mainBoard.board)
                currentT.applyOnBoard(mainBoard.board) #lock
                currentT = currentT.generateTetromino()
            elif event.key == pygame.K_b:
                currentT.rotateLeft(mainBoard.board)
            elif event.key == pygame.K_n:
                currentT.rotateRight(mainBoard.board)

    # Draw screen
    mainBoard.draw()

    # Draw board
    mainBoard.deleteFullLine() # Add score + add level
    changedBoard = copy.deepcopy(mainBoard.board)
    if currentT.applyOnBoard(changedBoard):
        # Game over
        print("C'est perdu")
        sys.exit()
    mainBoard.drawBoard(changedBoard)

    pygame.display.flip()
