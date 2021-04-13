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

-----------------------------------------------------
π = 4 * num of dart in circle/num of darts in square
-----------------------------------------------------

If we throw an infinite amount of darts at the canvas, we can obtain a good approximation for the value of π
We'll use Monte Carlo simulations to simulate throw outcomes

"""

# Importing libraries
import random
import math
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd

# We'll set the radius of the circle to 1
radius = 1

# Dictionary to store the individual approximations of pi after n simulations
values_dict = {
    "Simulations": [],
    "Pi": []
}

simulations = 10000  # 5000 simulations

for _ in range(1, simulations):
    all_outcomes = [
    ]  # Storing all darts that fall inside (distance to center < 1) and outside the circle boudery (distance to center > 1)
    all_x = []
    all_y = []
    # Randomly shooting darts at the canvas
    for i in range(_):

        x = np.random.uniform(-1, 1)
        all_x.append(x)
        y = np.random.uniform(-1, 1)
        all_y.append(y)

        # We can use Pythagoras' formula to calculate the distance of the dot from the center of the circle
        distance_to_center = np.sqrt((x**2 + y**2))

        if distance_to_center < radius:
            all_outcomes.append(1)
        else:
            all_outcomes.append(0)

    values_dict["Simulations"].append(_)
    values_dict["Pi"].append((sum(all_outcomes) / _) * 4)

pi_estimates_df = pd.DataFrame(data=values_dict)

final_pi_estimation = pi_estimates_df['Pi'].iloc[-1].round(4)
print(f'The estimated value of π is {final_pi_estimation}')



# Plotting the results

# Creating an array to create points that fall within and outside the circle bounderies
hit_miss_array = np.where(np.array(all_outcomes) == 1, 'hit', 'miss') # Used to distinguished points on the graph

fig = plt.figure(figsize=(5, 10))
plt.tight_layout()

ax1 = fig.add_subplot(211)
ax1.set_title('Monte Carlo Simulation to Estimate Value of Pi')
ax1 = sns.scatterplot(all_x, all_y, hue=hit_miss_array, legend=False)

ax2 = fig.add_subplot(212)
ax2 = sns.scatterplot(x="Simulations", y="Pi", data=pi_estimates_df)
ax2.axhline(y=3.14, color='g', linestyle='-')
ax2.annotate(f'Estimated value of pi = {final_pi_estimation}',
             xy=(1, 0),
             xycoords='axes fraction',
             xytext=(-20, 150),
             textcoords='offset pixels',
             horizontalalignment='right',
             verticalalignment='top')

ax2.set_ylabel('Value of Pi')
ax2.set_xlabel('Number of Simulations')

fig.savefig('images/monte_carlo_pi_estimation.png', dpi=300)