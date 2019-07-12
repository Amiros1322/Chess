from abc import ABCMeta
from LongMoves import LongMoves
class Horizontal(LongMoves):
    def horizontal_moves(self, b_board):
        squares = []
        squares.extend(self.long_moves(b_board, 0, 1))
        squares.extend(self.long_moves(b_board, 0, -1))
        squares.extend(self.long_moves(b_board, 1, 0))
        squares.extend(self.long_moves(b_board, -1, 0))
        return squares