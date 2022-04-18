from abc import ABCMeta, abstractmethod
class LongMoves():
    def long_moves(self, back_board, change_x, change_y):
        squares = []
        curr_x = self.x
        curr_y = self.y
        # Appends every square to the list if it is empty.
        # The loop will stop once it reaches an enemy piece or the edge of the board
        next_x = curr_x + change_x
        next_y = curr_y + change_y
        next_valid = 7 >= next_x >= 0 and 7 >= next_y >= 0

        while next_valid:
            if back_board[curr_y + change_y][curr_x + change_x] is None:
                curr_y += change_y
                curr_x += change_x
                squares.append((curr_x, curr_y))

                next_valid = 7 >= curr_x + change_x >= 0 and 7 >= curr_y + change_y >= 0

            elif back_board[curr_y + change_y][curr_x + change_x].color != self.color:
                curr_y += change_y
                curr_x += change_x
                squares.append((curr_x, curr_y))
                break
            else:
                break

        return squares
