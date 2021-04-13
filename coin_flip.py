"""
Here we'll use Monte Carlo simulations to demonstrate that the probability of getting a head, for example, on a coin toss is 0.5

If we flip a coin a large number of time, we can obtain a good approximation for the value of of the probability value.py

P(head) = number of heads/total number of coins flips
"""


# Importing libraries
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Simulating a coin toss
possible_outcomes = ['heads', 'tail']


def flip_coin():
    result = random.choice(possible_outcomes)
    return result


probability_values = []


def simulate_coin_flip(simulations):
    results = 0
    for sim in range(1, simulations):
        coin_flip = flip_coin()
        if coin_flip == "heads":
            results += 1
        else:
            results += 0

        temp_probability = results / sim
        probability_values.append(temp_probability)

    final_probability = results / simulations

    plt.style.use('fivethirtyeight')
    plt.title('Monte Carlo Simulations of Coin Flips', fontsize=16)
    plt.axhline(0.5, color='g')
    plt.xlabel('Number of Coin Flips', fontsize=12)
    plt.ylabel('Probability Values', fontsize=12)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.plot(probability_values)
    plt.annotate(f'Estimated Probability Value = {final_probability}',
                 xy=(1, 0),
                 xycoords='axes fraction',
                 xytext=(-20, 150),
                 textcoords='offset pixels',
                 horizontalalignment='right',
                 verticalalignment='top')
    plt.tight_layout()
    plt.savefig('images/coin_flip_simulation.png', dpi=300)

    # return final_probability
    print(final_probability)


simulate_coin_flip(1000)