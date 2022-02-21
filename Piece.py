from abc import ABCMeta, abstractmethod
import math


class Piece(object, metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, x, y, color):
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
        board.str_board[self.y][self.x] = "_"
        board.str_board[new_y][new_x] = str(self)

        # en passant checl
        if self.__name__ == "Pawn" and math.fabs(self.y - new_y) == 2:
            board.back_board[self.y][self.x] = self
            board.str_board[self.y][self.x] = "-"
            self.en_passant.append()

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
        i = 0
        while i < len(poss_moves):
            x = poss_moves[i][0]
            y = poss_moves[i][1]
            if (
                    min(poss_moves[i]) < 0 or max(poss_moves[i]) > 7 or
                    (back_board[y][x] is not None and back_board[y][x].color == self.color)
            ):
                poss_moves.remove(poss_moves[i])
                i -= 1
            i += 1
        return poss_moves
