# Play rock paper scissors with this program
# This one shows us the proof also!
# For rock -> 2 primes, paper -> 3 primes, scissors -> 4 primes

import math
import os
import random
import time

choices = ['rock','paper','scissors']
computer_points = 0
human_points = 0

human_payoffs = [
    [0,-1,1],
    [1,0,-1],
    [-1,1,0]
    ]

def get_random_prime(count):
    if count == 2:
        time.sleep(0.3)
        start = 100_000_000_000_000
    else:
        time.sleep(0.5)
        total = 1_000_000_000_000_000_000_000_000_000_000_000
        start = int(total**(1/count))
    suspect = random.randint(start - start//8,start + start//8)

    while True:
        is_prime = True
        for i in range(2,int(math.sqrt(suspect))+1):
            if suspect % i == 0:
                is_prime = False
                break
        if is_prime:
            return suspect
        suspect += 1


def get_random_primes(count):
    primes = []
    for i in range(count):
        primes.append(get_random_prime(count))
    return primes

def print_welcome():
    print("Hello, welcome to the rock, paper, scissors game!")

def ask_player_choice():
    choice = ''
    while choice not in choices:
        choice = input(f"Enter a choice: [{choices[0]}/{choices[1]}/{choices[2]}]: ")
    return choices.index(choice)


def ask_continue():
    choice = input("Do you want to play again? [y/n]: ")
    return choice != 'n'

def get_response():
    return random.randint(0,2)

def clear():
    os.system('clear')

def print_stats():
    print(20*"-")
    print(f"Human: {human_points}")
    print(f"Computer: {computer_points}")
    print(20*"-")

clear()
print_welcome()
while True:

    print_stats()

    c_index = get_response()
    primes = get_random_primes(c_index+2)
    print(f"The computer picked something. The proof is: {math.prod(primes)}\n")

    h_index = ask_player_choice()
    print(f"\nThe computer played: {choices[c_index]}\n")
    
    payoff = human_payoffs[h_index][c_index]
    if payoff > 0:
        print("You won!")
        human_points += 1
    elif payoff < 0:
        print("You lost!")
        computer_points += 1
    else:
        print("Tie!")
    
    print(f"The primes to prove computer action: {primes}")

    if not ask_continue():
        break
    clear()

    