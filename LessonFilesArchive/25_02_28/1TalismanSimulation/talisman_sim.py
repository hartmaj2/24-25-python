# We want to pass through the crypt
# Our hero has power n
# The enemy rolls three dice 
# We decrease the enemys roll by our power, if still enemy has nonzero power left, we lose

# The following program simulates the probability by doing multiple repetitions of the random events

import random

def crypt_trial(hero_power : int):
    rolls = 0
    for i in range(3):
        rolls += random.randint(1,6)
    return rolls - hero_power

def simulate_multiple(hero_power : int, repetitions : int):
    wins = 0
    for i in range(repetitions):
        res = crypt_trial(hero_power)
        if res <= 0:
            wins += 1
    return wins / repetitions

hero_power = 9
repetitions = 100_000
prob = simulate_multiple(hero_power,repetitions)
print(f"Estimated probability of your hero passing is {prob}")
