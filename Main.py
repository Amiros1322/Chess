import Knight, Bishop, Rook, Queen, King
from Board import Board
from Pawns import Pawn
import sys


def Main():
    game_board = Board()

    game_over = False
    turn = "white"

    print("Welcome to Chess!")
    print("Each piece is represented by the first letter in its' name (The lowercase pieces "
           "are white and the uppercase pieces are black.)")
    print("To select a piece, write 'sel [Piece coordinates]'. For example: 'sel 46' to select white's king pawn")
    print("The places the piece can be moved to will be highlighted, and then you will be able to use the "
           "'mov [Piece coordinates]' command to move a piece to a selected square.")
    print("For example: 'mov 44' will move the selected pawn two squares forward")

    game_board.print_front()

    while not game_over:
        selected = None

        # Selects a white piece
        while selected is None:
            command = input("sel ")  # gets the coordinates as input

            if val_select(command, game_board, turn):
                y = int(command[1])
                x = int(command[0])
                selected = (x, y)
            else:
                print("Invalid input. Please try again.")

        # Returns the possible moves of the piece on square (x, y)
        moves = game_board.back_board[y][x].poss_moves(game_board.back_board)
        game_board.show_selection(moves)

        destination = None
        while destination is None:

            destination = input("mov ")
            if val_move(destination, moves):
                x1 = selected[0]
                y1 = selected[1]
                x2 = int(destination[0])  # selected is a tuple of ints, while destination is a string
                y2 = int(destination[1])  # concatenation of x and y. So they must be casted to ints.
                game_board.back_board[y1][x1].move(x2, y2, game_board)
            else:
                print("That piece can't move there")
                destination = None

        turn = switch_turn(turn)
        game_board.clear_selection()
        game_board.print_front()
        print("Move successful. It is {0}'s turn. ".format(turn))


# Inputs: 2 digit selection command, board, which color's turn it is.
# Output: True if command is valid. False if invalid. It will print an error message if false.
def val_select(command, board, turn):
    try:
        y = int(command[1])
        x = int(command[0])

        if len(command) != 2:
            print("The selection command must consist of two positive numbers.")
            return False

        if board.back_board[y][x].color == turn:
            return True
        else:
            print("That is not a {0} piece. It is {0}'s turn".format(turn))
            return False
    except IndexError:
        print("Please enter values between 0 and 7.")
        return False
    except AttributeError:
        print("There is no piece on that square")
        return False
    except ValueError:
        print("The selection command must consist of two positive numbers between 0 and 7.")
    except:
        print(sys.exc_info()[0])
        return False

# Checks if a given move is valid. dest[ination] is a tuple (x, y),
# and moves is a list of valid moves.
def val_move(dest, moves):
    try:
        x = int(dest[0])
        y = int(dest[1])

        for i in moves:
            if i == (x, y):
                return True
    except:
        print("Invalid move - you must enter a square that is selected")
        return False


def switch_turn(turn):
    if turn == "white":
        return "black"
    return "white"


# Constructs a new chess board (2d matrix) with pieces set like in the beginning of a game
def construct_board():
    back_line = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
    white_back = [x.lower() for x in back_line]
    pawn_line = ['p' for x in range(8)]
    black_pawns = [x.upper() for x in pawn_line]
    empty_line = ['_' for x in range(8)]

    board = [back_line, black_pawns]
    for i in range(4):
        board.append(empty_line)
        board.append(pawn_line)
        board.append(white_back)
    return board


if __name__ == '__main__':
    Main()