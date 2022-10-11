from Piece import Piece
from Horizontal import Horizontal


class Rook(Piece, Horizontal):

    def __init__(self, x, y, color, sprite=None):
        super().__init__(x, y, color, sprite=sprite)

    def __str__(self):
        if self.color == "white":
            return 'r'
        return 'R'

    @staticmethod
    def __name__():
        return "Rook"

    def poss_moves(self, board):
        return self.horizontal_moves(board.back_board)
