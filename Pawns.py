from Piece import Piece
from Queen import Queen


class Pawn(Piece):

    # TODO: implement en passant. when you move a pawn check if you moved it 2 spaces. if you did turn en passant true
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        # if a pawn moves 2 squares, an opponent may do take the piece and move to the first
        # square the pawn moved past.
        self.en_passant = False

    def __str__(self):
        if self.color == "white":
            return 'p'
        return 'P'

    @staticmethod
    def __name__():
        return "Pawn"

    def poss_moves(self, back_board):
        # all pawn movements are one or two squares, but in different directions and with different starting
        # squares depending on the color of the piece.
        change = 1  # the direction the piece moves in - will change to -1 if piece is white.
        first_y = 1  # the y value that the piece starts on

        if str(self).islower():
            change = -1
            first_y = 6

        # puts all squares pawn could possibly go to into a list poss_moves
        poss_moves = []
        if back_board[self.y + 1*change][self.x] is None:
            poss_moves.append((self.x, self.y + 1*change))

        # if the piece is on it's starting square, it can move 2 squares at once.This possibility is added to poss_moves
        if self.y == first_y and back_board[self.y + 2*change][self.x] is None:
            poss_moves.append((self.x, self.y + 2*change))

        try:
            if back_board[self.y + 1*change][self.x + 1].color != self.color:
                poss_moves.append((self.x + 1, self.y + 1*change))
        except:
            pass
        try:
            if back_board[self.y + 1*change][self.x - 1].color != self.color:
                poss_moves.append((self.x - 1, self.y + 1*change))
        except:
            pass

        # poss_moves = self.valid_moves(poss_moves, back_board)

        # TODO: Make it so pawns can't eat while moving forward

        return poss_moves

    # promotes the pawn to a queen
    def promote(self):
        return Queen(self.x, self.y, self.color)

