from abc import ABCMeta, abstractmethod
from copy import deepcopy, copy
import math


class Piece(object, metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, x, y, color, sprite=None):

        # add a check that the sprite is actually a sprite
        if sprite is None:
            self._is_gui = False
        else:
            self._is_gui = True
        self._sprite = sprite


        self.x = x
        self.y = y
        self.color = color

    # move: moves a piece from it's current location to the specified one.
    def move(self, new_x, new_y, board):

        # deletes en_passant if it wasn't eaten en_passant.
        # if Pawns.en_passant:
        #       board.str_board[self.y - 1][self.x] = "_"
        # board.back_board[self.y - 1][self.x] = None
        # self.en_passant.clear()

        # TODO:implement en passant by creating another pointer to the eatable pawn in the square you can eat it on.
        # Represent this on the string_board. You will be able to eat it normally by eating the ccpy.

        board.back_board[self.y][self.x] = None
        board.back_board[new_y][new_x] = self
        board.str_board[self.y][self.x] = self.empty_vis()
        board.str_board[new_y][new_x] = self.visualization()

        # Removes piece taken piece if taking en passant
        if board.en_passant and new_x == board.en_passant[0] and new_y == board.en_passant[1] and str(self) in ('p', 'P'):
            board.back_board[self.y][new_x] = None
            print(f"Delete {(self.y, new_x)}")

        board.en_passant = None

        # # setting en passant if pawn moved 2 squares.
        if str(self) in ('p', 'P') and math.fabs(self.y - new_y) == 2:
            if self.color == "white":
                board.en_passant = (self.x, new_y + 1)
            else:
                board.en_passant = (self.x, new_y - 1)
            print(board.en_passant)

        self.x = new_x
        self.y = new_y

        # promotion check (Replaces piece with a new one)
        if self.__name__ == "Pawn":
            # Promotion
            if new_y == 7 or new_y == 0:
                self.promote(board)

    # given a list of possible moves for the piece, it returns a list with only the elements that are on the board and
    # unoccupied by an enemy piece. Moves are in a tuple format (x value, y value).
    def valid_moves(self, poss_moves, back_board):
        def valid_move(move):
            x = move[0]
            y = move[1]
            # TODO: See if using type + issubclass is faster than isinstance with an abstract class
            if (
                    min(move) < 0 or max(move) > 7 or
                    (issubclass(type(back_board[y][x]), Piece) and back_board[y][x].color == self.color)
            ):
                return False
            return True

        poss_moves = filter(valid_move, poss_moves)
        return list(poss_moves)

    def visualization(self):
        if self._is_gui:
            if self._sprite is not None:
                return copy(self._sprite)
            else:
                raise ValueError
        else:
            return str(self)

    def empty_vis(self):
        if self._is_gui:
            # The sprite if there is nothing there (empty square returned on None)
            return None
        else:
            return '_'
