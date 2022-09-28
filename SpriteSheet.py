from typing import overload

import pygame


# Note: SpriteSheet class based on https://github.com/russs123/pygame_tutorials/blob/main/sprite_tutorial/spritesheet.py

# Assumes Sprites arranged in two rows - 1 for each color
class PieceSpriteSheet:

    piece_names = {"knight", "pawn", "rook", "king", "queen", "bishop",
                   "k", "p", "r", "k", "q", "b"}

    def __init__(self, image, square_length, white_top: bool, piece_order: tuple, delta_x, delta_y, start_x=0, start_y=0):
        self._validate_pieces(piece_order)
        self.sheet = image
        self.square_length = square_length  # length of square in board
        self.white_top = white_top  # whether the top row is white pieces or black
        self.piece_order = dict(zip(piece_order, range(len(piece_order))))  # dict of piece: piece location

        # delta - distance between sprites in each direction. start - start point for traversal
        self.delta_x = delta_x
        self.delta_y = delta_y
        self.start_x = start_x
        self.start_y = start_y

    def get_image(self, piece_name, is_white, background_color, scale_to_x, scale_to_y, width=None, height=None):

        # Checks for width/height input
        if width is None and height is None:
            width, height = self.square_length, self.square_length
        elif (width is not None and height is None) or (width is None and height is not None):
            raise Exception("Invalid width/height input")

        x, y = self._get_image_coords(is_white, piece_name)

        # create image
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0, 0), (x, y, width, height))
        image = pygame.transform.scale(image, (scale_to_x, scale_to_y))
        image.set_colorkey(background_color)

        return image

    def _validate_pieces(self, piece_order):
        pieces_copy = self.piece_names.copy()

        for piece in piece_order:

            # Better exception behavior than letting set throw exception
            if piece.lower() not in self.piece_names:
                raise Exception("Invalid piece name")

            if piece.lower() not in pieces_copy:
                raise Exception("Duplicate Pieces in piece")

            pieces_copy.remove(piece)

    def _get_image_coords(self, is_white, piece_name):

        # stays at start_y if piece is same color as top row. else goes down a row
        y = self.start_y
        if self.white_top != is_white:
            y += self.delta_y

        # changes x to correspond to piece_slot
        x = self.start_x + self.piece_order[piece_name] * self.delta_x

        return x, y