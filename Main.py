import Knight, Bishop, Rook, Queen, King
from Board import Board
from Pawns import Pawn

def Main():
     game_board = Board()

     game_over = False
     turn = 1  # when turn = 1 it is white's turn, and when turn = -1 it is black's turn.

     print("Welcome to Chess!")
     print("Each piece is represented by the first letter in its' name (The lowercase pieces "
           "are white and the uppercase pieces are black.)")
     print("To select a piece, write 'sel [Piece coordinates]'. For example: 'sel 46' to select white's king pawn")
     print("The places the piece can be moved to will be highlighted, and then you will be able to use the "
           "'mov [Piece coordinates]' command to move a piece to a selected square.")
     print("For example: 'mov 44' will move the selected pawn two squares forward")

     game_board.print_front()

     while not game_over:
         command = input("sel ") #gets the coordiantes as input
         if(val_input(command, game_board)):




def val_input(command, board):
    x = None
    y = None
    try:
        y = int(command[1])
        x = int(command[0])
        if(board[])
    except :
        return False

def val_output(command, board):

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