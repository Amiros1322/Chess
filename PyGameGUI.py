import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    MOUSEBUTTONDOWN,
)

# init pygame
pygame.init()

# Player sprite class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 255))  # This is supposed to be the image
        self.rect = self.surf.get_rect()

# settings, constants
pygame.display.set_caption("Chess")
FPS = 60
clock = pygame.time.Clock()
SCREEN_WIDTH, SCREEN_HEIGHT = 700, 700
BOARD_LENGTH = 8

# start window (returns surface)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = Player()
king_img = pygame.image.load('images/King.png')
queen_img = pygame.image.load('images/queen.png')
images_2d = [[None for i in range(BOARD_LENGTH)] for j in range(BOARD_LENGTH)]  # Makes 2d list with Nones
SQUARE_LENGTH = 85

# fills empty board sizes with corresponding
def draw_board(board):
    for row in range(BOARD_LENGTH):
        for col in range(BOARD_LENGTH):
            if board[row][col] is None:
                board[row][col] = pygame.Surface((SQUARE_LENGTH, SQUARE_LENGTH))
                if (row + col) % 2 == 0:
                    board[row][col].fill((250, 250, 250))  # White
                else:
                    board[row][col].fill((128, 128, 128))  # Grey

def render_board(board):
    # Fill background with white
    screen.fill((0, 0, 0))
    for row in range(8):
        for col in range(8):
            screen.blit(board[row][col], (row * SQUARE_LENGTH, col * SQUARE_LENGTH))

def draw_image(board):
    # king starting position
    board[2][2] = king_img
    board[5][4] = queen_img


print(images_2d)
draw_image(images_2d)

print(images_2d[2][2])
print(images_2d[5][4])
# Make surfaces for each squares and fill with colored surface if empty
draw_board(images_2d)

# run loop
running = True
while running:
    # set game to run at 60 FPS. (changing this will change 'speed' of the game)
    clock.tick(FPS)

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        # blit (block transfer) of the surface onto the screen. Tuple is draw location
        # screen.blit(king_img, (0, 0))


    render_board(images_2d)

    # Flip display
    pygame.display.flip()

pygame.quit()


