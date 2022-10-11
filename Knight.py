from Piece import Piece
class Knight(Piece):

    def __init__(self, x, y, color, sprite=None):
        super().__init__(x, y, color, sprite=sprite)

    def __str__(self):
        if self.color == "white":
            return 'n'
        return 'N'

    @staticmethod
    def __name__():
        return "Knight"

    # returns in proper (x, y) format
    def old_poss_moves(self, board):
        squares = [(self.x + 1, self.y + 2), (self.x + 2, self.y + 1), (self.x + 2, self.y - 1),
                   (self.x + 1, self.y - 2), (self.x - 1, self.y - 2), (self.x - 2, self.y - 1),
                   (self.x - 2, self.y + 1), (self.x - 1, self.y + 2)]

        # Possible exceptions: None does not have color. In this case we don't delete the square
        # loops over the squares and deletes invalid squares. Stops once it makes a full iteration without deleting
        # anything.
        i = 0
        while i < len(squares):
            try:
                mn = min(squares[i])
                mx = max(squares[i])
                if mn < 0 or mx > 7 or board[squares[i][1]][squares[i][0]].color == self.color:
                    squares.remove(squares[i])
                    i -= 1
            except:
                pass
            i += 1



        return squares

    def poss_moves(self, board):

        squares = [(self.x + 1, self.y + 2), (self.x + 2, self.y + 1), (self.x + 2, self.y - 1),
                   (self.x + 1, self.y - 2), (self.x - 1, self.y - 2), (self.x - 2, self.y - 1),
                   (self.x - 2, self.y + 1), (self.x - 1, self.y + 2)]
        valids = self.valid_moves(squares, board.back_board)
        return valids
