# Play rock paper scissors with this program
# This one should be fine. But can we really trust it?


import os
import random

choices = ['rock','paper','scissors']
computer_points = 0
human_points = 0

human_payoffs = [
    [0,-1,1],
    [1,0,-1],
    [-1,1,0]
    ]

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
    print("The computer picked something. But I will show you only after you play.\n")

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
    
    if not ask_continue():
        break
    clear()

    