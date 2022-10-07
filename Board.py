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
                                "queen": {"white": None, "black": None}, "king": {"white": None, "black": None}}
        elif self._spirte_dict_val(sprite_dict):
            use_gui = True
            self.sprite_dict = sprite_dict
        else:
            raise Exception("Invalid Sprite_dict")

        self.back_board = self.__new_back_board()

        self.use_gui = use_gui

        if use_gui:
            # self.str_board = self.__new_gui_board() #TODO: implement GUI board
            self.move_op_mark = None
        else:
            self.str_board = self.__new_str_board()
            self.move_op_mark = "?"


    # Not used anywhere. Was for debugging
    def print_back(self):
        for i in self.back_board:
            print(i)

    # A function to improve readability of the move function - this way it can be called from the board.
    def move_piece(self, old_x, old_y, new_x, new_y):
        self.back_board[old_y][old_x].move(new_x, new_y, self.back_board, self.str_board)

    def print_front(self):
        if self.use_gui:
            raise NotImplementedError
        else:
            print(" ", ['0', '1', '2', '3', '4', '5', '6', '7'])
            for index, i in enumerate(self.str_board):
                print(index, i)

    # gets a list of possible moves and marks them on the board. Currently only marks empty squares.
    # TODO: Make it so show_selection shows when a piece can eat an enemy piece. (with curses?)
    def show_selection(self, moves):
        if self.is_gui:
            raise NotImplementedError
        else:
            self.clear_selection()

            # marks possible moves
            for item in moves:
                x = item[0]
                y = item[1]
                if self.back_board[y][x] is None:
                    self.str_board[y][x] = '?'
            self.print_front()

    # erases previous selection marks.
    def clear_selection(self):

        if self.is_gui:
            raise NotImplementedError
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
        input_set = set([x.lower() for x in sprite_dict.keys()])
        if input_set != {"pawn", "knight", "bishop", "rook", "queen", "king"}:
            print("Invalid piece keys in sprite_dict")
            return False

        for val in sprite_dict.values():
            if set(val.keys()) != {"black", "white"}:
                print("Invalid color values keys in sprite_dict")
                return False
        return True



