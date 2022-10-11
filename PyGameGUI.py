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
from King import King
from Helper import val_move, val_select, switch_turn

FPS = 24  # Chess doesnt need a high fps.
SCREEN_WIDTH, SCREEN_HEIGHT = 700, 700
BOARD_LENGTH = 8
SQUARE_LENGTH = 85

# Options for manual debugging
IGNORE_TURNS = True
MOVE_ANYWHERE = True

clock = pygame.time.Clock()
pygame.display.set_caption("Chess")

# default theme brown. TODO: Change theme option
# darker color should be on the right. Otherwise square color inversed
color_theme = {"Brown": ("#964d22", "#964d37"), "Green": ("#eeeed2", "#769656")}
color1, color2 = color_theme["Green"]

# start window (returns surface)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

selected_img = pygame.image.load('images/selected_mark.png')
sprite_sh_img1 = pygame.image.load('images/output-onlinepngtools - Copy.png')
sprite_sh_img2 = pygame.image.load('images/Chess_spritesheet.png')

bounding_size = 100
bounding_size2 = 126
sprite_sheet1 = PieceSpriteSheet(sprite_sh_img1, bounding_size, white_top=False,
                                 piece_order=("king", "queen", "rook", "bishop",
                                              "knight", "pawn"),
                                 delta_x=168, delta_y=143, start_x=22, start_y=22)

sprite_sheet2 = PieceSpriteSheet(sprite_sh_img2, bounding_size2, white_top=True,
                                 piece_order=("king", "queen", "bishop", "knight", "rook", "pawn"),
                                 delta_x=141, delta_y=141, start_x=42, start_y=36, background_color=(247, 247, 247))

sprite_sheet = sprite_sheet1

images_2d = [[None for i in range(BOARD_LENGTH)] for j in range(BOARD_LENGTH)]  # Makes 2d list with Nones


# creates 2 surfaces to use for drawing.
def draw_board_surfaces(c1, c2):
    surf_1 = pygame.Surface((SQUARE_LENGTH, SQUARE_LENGTH))
    surf_1.fill(c1)

    surf_2 = pygame.Surface((SQUARE_LENGTH, SQUARE_LENGTH))
    surf_2.fill(c2)

    return surf_1, surf_2


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
        sprites[piece] = {
            "white": piece_spsh.get_image(piece, True, SQUARE_LENGTH, SQUARE_LENGTH),
            "black": piece_spsh.get_image(piece, False, SQUARE_LENGTH, SQUARE_LENGTH)}

    sprites["select_mark"] = select_mark_image
    return sprites


# given a piece and its valid moves, updates the board and changes the valid move.
def update_possible_moves(piece: Piece, board: Board):
    new_moves = piece.poss_moves(board.back_board)
    log_board.show_selection(new_moves)
    return new_moves


# Make surfaces for each squares and fill with colored surface if empty
surf_1, surf_2 = draw_board_surfaces(color1, color2)

# Make board
sprite_dict = create_sprite_dict(sprite_sheet, select_mark_image=selected_img)
log_board = Board(sprite_dict=sprite_dict)

# loop variables
selected = None  # selected piece. Its moves will be shown
moves = None  # valid squares the selected piece can move to. None is no selected piece
turn = "white"  # which color can move
game_end = False  # Has the game ended

# run loop
running = True
while running:
    # set game FPS. (changing this will change 'speed' of the game)
    clock.tick(FPS)

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == KEYDOWN:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == MOUSEBUTTONDOWN:
            if game_end:
                break

            # Clicking a square
            if event.button == 1:  # 1 specifies the left mouse button
                moved = False
                row, col = get_mouse_board_coordinates(
                    SQUARE_LENGTH)  # gets row, col of the board where mouse held down

                # Checking that something is selected, that it is not moving to its own square, and that either the square
                # it is moving to is valid or MOVE_ANYWHERE=True
                if selected is not log_board.back_board[col][row] and val_move((row, col), moves) or \
                        (MOVE_ANYWHERE and moves is not None):
                    log_board.move_piece(selected.x, selected.y, row, col)
                    log_board.clear_selection()

                    turn = switch_turn(turn)
                    selected = None
                    moved = True

                # If a piece is clicked its possible moves are retrieved and shown on screen
                if isinstance(log_board.back_board[col][row], Piece) and (
                        IGNORE_TURNS or turn == log_board.back_board[col][row].color):
                    selected = log_board.back_board[col][row]
                    moves = update_possible_moves(selected, log_board)

                # Clear board if an empty square clicked
                if moved or log_board.back_board[col][row] is None:
                    log_board.clear_selection()
                    moves = None

    # check for mate
    if log_board.game_end:
        print(f"{log_board.winner} has won!")
        game_end = True

    # renders board in checkerboard pattern with
    render_board_2_surf(log_board.back_board, surf_1, surf_2)

    # Flip display
    pygame.display.flip()

pygame.quit()
