from abc import ABCMeta, abstractmethod
import math
class Piece(object, metaclass = ABCMeta):

    @abstractmethod
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    # move: moves a piece from it's current location to the specified one.
    def move(self, new_x, new_y, board):
        # Checks if an en passant can be done on the pawn.
        # if self is Pawns and math.fabs(new_y - self.y):
        #     self.en_passant = True
        # elif self is Pawns:
        #     self.en_passant = False

        board.back_board[self.x][self.y] = None
        board.back_board[new_x][new_y] = self
        board.str_board[self.x][self.y] = "_"
        board.str_board[new_x][new_y] = str(self)

        self.x = new_x
        self.y = new_y

    # given a list of possible moves for the piece, it returns a list with only the elements that are on the board and
    # unoccupied by an enemy piece. Moves are in a tuple format (x value, y value).
    def valid_moves(self, poss_moves, back_board):
        i = 0
        while i < len(poss_moves):
            x = poss_moves[i][0]
            y = poss_moves[i][1]
            if(
                    min(poss_moves[i]) < 0 or max(poss_moves[i]) > 7 or
                    (back_board[y][x] is not None and back_board[y][x].color == self.color) 
              ):
                poss_moves.remove(poss_moves[i])
                i -= 1
            i += 1
        return poss_moves



