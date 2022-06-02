from xml.dom.minidom import parseString
import math
import random

from torch import maximum


class Player():

    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass


class ComputerPlayer(Player):

    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square


class HumanPlayer(Player):

    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8):')
            try:
                val = int(square)
                if val not in game.available_moves():
                    return ValueError
                valid_square = True
            except ValueError:
                print('Invalid square, Try again')

        return val


class GeniusComputerPlayer(Player):

    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(
                game.available_moves())  #randamly choose one square
        else:
            #get teh square based on minimax algorithm
            square = game.minimax(game, self.letter)

    def minimax(self, state, player):
        max_player = self.letter  #youself
        other_player = 'O' if player == 'X' else 'X'  #the other player

        # first, we want to check if the previous move is a winner
        # this  is our base case
        if state.current_winner == other_player:
            # we should return position and score because we need to keep track of the score
            # for minimax to work
            return {'position': None, 'score': 1}
