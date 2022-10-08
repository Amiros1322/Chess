from Piece import Piece
from Pawns import Pawn
from Knight import Knight
from Bishop import Bishop
from Rook import Rook
from Queen import Queen
from King import King

"""""
takes a piece and the string board and calculates
"""""


def str_board():
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


def back_board():
    black_back = [Rook(0, 0, "black"), Knight(1, 0, "black"), Bishop(2, 0, "black"), Queen(3, 0, "black"),
                  King(4, 0, "black"), Bishop(5, 0, "black"), Knight(6, 0, "black"), Rook(7, 0, "black")]
    white_back = [Rook(0, 7, "white"), Knight(1, 7, "white"), Bishop(2, 7, "white"), Queen(3, 7, "white"),
                  King(4, 7, "white"), Bishop(5, 7, "white"), Knight(6, 7, "white"), Rook(7, 7, "white")]

    white_pawns, black_pawns, empty1, empty2, empty3, empty4 = [], [], [], [], [], []
    for i in range(8):
        white_pawns.append(Pawn(i, 6, "white"))
        black_pawns.append(Pawn(i, 1, "black"))
        empty1.append(None)
        empty2.append(None)
        empty3.append(None)
        empty4.append(None)

    back_board = [black_back, black_pawns, empty1, empty2, empty3, empty4, white_pawns, white_back]

    return back_board

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
        return False
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