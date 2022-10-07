from Piece import Piece
from Diagonal import Diagonal

class Bishop(Piece, Diagonal):

    def __init__(self, x, y, color, sprite=None):
        super().__init__(x, y, color, sprite=sprite)

    def __str__(self):
        if self.color == "white":
            return 'b'
        return 'B'

    @staticmethod
    def __name__():
        return "Bishop"

    def poss_moves(self, back_board):
        return self.all_diag(back_board)


