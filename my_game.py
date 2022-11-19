board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

class TicTacToe():

    def __init__(self, board):
        self.board = board

    def board_print(self):
        print(self.board[0][0] + '   ' + self.board[0][1] + '   ' + self.board[0][2])
        print()
        print(self.board[1][0] + '   ' + self.board[1][1] + '   ' + self.board[1][2])
        print()
        print(self.board[2][0] + '   ' + self.board[2][1] + '   ' + self.board[2][2])

game = TicTacToe(board)
game.board_print()