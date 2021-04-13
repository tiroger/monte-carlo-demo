"""
In American Roulette, there are 18 red pockets, 18 black pockets, 
and 2 green pockets that the ball can fall into after spinning around the wheel
"""
# Importing libraries
import random
import seaborn as sns

class Roulette(): # Creating a class to simulate a game of roulette

    def __init__(self):
        self.pockets = [] # Creating our roulette wheel
        for i in range (1,37):
            self.pockets.append(i)
            self.pockets.append(0)
            self.pockets.append(00)
        self.ball = None
        self.pocket_odds = len(self.pockets) - 1

    def spin(self):
        self.ball = random.choice(self.pockets)

    def bet_pocket(self, pocket, amount_bet):
        if str(pocket) == str(self.ball):
            payoff = amount_bet * self.pocket_odds
            return payoff
        else: return -amount_bet

    def __str__(self):
        return 'Roulette'


def play_roulette(game, number_spins, pocket, bet, print_text):
    total_pocket = 0
    for _ in range(number_spins):
        game.spin()
        total_pocket += game.bet_pocket(pocket, bet)

    if print_text:
        print(number_spins, 'spins of', game)
        print(f'Expected return when betting {pocket} = {str(total_pocket/number_spins*100)} %')
    return (total_pocket/number_spins)


game = Roulette()
for number_spins in (1000, 1000000):
    for i in range(3):
        play_roulette(game, number_spins, 2, 1, True)
