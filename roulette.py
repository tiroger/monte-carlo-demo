# Creating our virtual roulette wheel
"""
Here we'll use Monte Carlo simulations to evaluate various gambling strategies and scenarios, while playong roulette.
"""

#importing libraries
import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Creating our simulated wheel
roulette_wheel = ['red'] * 18 + ['black'] * 18 + ['green'] * 2  # In American Roulette, the ball can fall in one of 38 pockets -- 18 red pockets, 18 black pockets, & 2 green pockets

# Creating a function to simulate a spin of the wheel
def spin_wheel():
    return random.choice(roulette_wheel)

#outcomes = []
#bankroll_over_time = []


"""
Strategy 1: A player always chooses 'red' and bets the same amount of money
"""

# Function to simulate game play where a player always picks red, while placing a bet for the same amout of money
def gamble_same_amount():
    bankroll_over_time = []
    bet = 1 # Player always bets $1 for every spin of the wheel
    bankroll = 100 # Starting money reserve
    while bankroll > 0: # Player can bet as long as they have money
        #for sim in range(1, simulations):
        roll = spin_wheel()
        #outcomes.append(roll)
        if roll == 'red':
            bankroll += bet
        else:
            bankroll -= bet

        bankroll_over_time.append(bankroll)
    #plt.plot(bankroll_over_time)
    return bankroll_over_time


"""
Strategy 2: Martingale: The Martingale system is the most popular and commonly used roulette strategy. 
The concept behind it is pretty simple – you increase your bet after every loss, so when you eventually win, 
you get your lost money back and start betting with the initial amount again. It seems quite logical, and 
it’s fairly easy to understand and implement. No need to be a math wizard or a strategic mastermind in 
order to use this system.
"""


# Function to simulate game play where a player uses the Martingale Strategy
def martingale():
    bankroll_over_time = []
    bet = 0.01  # Initial bet
    bankroll = 100  # Starting money reserve
    while bankroll > 0:
        roll = spin_wheel()
        if bet > bankroll:
            bet = bankroll  # This ensures that the player cannot bet more than they have
        #outcomes.append(roll)
        if roll == 'red':
            bankroll += bet
            bet = 0.01
        else:
            bankroll -= bet
            bet *= 2 

        bankroll_over_time.append(bankroll)
    #plt.plot(bankroll_over_time)
    return bankroll_over_time



# # Function to simulate multiple gambling sessions
# def monte_carlo(simulations):
#     plt.style.use('fivethirtyeight')
#     for sim in range(1, simulations+1):
#         plt.plot(gamble_same_amount(), linewidth=0.5)
#         plt.xlabel("Number of Games Played", fontsize=12)
#         plt.ylabel("Bankroll ($)", fontsize=12)
#         plt.xticks(fontsize=10)
#         plt.yticks(fontsize=10)
#         plt.title("Constant Bet - Bankroll Over Time", fontsize=16)
#         plt.tight_layout()
#         plt.savefig(f'images/roulette_constant_bet.png', dpi=300)

# monte_carlo(10)


# Function to simulate multiple gambling sessions
def monte_carlo(simulations):
    plt.style.use('fivethirtyeight')
    for sim in range(1, simulations + 1):
        plt.plot(martingale(), linewidth=0.5)
        plt.xlabel("Number of Games Played", fontsize=12)
        plt.ylabel("Bankroll ($)", fontsize=12)
        plt.xticks(fontsize=10)
        plt.yticks(fontsize=10)
        plt.title("Martingal Strategy - Bankroll Over Time", fontsize=16)
        plt.tight_layout()
        plt.savefig(f'images/roulette_martingale.png', dpi=300)


monte_carlo(10)