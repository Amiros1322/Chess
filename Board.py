import Helper
class Board:

    def __init__(self):
        self.str_board = Helper.str_board()
        self.back_board = Helper.back_board()


    def print_back(self):
        for i in self.back_board:
            print(i)

    # A function to improve readability of the move function - this way it can be called from the board.
    def movePiece(self, old_x, old_y, new_x, new_y,):
        self.back_board[old_y][old_x].move(new_x, new_y, self.back_board, self.str_board)

    def print_front(self):
        print(" ", ['0', '1', '2', '3', '4', '5', '6', '7'])
        for index, i in enumerate(self.str_board):
            print(index, i)

    # gets a list of possible moves and marks them on the board. Currently only marks empty squares.
    # TODO: Make it so show_selection shows when a piece can eat an enemy piece.
    def show_selection(self, moves):
        #erases previous marks.
        for Y_index, i in enumerate(self.str_board):
            for X_index, j in enumerate(i):
                if j == '?':
                    self.str_board[Y_index][X_index] = '_'

        #marks possible moves
        for item in moves:
            x = item[0]
            y = item[1]
            if self.back_board[y][x] is None:
                self.str_board[y][x] = '?'
        self.print_front()
