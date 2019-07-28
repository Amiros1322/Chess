from abc import ABCMeta, abstractmethod
class LongMoves():
    def long_moves(self, back_board, change_x, change_y):
        squares = []
        curr_x = self.x
        curr_y = self.y
        # Appends every square to the list if it is empty.
        # The loop will stop once it reaches an enemy piece or the edge of the board

        next_valid = curr_x + change_x <= 7 and curr_y + change_y <= 7 and curr_x + change_x >= 0 and \
                     curr_y + change_y >= 0
        while next_valid and back_board[curr_y + change_y][curr_x + change_x] == None:
            curr_y += change_y
            curr_x += change_x
            squares.append((curr_x, curr_y))

            next_valid = curr_x + change_x <= 7 and curr_y + change_y <= 7 and curr_x + change_x >= 0 and \
                         curr_y + change_y >= 0

        return squares