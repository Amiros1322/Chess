from Bishop import Bishop
from Knight import Knight
from Piece import Piece
from Queen import Queen
from Rook import Rook


class Pawn(Piece):
    # takes coordinates of en_passant. That way after an opponent does not eat a piece it can delete it w/out
    # iterating on all of the pawns.
    en_passant = None

    def __init__(self, x, y, color, sprite=None):
        super().__init__(x, y, color, sprite=sprite)
        
        # En passant
        self.can_be_taken_EP = False

        # all pawn movements are one or two squares, but in different directions and with different starting
        # squares depending on the color of the piece.
        if self.color == "white":
            self.change = -1
            self.first_y = 6
        else:
            self.change = 1
            self.first_y = 1

    def __str__(self):
        if self.color == "white":
            return 'p'
        return 'P'

    @staticmethod
    def __name__():
        return "Pawn"

    def poss_moves(self, board):
        back_board = board.back_board
        poss_moves = []

        # adds the square in front of the pawn to poss_moves if it is empty.
        if back_board[self.y + self.change][self.x] is None:
            poss_moves.append((self.x, self.y + 1 * self.change))

        # if the piece is on it's starting square, it can move 2 squares at once.This possibility is added to poss_moves
        if self.y == self.first_y and back_board[self.y + 2 * self.change][self.x] is None and back_board[self.y + self.change][self.x] is None:
            poss_moves.append((self.x, self.y + 2 * self.change))
            
        # Adds taking en passant if possible.
        if self.can_take_ep(board):
            poss_moves.append(board.en_passant)

        try:
            if back_board[self.y + 1 * self.change][self.x + 1].color != self.color:
                poss_moves.append((self.x + 1, self.y + self.change))
        except:
            pass
        try:
            if back_board[self.y + self.change][self.x - 1].color != self.color:
                poss_moves.append((self.x - 1, self.y + self.change))
        except:
            pass

        return poss_moves

    # promotes the pawn to a queen
    def promote(self, board):
        new_piece = input("Which piece do you want to promote the pawn to?").lower()
        valid_names = ("queen", "knight", "rook", "bishop", "q", "r", "k", "b")
        name_str = valid_names.join()

        while new_piece not in valid_names:
            new_piece = input("Invalid input. Valid pieces are {0}.".format(name_str)).lower()


        if new_piece == "queen" or new_piece == "q":
            new_piece_obj = Queen(self.x, self.y, self.color)
        elif new_piece == "rook" or new_piece == "r":
            new_piece_obj = Rook(self.x, self.y, self.color)
        elif new_piece == "knight" or new_piece == "k":
            new_piece_obj = Knight(self.x, self.y, self.color)
        elif new_piece == "bishop" or new_piece == "b":
            new_piece_obj = Bishop(self.x, self.y, self.color)

        board.back_board[self.y][self.x] = new_piece_obj
        board.str_board[self.y][self.x] = str(new_piece_obj)

    def can_take_ep(self, board):
        if not board.en_passant:
            return False
        
        if abs(self.x - board.en_passant[0]) == 1 and self.y + self.change == board.en_passant[1]:
            return True
