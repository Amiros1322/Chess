from Piece import Piece
from Diagonal import Diagonal
from Horizontal import Horizontal
class Queen(Piece, Diagonal, Horizontal):

    def __init__(self, x, y, color, sprite=None):
        super().__init__(x, y, color, sprite=sprite)

    def __str__(self):
        if self.color == "white":
            return 'q'
        return 'Q'

    @staticmethod
    def __name__():
        return "Queen"

    def poss_moves(self, board):
        squares = self.all_diag(board.back_board)
        squares.extend(self.horizontal_moves(board.back_board))
        return squares
