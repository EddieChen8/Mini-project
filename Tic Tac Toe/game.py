import time
from sklearn.utils import column_or_1d

from player import ComputerPlayer, HumanPlayer


class TicTacToe():

    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)]
                        for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_square(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        #if valid move, the make the move (assign square to letter)
        #the return true. if invalid, return false

        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        #winner if 3 in a row anywhere. we have to check all of these!
        #first let's check the row
        row_ind = square // 3
        row = self.board[row_ind:(row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        # second let's check the column
        column_ind = square % 3
        column = [self.board[column_ind + i * 3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # third let's check the diagonal'
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True

            diagonal2 = [self.board[i] for i in [2, 4, 6]]

            if all([spot == letter for spot in diagonal2]):
                return True

        # if all fails, return
        return False


def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()

    letter = 'X'  #starting letter

    # iterate while teh game still has empty_squares
    # we don't have to worry about winner because we'll just return that
    # which breaks the loop

    while game.empty_squares():
        # get the move from the appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('')  #just empty line

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter

        #after we made our move,we need to alternate letter
            letter = 'O' if letter == 'X' else 'X'

        time.sleep(0.8)

        if print_game:
            print('it\'s a tie!')


if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = ComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)
