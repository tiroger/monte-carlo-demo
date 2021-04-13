# Creating our virtual roulette wheel
"""
Here we'll use Monte Carlo simulations to evaluate various roulette strategies. 
All bets are placed on even-money sections (e.g (Red/Black, Odd/Even, 1-18/19-36, etc),
 which pay out 1/1.
"""

#importing libraries
import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#####################

# Creating our simulated wheel and a function to simulate a spin of the wheel

roulette_wheel = ['red'] * 18 + ['black'] * 18 + ['green'] * 2  # In American Roulette, the ball can fall in one of 38 pockets -- 18 red pockets, 18 black pockets, & 2 green pockets

numbered_wheel = list(range(0, 37))
numbered_wheel.append('00')

def spin_wheel():
    return random.choice(roulette_wheel)

def spin_numbered_wheel():
    return random.choice(numbered_wheel)

#####################

"""
Strategy 1: The Constant Bet 
No matter whether the player wins or loses, their bet remains the same.
"""

# Function to simulate the Constant Bet strategy
def constant_bet():
    bankroll_over_time = []
    bankroll = 100  # Starting money reserve
    bet = 1 # Player always bets $1 for every spin of the wheel
    while bankroll > 0: # Player can bet as long as they have money
        #for sim in range(1, simulations):
        roll = spin_wheel()
        #outcomes.append(roll)
        if roll == 'red':
            bankroll += bet
        else:
            bankroll -= bet

        bankroll_over_time.append(bankroll)

    return bankroll_over_time



"""
Strategy 2: The Martingale
The Martingale system is the most popular and commonly used roulette strategy. 
The player increases their bet after every loss, so when you eventually win, 
you get your lost money back and start betting with the initial amount again. 
There are different methods to increase the value of the bet. Here we'll double 
the bet after every loss.
"""

# Function to simulate game play where a player uses the Martingale strategy
def martingale():
    bankroll_over_time = []
    bankroll = 100  # Starting money reserve
    bet = 1  # Initial bet
    while bankroll > 0:
        roll = spin_wheel()
        if bet > bankroll:
            bet = bankroll  # This ensures that the player cannot bet more than they have
        #outcomes.append(roll)
        if roll == 'red':
            bankroll += bet
            bet = 1
        else:
            bankroll -= bet
            bet *= 2

        bankroll_over_time.append(bankroll)

    return bankroll_over_time



"""
Strategy 3: The Grand Martingale
The Grand Martingale strategy is the same as the Martingale strategy at its core. 
The only difference is that every time the player loses a hand, they double the 
current bet plus an extra amount equal to the original bet. 
"""


# Function to simulate game play where a player uses the Martingale strategy
def grand_martingale():
    bankroll_over_time = []
    bankroll = 100  # Starting money reserve
    bet = 1  # Initial bet
    while bankroll > 0:
        roll = spin_wheel()
        if bet > bankroll:
            bet = bankroll  # This ensures that the player cannot bet more than they have
        #outcomes.append(roll)
        if roll == 'red':
            bankroll += bet
            bet = 1
        else:
            bankroll -= bet
            bet = 2*bet + bet

        bankroll_over_time.append(bankroll)

    return bankroll_over_time



"""
Strategy 4: The Reverse Martingale
The Reverse Martingale betting strategy follows similar rules to the 
Martingale strategy, but in reverse. Instead of doubling their bet 
when they lose a hand, it is increased after a win.
"""

# Function to simulate game play where a player uses the Reverse Martingale strategy
def reverse_martingale():
    bankroll_over_time = []
    bankroll = 100  # Starting money reserve
    bet = 1  # Initial bet
    while bankroll > 0:
        roll = spin_wheel()
        if bet > bankroll:
            bet = bankroll  # This ensures that the player cannot bet more than they have
        #outcomes.append(roll)
        if roll == 'red':
            bankroll += bet
            bet *= 2
        else:
            bankroll -= bet
            bet = 1

        bankroll_over_time.append(bankroll)

    return bankroll_over_time


"""
Strategy 5: The D’Alembert
The D'Alembert strategy is similar to the Martingale strategy, but instead 
of doubling the stake after a losing bet, as in the Martingale, one unit is 
added to the player's stake. After a win, the stake decreases by one unit.
"""

# Function to simulate game play where a player uses the D'Alembert strategy
def dalembert():
    bankroll_over_time = []
    bankroll = 100  # Starting money reserve
    bet = 1  # Initial bet
    while bankroll > 0:
        roll = spin_wheel()
        if bet > bankroll:
            bet = bankroll  # This ensures that the player cannot bet more than they have
        #outcomes.append(roll)
        if roll == 'red':
            bankroll += bet
            bet -= 1
            if bet == 0:
                bet = 1 # In case the player wins on the first roll
        else:
            bankroll -= bet
            bet += 1

        bankroll_over_time.append(bankroll)

    return bankroll_over_time



"""
Strategy 6: All-In
For players who like living a little on the edge, the All-In betting strategy 
can provide an adrenaline rush or quick cash. The approach is exactly like it 
sounds. Choose a number to bet on, and bet your whole bankroll on it.
"""

# Function to simulate game play where a player uses the D'Alembert strategy
def all_in():
    bankroll_over_time = []
    bankroll = 100  # Starting money reserve
    bet = 100  # Initial bet
    while bankroll > 0:
        roll = spin_wheel()
        #outcomes.append(roll)
        if roll == 'red':
            bankroll += bet
            bet = bankroll
        else:
            bankroll -= bet
            bet = bankroll

        bankroll_over_time.append(bankroll)

    return bankroll_over_time


###################################################

# Function to simulate multiple gambling sessions
def monte_carlo(simulations):
    plt.style.use('fivethirtyeight')
    for sim in range(1, simulations + 1):
        plt.plot(martingale(), linewidth=0.5)
        plt.xlabel("Number of Games Played", fontsize=12)
        plt.ylabel("Bankroll ($)", fontsize=12)
        plt.xticks(fontsize=10)
        plt.yticks(fontsize=10)
        plt.title('Martingale Strategy - Bankroll Over Time', fontsize=16)
        plt.tight_layout()
        plt.savefig('images/roulette_martingale.png', dpi=300)

###################################################


monte_carlo(10)  # Running 10 simulations
