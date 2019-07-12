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
"133-221-333-123-111"