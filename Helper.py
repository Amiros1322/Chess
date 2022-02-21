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
    black_back = [Rook(0,0,"black"), Knight(1,0,"black"), Bishop(2,0,"black"), Queen(3,0,"black"),
                 King(4,0,"black"), Bishop(5,0,"black"), Knight(6,0,"black"), Rook(7,0,"black")]
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

    return  back_board