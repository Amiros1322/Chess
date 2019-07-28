from Piece import Piece
class King(Piece):

    def __init__(self, x, y, color):
        super().__init__(x, y, color)

    def __str__(self):
        if self.color == "white":
            return 'k'
        return 'K'

    @staticmethod
    def __name__():
        return "King"
    "TODO: possible improvement here, making a nested for loop (1 loop for each coordinate - each \
    runs through the three possiblities for that coordinate, and checks if it is open or not with \
    try except."

    def poss_moves(self, b_board):
        squares = [(self.x + 1, self.y), (self.x + 1, self.y + 1), (self.x, self.y + 1),
                   (self.x - 1, self.y + 1),  (self.x - 1, self.y), (self.x - 1, self.y - 1),
                   (self.x, self.y - 1), (self.x + 1, self.y + 1)]
        i = 0
        while i < len(squares):
            try:
                y = squares[i][1]
                x = squares[i][0]
                if min(squares[i]) < 0 or max(squares[i]) > 7 or b_board[y][x].color == self.color:
                    squares.remove(squares[i])
                    i -= 1
            except:
                pass
            i += 1
        return squares