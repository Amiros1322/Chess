class CmdPrints():

    @staticmethod
    def print_intro():
        print("Welcome to Chess!")
        print("Each piece is represented by the first letter in its' name (The lowercase pieces "
              "are white and the uppercase pieces are black.)")
        print("To select a piece, write 'sel [Piece coordinates]'. For example: 'sel 46' to select white's king pawn")
        print("The places the piece can be moved to will be highlighted, and then you will be able to use the "
              "'mov [Piece coordinates]' command to move a piece to a selected square.")
        print("For example: 'mov 44' will move the selected pawn two squares forward.")
        print("To switch a selected piece input 'esc'.")