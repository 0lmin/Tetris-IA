import sys, pygame

#  Variables

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

BOARD_LEFT = SCREEN_WIDTH / 3
BOARD_TOP = SCREEN_HEIGHT / 20
BOARD_WIDTH = SCREEN_WIDTH / 3
BOARD_HEIGHT = SCREEN_HEIGHT - 2 * SCREEN_HEIGHT / 20

DOT_SPACE_WIDTH = BOARD_WIDTH / 10
DOT_SPACE_HEIGHT = BOARD_HEIGHT / 20
DOT_RADIUS = 3

LEVEL = 0
SCORE = 0

# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

# Init pygame environment
pygame.init()

# Create surface
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Draw the board
pygame.draw.rect(screen, WHITE, pygame.Rect((BOARD_LEFT, BOARD_TOP), (BOARD_WIDTH, BOARD_HEIGHT)), 2)
for i in range(1, 11):
    for j in range(1, 21):
        pygame.draw.circle(screen, WHITE, (BOARD_LEFT - DOT_SPACE_WIDTH / 2 + i * DOT_SPACE_WIDTH, BOARD_TOP - DOT_SPACE_HEIGHT / 2 + j * DOT_SPACE_HEIGHT), DOT_RADIUS)

# Draw the title
font = pygame.font.Font('freesansbold.ttf', 32)
title = font.render("Tetris", True, WHITE, BLACK)
titleRect = title.get_rect()
titleRect.center = (BOARD_LEFT + BOARD_WIDTH / 2, BOARD_TOP)
screen.blit(title, titleRect)

# Draw Stats
pygame.draw.rect(screen, WHITE, pygame.Rect((10, BOARD_HEIGHT / 4), (BOARD_WIDTH - 15, BOARD_HEIGHT / 3)), 2)

font = pygame.font.Font('freesansbold.ttf', 32)
levelText = font.render("Level : " +str(LEVEL), True, WHITE, BLACK)
levelTextRect = levelText.get_rect()
levelTextRect.center = (BOARD_WIDTH / 2 - 7, BOARD_HEIGHT / 4 + 30)
screen.blit(levelText, levelTextRect)

font = pygame.font.Font('freesansbold.ttf', 32)
scoreText = font.render("Score : " + str(SCORE), True, WHITE, BLACK)
scoreTextRect = scoreText.get_rect()
scoreTextRect.center = (BOARD_WIDTH / 2 - 7, BOARD_HEIGHT / 4 + 100)
screen.blit(scoreText, scoreTextRect)

# Game loop
while 1:
    # Enable exit the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    font = pygame.font.Font('freesansbold.ttf', 32)
    levelText = font.render("Level : " +str(LEVEL), True, WHITE, BLACK)
    levelTextRect = levelText.get_rect()
    levelTextRect.center = (BOARD_WIDTH / 2 - 7, BOARD_HEIGHT / 4 + 30)
    screen.blit(levelText, levelTextRect)

    font = pygame.font.Font('freesansbold.ttf', 32)
    scoreText = font.render("Score : " + str(SCORE), True, WHITE, BLACK)
    scoreTextRect = scoreText.get_rect()
    scoreTextRect.center = (BOARD_WIDTH / 2 - 7, BOARD_HEIGHT / 4 + 100)
    screen.blit(scoreText, scoreTextRect)

    pygame.display.flip()
