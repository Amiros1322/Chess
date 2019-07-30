from abc import ABCMeta, abstractmethod
from LongMoves import LongMoves
class Diagonal(LongMoves):
    """  Returns a list of squares that the piece can reach by moving diagonally in one direction """
    def all_diag(self, back_board):
        squares = []
        squares.extend(self.long_moves(back_board, 1, 1))
        squares.extend(self.long_moves(back_board, -1, 1))
        squares.extend(self.long_moves(back_board, 1, -1))
        squares.extend(self.long_moves(back_board, -1, -1))
        return squares
