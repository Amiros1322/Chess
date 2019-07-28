from Piece import Piece
from Horizontal import Horizontal


class Rook(Piece, Horizontal):

    def __init__(self, x, y, color):
        super().__init__(x, y, color)

    def __str__(self):
        if self.color == "white":
            return 'r'
        return 'R'

    @staticmethod
    def __name__():
        return "Rook"

    def poss_moves(self, b_board):
        return self.horizontal_moves(b_board)
