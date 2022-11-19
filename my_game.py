board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

class TicTacToe():

    def __init__(self, board):
        self.board = board

    def board_print(self): #выводит стол
        print(self.board[0][0] + '   ' + self.board[0][1] + '   ' + self.board[0][2])
        print()
        print(self.board[1][0] + '   ' + self.board[1][1] + '   ' + self.board[1][2])
        print()
        print(self.board[2][0] + '   ' + self.board[2][1] + '   ' + self.board[2][2])

    def moves(self): #проверка можно ли совершить ход, возвращает список доступных ходов
        movess = []
        for i in self.board:
            for j in i:
                if j != 'X' and j != 'O':
                    movess.append(j)
        return movess

    def win(self, XO):
        for i in self.board:
            if i.count(XO) == 3:
                return True
        for i in range(3):
            if self.board[0][i] == XO and self.board[1][i] == XO and self.board[2][i] == XO:
                return True
        if self.board[0][0] == XO and self.board[1][1] == XO and self.board[2][2] == XO:
            return True
        elif self.board[0][2] == XO and self.board[1][1] == XO and self.board[2][0] == XO:
            return True
        return False






game = TicTacToe(board)
game.board_print()