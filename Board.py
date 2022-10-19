import math

from Piece import Piece
from Pawns import Pawn
from Knight import Knight
from Bishop import Bishop
from Rook import Rook
from Queen import Queen
from King import King
from cmd_prints import CmdPrints

class Board:

    def __init__(self, sprite_dict=None):

        # originally used 2d arr for board implementation because of string formatting
        # problems. Should refactor to 1 board

        if sprite_dict is None:
            use_gui = False
            self.sprite_dict = {"pawn": {"white": None, "black": None}, "knight": {"white": None, "black": None},
                                "bishop": {"white": None, "black": None}, "rook": {"white": None, "black": None},
                                "queen": {"white": None, "black": None}, "king": {"white": None, "black": None},
                                "select_mark": None}
        elif self._spirte_dict_val(sprite_dict):
            use_gui = True
            self.sprite_dict = sprite_dict
        else:
            raise Exception("Invalid Sprite_dict")

        self.en_passant = None  # Square that can be taken en passant. None or (x, y) of square that can be taken.
        self.back_board = self.__new_back_board()
        self.use_gui = use_gui
        self.str_board = self.__new_str_board()
        self.game_end = False
        self.winner = None
        self.can_castle_white = True
        self.can_castle_black = True

        self.castle_black_KS = True
        self.castle_black_QS = True
        self.castle_white_KS = True
        self.castle_white_QS = True

        # Protected so that turn
        self.white_turn = True


    # Not used anywhere. Was for debugging
    def print_back(self):
        for i in self.back_board:
            print(i)

    # A function to improve readability of the move function - this way it can be called from the board.
    def move_piece(self, old_x, old_y, new_x, new_y):
        piece = self.back_board[old_y][old_x]

        # check for king being taken
        if type(self.back_board[new_y][new_x]) is King:
            if self.back_board[new_y][new_x].color == "white":
                self.winner = "black"
            elif self.back_board[new_y][new_x].color == "black":
                self.winner = "white"
            self.game_end = True

        # check for castling
        if type(piece) is King:
            if math.fabs(old_x - new_x) > 1:
                self.remove_castling_rights(piece.color)

        # Checks whether to call type(piece) is Rook to check if the rook moved.
        if old_x == 0 and old_y == 0:
            self.castle_black_QS = False
        elif old_x == 7 and old_y == 0:
            self.castle_black_KS = False
        elif old_x == 0 and old_y == 7:
            self.castle_white_QS = False
        elif old_x == 7 and old_y == 7:
            self.castle_white_KS = False

        piece.move(new_x, new_y, self)

        # check for promotion
        if piece.__name__() == "Pawn" and (
                (new_y == 0 and piece.color == "white") or (new_y == 7 and piece.color == "black")):
            self.back_board[new_y][new_x] = Queen(new_x, new_y, piece.color, sprite=self.sprite_dict["queen"][piece.color])


    # Only used for cmd display
        def print_front(self):
            print(" ", ['0', '1', '2', '3', '4', '5', '6', '7'])
            for index, i in enumerate(self.str_board):
                print(index, i)

    # gets a list of possible moves and marks them on the board. Currently only marks empty squares.
    # TODO: Make it so show_selection shows when a piece can eat an enemy piece. (with curses?)
    def show_selection(self, moves):
        # Selects the correct graphical representation of an empty square and the board to modify
        if self.use_gui:
            modified_board = self.back_board
            mark = self.sprite_dict["select_mark"]
        else:
            modified_board = self.str_board
            mark = '_'

        self.clear_selection()

        # marks possible moves with
        for item in moves:
            x = item[0]
            y = item[1]
            if self.back_board[y][x] is None:
                modified_board[y][x] = mark

        # The cmd interface has to print explicitly - the gui is drawn every frame.
        if not self.use_gui:
            self.print_front()


    # erases previous selection marks.
    def clear_selection(self):
        if self.use_gui:
            for row in range(len(self.back_board)):
                for col in range(len(self.back_board[0])):
                    if self.back_board[col][row] == self.sprite_dict["select_mark"]:
                        self.back_board[col][row] = None
        else:
            for Y_index, i in enumerate(self.str_board):
                for X_index, j in enumerate(i):
                    if j == '?':
                        self.str_board[Y_index][X_index] = '_'

    def pen_rep(self):
        raise NotImplementedError

    # creates new string board representation
    def __new_str_board(self):
        back_line = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        white_back = [x.lower() for x in back_line]

        pawn_line, black_pawns, empty1, empty2, empty3, empty4 = [], [], [], [], [], []
        for x in range(8):
            pawn_line.append('p')
            black_pawns.append('P')
            empty1.append('_')
            empty2.append('_')
            empty3.append('_')
            empty4.append('_')

        board = [back_line, black_pawns, empty1, empty2, empty3, empty4, pawn_line, white_back]

        return board

    def __new_gui_board(self):
        #TODO: implement

        raise NotImplementedError

    # creates new object board representation
    def __new_back_board(self):
        black_back = [Rook(0, 0, "black", sprite=self.sprite_dict["rook"]["black"]), Knight(1, 0, "black", sprite=self.sprite_dict["knight"]["black"]),
                      Bishop(2, 0, "black", sprite=self.sprite_dict["bishop"]["black"]), Queen(3, 0, "black", sprite=self.sprite_dict["queen"]["black"]),
                      King(4, 0, "black", sprite=self.sprite_dict["king"]["black"]), Bishop(5, 0, "black", sprite=self.sprite_dict["bishop"]["black"]),
                      Knight(6, 0, "black", sprite=self.sprite_dict["knight"]["black"]), Rook(7, 0, "black", sprite=self.sprite_dict["rook"]["black"])]
        white_back = [Rook(0, 7, "white", sprite=self.sprite_dict["rook"]["white"]), Knight(1, 7, "white", sprite=self.sprite_dict["knight"]["white"]),
                      Bishop(2, 7, "white", sprite=self.sprite_dict["bishop"]["white"]), Queen(3, 7, "white", sprite=self.sprite_dict["queen"]["white"]),
                      King(4, 7, "white", sprite=self.sprite_dict["king"]["white"]), Bishop(5, 7, "white", sprite=self.sprite_dict["bishop"]["white"]),
                      Knight(6, 7, "white", sprite=self.sprite_dict["knight"]["white"]), Rook(7, 7, "white", sprite=self.sprite_dict["rook"]["white"])]

        white_pawns, black_pawns, empty1, empty2, empty3, empty4 = [], [], [], [], [], []
        for i in range(8):
            white_pawns.append(Pawn(i, 6, "white", sprite=self.sprite_dict["pawn"]["white"]))
            black_pawns.append(Pawn(i, 1, "black", sprite=self.sprite_dict["pawn"]["black"]))
            empty1.append(None)
            empty2.append(None)
            empty3.append(None)
            empty4.append(None)

        back_board = [black_back, black_pawns, empty1, empty2, empty3, empty4, white_pawns, white_back]

        return back_board

    # Does not check the sprites, only checks that there is one of every piece
    #
    def _spirte_dict_val(self, sprite_dict) -> bool:
        for key, val in sprite_dict.items():
            if key not in {"pawn", "knight", "bishop", "rook", "queen", "king", "select_mark"}:
                print("Invalid keys in sprite_dict")
                return False

            if key != "select_mark" and set(val.keys()) != {"black", "white"}:
                print("Invalid color values keys in sprite_dict")
                return False

        return True

    def switch_turn(self):
        self.white_turn = not self.white_turn

    # TODO: Refactor so that this isn't necessary. Whether a piece is white or black should be a bool in the piece.
    def color_turn(self):
        if self.white_turn:
            return "white"
        return "black"

    def remove_castling_rights(self, color, side=False):
        if not side:
            if color == "white":
                self.castle_white_QS = False
                self.castle_white_KS = False
            elif color == "black":
                self.castle_black_QS = False
                self.castle_black_KS = False
        elif side == "queen":
            if color == "white":
                self.castle_white_QS = False
            elif color == "black":
                self.castle_black_QS = False
        elif side == "king":
            if color == "white":
                self.castle_white_KS = False
            elif color == "black":
                self.castle_black_KS = False




