import Knight, Bishop, Rook, Queen, King
from Board import Board
from Pawns import Pawn
from Helper import *
import sys
import PyGameGUI


def Main():
    game_board = Board()
    USEGUI = False
    game_over = False
    turn = "white"

    print("Welcome to Chess!")
    print("Each piece is represented by the first letter in its' name (The lowercase pieces "
          "are white and the uppercase pieces are black.)")
    print("To select a piece, write 'sel [Piece coordinates]'. For example: 'sel 46' to select white's king pawn")
    print("The places the piece can be moved to will be highlighted, and then you will be able to use the "
          "'mov [Piece coordinates]' command to move a piece to a selected square.")
    print("For example: 'mov 44' will move the selected pawn two squares forward.")
    print("To switch a selected piece input 'esc'.")

    game_board.print_front()

    # For implementing en passant, castling, and checkmate we need to keep
    # a list of which squares both pieces can move to.

    while not game_over:
        selected = None

        # Selects a white piece
        while selected is None:
            command = input("sel ")  # gets the coordinates as input

            # TODO: implement editing mode where you can move pieces even to invalid squares.

            if val_select(command, game_board, turn):
                y = int(command[1])
                x = int(command[0])
                selected = (x, y)
            else:
                print("Invalid input. Please try again.")

        # Returns the possible moves of the piece on square (x, y)
        piece = game_board.back_board[y][x]
        moves = piece.poss_moves(game_board.back_board)
        game_board.show_selection(moves)
        print("{0} selected".format(piece.__name__()))

        destination = None
        while destination is None:

            destination = input("mov ")

            # If the player wants to switch the selected piece he inputs esc.
            if destination == 'esc':
                turn = switch_turn(turn)
                break

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
        print("It is {0}'s turn. ".format(turn))

# Gets all the squares pieces from the chosen color can move to next turn.
# Output: (piece, [array with piece moves])
def team_threats(color, back_board):
    threats = []
    for i in back_board:
        for piece in i:
            if piece is not None and piece.color == color:
                threats.append((piece, piece.poss_moves()))
    return threats


# After a piece has moved, it updates the threats of the team
def update_threats(piece, new_poss_moves, threats, old_x, old_y):
    for i in threats:
        if (old_x, old_y) in i[1]:
            i[0]
        if piece is i[0]:
            i[1] = new_poss_moves

if __name__ == '__main__':
    #Main()
    pass
