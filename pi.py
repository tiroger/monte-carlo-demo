"""
Here we'll use Monte Carlo simulations to approximate the value of π

Imagine we square canvas contaning a circular dartboard, centered and tangent with the side of a square.
A dart thrower has an equal probability of hitting anywhere on the canvas.

We can calculate the probability of hitting the circular board:

p(hit) = number of dart in circle/total number of darts thrown

Since the thrower always hits the canvas, we can rewrite this as:

p(hit) = area of circle/area of square

If the circle has radius r, we can rewrite the equation:

p(hit) = πr^2/2(r^2) = πr^2/4r^2)
p(hit) = π/4
π = 4*p(hit)

---------------------------------------------------------
π = 4 * num of darts in circle/total num of darts thrown
---------------------------------------------------------

If we throw an infinite amount of darts at the canvas, we can obtain a good approximation for the value of π
We'll use Monte Carlo simulations to simulate throw outcomes.

"""

# Importing libraries
import random
import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns




num_sims = 10000  # Number of simulations

all_pis = []

def estimate_pi(simulations):
    # Simulating dart throws on a board with radius = 1
    hits = 0  # Counter for the number of "darts that fall inside the circle"
    inside_outside = [
    ]  # Array to contain all the dart outcomes; used for plotting

    all_x = []
    all_y = []

    for sim in range(1, num_sims):
        x = np.random.uniform(-1, 1)
        all_x.append(x)
        y = np.random.uniform(-1, 1)
        all_y.append(y)

        d = np.sqrt(
            x**2 + y**2
        )  # We can use Pythagoras' formula to calculate the distance of the dot from the center of the circle
        if (d) < 1:
            hits += 1
            inside_outside.append(1)
        else:
            inside_outside.append(0)

        temp_pi = 4 * hits / sim
        all_pis.append(temp_pi)

    hit_or_miss = np.where(np.array(inside_outside) == 1, 'hit', 'miss')

    pi = 4 * hits / num_sims
    print(f'The estimated value of π is {pi}')

    # Plotting the results

    fig = plt.figure(figsize=(5, 10))
    plt.style.use('fivethirtyeight')

    ax1 = fig.add_subplot(211)
    ax1.set_title('Monte Carlo Simulation to Estimate Value of Pi',
                  fontsize=16)
    ax1 = sns.scatterplot(all_x, all_y, hue=hit_or_miss, legend=False)

    ax2 = fig.add_subplot(212)
    ax2 = plt.plot(all_pis)
    plt.xlabel('Number of Simulations', fontsize=12)
    plt.ylabel('Value of Pi', fontsize=12)

    plt.axhline(y=3.14, color='g', linestyle='-')
    plt.annotate(f'Estimated value of pi = {pi}',
                 xy=(1, 0),
                 xycoords='axes fraction',
                 xytext=(-20, 150),
                 textcoords='offset pixels',
                 horizontalalignment='right',
                 verticalalignment='top')
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    # ax2.ylabel('Value of Pi')
    # ax2.xlabel('Number of Simulations')

    plt.tight_layout()
    plt.show()
    fig.savefig('images/monte_carlo_pi_estimation.png', dpi=300)


estimate_pi(100)