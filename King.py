import math
from Piece import Piece
from Rook import Rook


class King(Piece):

    def __init__(self, x, y, color, sprite=None):
        super().__init__(x, y, color, sprite=sprite)
        self.can_castle = True

    def __str__(self):
        if self.color == "white":
            return 'k'
        return 'K'

    @staticmethod
    def __name__():
        return "King"

    def move(self, new_x, new_y, board):
        delta_x = self.x - new_x

        # reminder: queenside rook at x=0, kingside rook at x=7

        # Check for castling
        if math.fabs(delta_x) > 1:

            if delta_x > 0:
                # Queenside Castle
                board.back_board[self.y][0].move(new_x + 1, new_y, board)
            else:
                # Kingside Castle
                board.back_board[self.y][7].move(new_x - 1, new_y, board)

        super(King, self).move(new_x, new_y, board)

    "TODO: possible improvement here, making a nested for loop (1 loop for each coordinate - each \
    runs through the three possibilities for that coordinate, and checks if it is open or not with \
    try except."

    def poss_moves(self, board):
        squares = [(self.x + 1, self.y), (self.x + 1, self.y + 1), (self.x, self.y + 1),
                   (self.x - 1, self.y + 1), (self.x - 1, self.y), (self.x - 1, self.y - 1),
                   (self.x, self.y - 1), (self.x + 1, self.y + 1)]

        if (self.color == "white" and board.can_castle_white) or (self.color == "black" and board.can_castle_black):

            # if can castle king is on starting square. Checks that empty squares between king and rook.
            if board.back_board[self.y][self.x + 1] is None and board.back_board[self.y][self.x + 2] is None and \
                    type(board.back_board[self.y][self.x + 3]) is Rook:
                squares.append((self.x + 2, self.y))

            if board.back_board[self.y][self.x - 1] is None and board.back_board[self.y][self.x - 2] is None and \
                board.back_board[self.y][self.x - 3] is None and type(board.back_board[self.y][self.x - 4]) is Rook:
                squares.append((self.x - 2, self.y))

        # Removes blocked squares
        i = 0
        while i < len(squares):
            try:
                y = squares[i][1]
                x = squares[i][0]
                if min(squares[i]) < 0 or max(squares[i]) > 7 or board.back_board[y][x].color == self.color:
                    squares.remove(squares[i])
                    i -= 1
            except:
                print("King Exception", i)
                pass
            i += 1
        return squares
