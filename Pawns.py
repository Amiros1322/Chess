from Piece import Piece
from Queen import Queen


class Pawn(Piece):
    # takes coordinates of en_passant. That way after an opponent does not eat a piece it can delete it w/out
    # iterating on all of the pawns.
    en_passant = []

    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        # if a pawn moves 2 squares, an opponent may do take the piece and move to the first
        # square the pawn moved past.

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

        poss_moves = []

        # adds the square in front of the pawn to poss_moves if it is empty.
        if back_board[self.y + change][self.x] is None:
            poss_moves.append((self.x, self.y + 1 * change))

        # if the piece is on it's starting square, it can move 2 squares at once.This possibility is added to poss_moves
        if self.y == first_y and back_board[self.y + 2 * change][self.x] is None:
            poss_moves.append((self.x, self.y + 2 * change))

        try:
            if back_board[self.y + 1 * change][self.x + 1].color != self.color:
                poss_moves.append((self.x + 1, self.y + change))
        except:
            pass
        try:
            if back_board[self.y + change][self.x - 1].color != self.color:
                poss_moves.append((self.x - 1, self.y + change))
        except:
            pass

        return poss_moves

    # promotes the pawn to a queen
    def promote(self):
        new_piece = input("Which piece do you want to promote the pawn to?").lower()
        valid_names = ("queen", "knight", "rook", "bishop")
        name_str = valid_names.join()

        while new_piece not in valid_names:
            new_piece = input("Invalid input. Valid pieces are {0}.".format(name_str)).lower()

    # TODO implement

    """
    def take_passant(self, back_board):
        try:
            if back_board[self.y][self.x + 1]
    """
