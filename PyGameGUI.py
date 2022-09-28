import pygame
from SpriteSheet import *
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
#
# # init pygame
# pygame.init()
#
# # Player sprite class
# class Player(pygame.sprite.Sprite):
#     def __init__(self):
#         super(Player, self).__init__()
#         self.surf = pygame.Surface((75, 25))
#         self.surf.fill((255, 255, 255))  # This is supposed to be the image
#         self.rect = self.surf.get_rect()
#
# # settings, constants
FPS = 24 # Chess doesnt need a high fps.
SCREEN_WIDTH, SCREEN_HEIGHT = 700, 700
BOARD_LENGTH = 8
SQUARE_LENGTH = 85

clock = pygame.time.Clock()
pygame.display.set_caption("Chess")

# default theme brown. TODO: Change theme option
color_theme = {"Brown": ("#964d22", "#964d37"), "Green": ("#769656", "#eeeed2")}
color1, color2 = color_theme["Green"]

# start window (returns surface)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

king_img = pygame.image.load('images/King.png')
queen_img = pygame.image.load('images/queen.png')
queen_img.set_colorkey((255, 255, 255))
sprite_sh_img = pygame.image.load('images/output-onlinepngtools.png')
bounding_size = 100
# king_img_spsh = pygame.Surface((bounding_size, bounding_size))
# king_img_spsh.blit(sprite_sh_img, (0, 0), (22, 22, bounding_size, bounding_size))
# king_img_spsh = pygame.transform.scale(king_img_spsh, (SQUARE_LENGTH, SQUARE_LENGTH))
# king_img_spsh.set_colorkey((0,0,0))

sprite_sheet = PieceSpriteSheet(sprite_sh_img, bounding_size, white_top=False, piece_order=("king", "queen", "rook", "bishop",
                                                                                            "knight", "pawn"),
                                delta_x=166, delta_y=143, start_x=22, start_y=22)
king_img_spsh = sprite_sheet.get_image("queen", True, (0, 0, 0), SQUARE_LENGTH, SQUARE_LENGTH)


images_2d = [[None for i in range(BOARD_LENGTH)] for j in range(BOARD_LENGTH)]  # Makes 2d list with Nones


def extract_spritesheet_image(board, sprite_length, sprite_width, row, column):
    pass

# creates 2 surfaces to use for drawing.
def draw_board_surfaces(c1, c2):
    surf_1 = pygame.Surface((SQUARE_LENGTH, SQUARE_LENGTH))
    surf_1.fill(c1)

    surf_2 = pygame.Surface((SQUARE_LENGTH, SQUARE_LENGTH))
    surf_2.fill(c2)

    return surf_1, surf_2


def draw_board_64_surfaces(board):
    for row in range(BOARD_LENGTH):
        for col in range(BOARD_LENGTH):
            board[row][col] = pygame.Surface((SQUARE_LENGTH, SQUARE_LENGTH))
            if (row + col) % 2 == 0:
                board[row][col].fill(color1)  # White
            else:
                board[row][col].fill(color2)  # Grey

def draw_board_2_surfaces(board):
    for row in range(BOARD_LENGTH):
        for col in range(BOARD_LENGTH):
            board[row][col] = pygame.Surface((SQUARE_LENGTH, SQUARE_LENGTH))
            if (row + col) % 2 == 0:
                board[row][col].fill(color1)  # White
            else:
                board[row][col].fill(color2)  # Grey

def render_board(board):
    # Fill background with white
    screen.fill((255, 255, 255))
    for row in range(BOARD_LENGTH):
        for col in range(BOARD_LENGTH):
            if board[row][col] != None:
                screen.blit(board[row][col], (row * SQUARE_LENGTH, col * SQUARE_LENGTH))
                if row == 4 and col == 1:
                    screen.blit(king_img, (row*SQUARE_LENGTH, col*SQUARE_LENGTH))

def render_board_2_surf(piece_board, s1, s2):
    # Fill background with white
    screen.fill((255, 255, 255))
    for row in range(BOARD_LENGTH):
        for col in range(BOARD_LENGTH):
            coords = (row * SQUARE_LENGTH, col * SQUARE_LENGTH)

            if (row + col) % 2 == 0:
                screen.blit(s1, coords)
            else:  # (row + col) % 2 == 1
                screen.blit(s2, coords)

            if piece_board[row][col] != None:
                screen.blit(piece_board[row][col], coords)

def draw_image(board):
    # king starting position
    board[2][1] = king_img
    board[5][4] = pygame.transform.scale(queen_img, (SQUARE_LENGTH, SQUARE_LENGTH))
    board[5][4].set_colorkey((100,100,100))
    board[6][6] = king_img_spsh


# Make surfaces for each squares and fill with colored surface if empty
surf_1, surf_2 = draw_board_surfaces(color1, color2)
draw_image(images_2d)

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

    # renders board in checkerboard pattern with
    render_board_2_surf(images_2d, surf_1, surf_2)

    # Flip display
    pygame.display.flip()

pygame.quit()


# pygame.init()
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# image = pygame.image.load('images\King.png')
#
# run = True
# while run:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#
#     screen.fill(color2)
#
#     screen_w, screen_h = screen.get_size()
#     image_w, image_h = image.get_size()
#
#     for x in range(0, screen_w, image_w):
#         for y in range(0, screen_h, image_h):
#             screen.blit(image, (x, y))
#
#     pygame.display.flip()
#
# pygame.quit()
# exit()