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

        while True:
            selected = None
            command = input("sel ")  # gets the coordinates as input

            if val_select(command, game_board, turn):
                y = int(command[1])
                x = int(command[0])

                moves = game_board.back_board[y][x].poss_moves(game_board.back_board)
                game_board.show_selection(moves)
                turn = switch_turn(turn)
                print("Good job! Now its {0}'s turn".format(turn))
            else:
                print("Invalid input. Please try again.")


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


def switch_turn(turn):
    if turn == "white":
        return "black"
    return "white"

# def val_output(command, board):

    # p = Pawn(2, 2, "black")
    # moves = [(2, 3), (2, -3), (5, 1)]
    # print(p.valid_moves(moves, game_board.back_board))
    #
    # for i in range(8):
    #    print(game_board.back_board[6][i].poss_moves(game_board.back_board))









#Constructs a new chess board (2d matrix) with pieces set like in the beginning of a game
def ConstructBoard():
      back_line = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
      white_back = [x.lower() for x in back_line]
      pawn_line = ['p' for x in range(8)]
      black_pawns = [x.upper() for x in pawn_line]
      empty_line = ['_' for x in range(8)]

      board = [back_line,black_pawns]
      for i in range(4):
        board.append(empty_line)
        board.append(pawn_line)
        board.append(white_back)
      return board







if __name__ == '__main__':
    Main()