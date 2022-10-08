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
    MOUSEBUTTONUP
)

from Board import Board
from SpriteSheet import PieceSpriteSheet
from Piece import Piece
from Helper import val_move, val_select

FPS = 24  # Chess doesnt need a high fps.
SCREEN_WIDTH, SCREEN_HEIGHT = 700, 700
BOARD_LENGTH = 8
SQUARE_LENGTH = 85

clock = pygame.time.Clock()
pygame.display.set_caption("Chess")

# default theme brown. TODO: Change theme option
# darker color should be on the right. Otherwise square color inversed
color_theme = {"Brown": ("#964d22", "#964d37"), "Green": ("#eeeed2", "#769656")}
color1, color2 = color_theme["Green"]

# start window (returns surface)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

king_img = pygame.image.load('images/King.png')
queen_img = pygame.image.load('images/queen.png')
selected_img = pygame.image.load('images/selected_mark.png')
queen_img.set_colorkey((255, 255, 255))
sprite_sh_img = pygame.image.load('images/output-onlinepngtools.png')
bounding_size = 100
# king_img_spsh = pygame.Surface((bounding_size, bounding_size))
# king_img_spsh.blit(sprite_sh_img, (0, 0), (22, 22, bounding_size, bounding_size))
# king_img_spsh = pygame.transform.scale(king_img_spsh, (SQUARE_LENGTH, SQUARE_LENGTH))
# king_img_spsh.set_colorkey((0,0,0))

sprite_sheet = PieceSpriteSheet(sprite_sh_img, bounding_size, white_top=False,
                                piece_order=("king", "queen", "rook", "bishop",
                                             "knight", "pawn"),
                                delta_x=168, delta_y=143, start_x=22, start_y=22)
king_img_spsh = sprite_sheet.get_image("queen", False, (0, 0, 0), SQUARE_LENGTH, SQUARE_LENGTH)

images_2d = [[None for i in range(BOARD_LENGTH)] for j in range(BOARD_LENGTH)]  # Makes 2d list with Nones


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
                    screen.blit(king_img, (row * SQUARE_LENGTH, col * SQUARE_LENGTH))


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

            if isinstance(piece_board[col][row], Piece):
                screen.blit(piece_board[col][row]._sprite, coords)
            elif isinstance(piece_board[col][row], pygame.Surface):
                screen.blit(piece_board[col][row], coords)


def get_mouse_board_coordinates(square_len):
    mx, my = pygame.mouse.get_pos()
    row, col = mx // square_len, my // square_len
    return row, col


# Given a spritesheet of chess pieces, returns a dictionary mapping each piece type to its sprite:
# {piece_name: {white: piece white sprite, black: piece black sprite}...}
def create_sprite_dict(piece_spsh: PieceSpriteSheet, select_mark_image):
    sprites = dict()
    pieces = ("pawn", "knight", "bishop", "rook", "queen", "king")
    for piece in pieces:
        sprites[piece] = {"white": piece_spsh.get_image(piece, True, (0, 0, 0), SQUARE_LENGTH, SQUARE_LENGTH),
                             "black": piece_spsh.get_image(piece, False, (0, 0, 0), SQUARE_LENGTH, SQUARE_LENGTH)}

    sprites["select_mark"] = select_mark_image
    return sprites


# Make surfaces for each squares and fill with colored surface if empty
surf_1, surf_2 = draw_board_surfaces(color1, color2)

# Make board
sprite_dict = create_sprite_dict(sprite_sheet, select_mark_image=selected_img)
log_board = Board(sprite_dict=sprite_dict)

# loop variables
mouse_held_down = False  # Is left mouse button held down?
selected = None

# run loop
running = True
while running:
    # set game FPS. (changing this will change 'speed' of the game)
    clock.tick(FPS)

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == MOUSEBUTTONDOWN:

            # Clicking a square
            if event.button == 1:  # 1 specifies the left mouse button
                if not mouse_held_down:
                    row, col = get_mouse_board_coordinates(
                        SQUARE_LENGTH)  # gets row, col of the board where mouse held down
                    mouse_held_down = True

                    # If a piece is clicked its possible moves are shown.
                    if isinstance(log_board.back_board[col][row], Piece):
                        selected = log_board.back_board[col][row]
                        print(f"{selected} was selected")
                        moves = selected.poss_moves(log_board.back_board)
                        log_board.show_selection(moves)

        elif event.type == MOUSEBUTTONUP:
            # Mouse Drag: letting go
            if event.button == 1:
                row, col = get_mouse_board_coordinates(SQUARE_LENGTH)

                # isinstance checks for selected surface in practice
                if selected is not None:
                    print(f"{selected} let go at ({row}, {col})")

                    # Checking if it was just clicked or is being dragged
                    if selected is not log_board.back_board[col][row] and isinstance(log_board.back_board[col][row], pygame.Surface):
                        selected.move(row, col, log_board)
                        log_board.clear_selection()
                        selected = None



                mouse_held_down = False

    # renders board in checkerboard pattern with
    render_board_2_surf(log_board.back_board, surf_1, surf_2)

    # Flip display
    pygame.display.flip()

pygame.quit()

