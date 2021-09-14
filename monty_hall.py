"""
The Monty Hall Problem

In the first chapter, Allen B. Downey introduces the Monty Hall problem:

Monty shows you three closed doors and tells you that there is a prize 
behind each door: one prize is a car, the other two are less valuable 
prizes like peanut butter and fake fingernails. The prizes are arranged 
at random.

The object of the game is to guess which door has the car. If you guess 
right, you get to keep the car.

You pick a door, which we will call Door A. We’ll call the other doors B 
and C. Before opening the door you chose, Monty increases the suspense by 
opening either Door B or C, whichever does not have the car. (If the car 
is actually behind Door A, Monty can safely open B or C, so he chooses one 
at random.)

Then Monty offers you the option to stick with your original choice or switch 
to the one remaining unopened door.

SHOULD YOU STAY OR SWITCH?

Here we use Monte Carlo simulations to show that the best strategy is to switch.
"""


# Importing libraries
import random
import matplotlib.pyplot as plt


stay_probabilities = []  # Probability values when player stays with his first choice (i.e. player_choice)
switch_probabilities = []  # Probability values when player switches his choice (i.e. player_choice_2)


def monty_hall(simulations):

    stay_wins = 0  # Wins when player stays with his first choice (i.e. player_choice)
    switch_wins = 0  # Wins when player switches his choice (i.e. player_choice_2)

    for sim in range(1, simulations):

        doors = ['goat', 'goat', 'car']

        # The player first chooses a door
        player_choice = random.choice(doors)
        if player_choice == 'car': # This is the case where the player chooses the correct door on his firt attempt, P=1/3.
            stay_wins += 1

        temp_stay_probability = stay_wins / sim
        stay_probabilities.append(temp_stay_probability)

        # The host then removes one of the remaining doors not chosen by the contestant -- The removed door cannot be the 'car' and is always a 'goat'
        doors.remove('goat')
        remaining_doors = doors

        remaining_doors.remove(
            player_choice)  # Here, the player switches his initial choice and chooses the remaining door
        player_choice_2 = remaining_doors[0]
        if player_choice_2 == 'car':
            switch_wins += 1

        temp_switch_probability = switch_wins / sim
        switch_probabilities.append(temp_switch_probability)

    stay_win_prob = stay_wins / simulations
    print(
        f'The Probability of winning the car when staying is initial choice is: {stay_win_prob}'
    )

    switch_wins_prob = switch_wins / simulations
    print(
        f'The Probability of winning the car when switching: {switch_wins_prob}'
    )

    # Plotting the results
    plt.style.use('fivethirtyeight')
    plt.title('Monte Carlo Simulations of Monty Hall Strategy',
              fontsize=16)
    plt.axhline(0.333, color='g')
    plt.axhline(0.666, color='purple')
    plt.xlabel('Number of Simulations', fontsize=12)
    plt.ylabel('Probability Values', fontsize=12)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.plot(stay_probabilities, label='Stay')
    plt.plot(switch_probabilities, label='Switch door')
    plt.legend(loc="upper right")
    plt.annotate(
        f'Win Probability if Switch = {switch_wins_prob}\nWin Probability if Stay = {stay_win_prob}',
        xy=(1, 0),
        xycoords='axes fraction',
        xytext=(-20, 120),
        textcoords='offset pixels',
        horizontalalignment='right',
        verticalalignment='top',
        fontsize=10)
    plt.tight_layout()
    plt.savefig('images/monty_hall_monte_carlo.png', dpi=300)


monty_hall(1000)