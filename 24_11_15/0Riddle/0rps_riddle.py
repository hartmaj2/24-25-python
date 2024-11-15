# Play rock paper scissors with this program
# Is there anything suspicious about it?


import os

choices = ['rock','paper','scissors']
responses = ['paper','scissors','rock']
computer_points = 0
human_points = 0


def print_welcome():
    print("Hello, welcome to the rock, paper, scissors game!")

def ask_player_choice():
    choice = ''
    while choice not in choices:
        choice = input(f"Enter a choice: [{choices[0]}/{choices[1]}/{choices[2]}]: ")
    return choice


def ask_continue():
    choice = input("Do you want to play again? [y/n]: ")
    return choice != 'n'

def get_response(choice):
    return responses[choices.index(choice)]

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
    print("The computer picked something. But I will show you only after you play.\n")
    choice = ask_player_choice()
    print(f"\nThe computer played: {get_response(choice)}\n")
    print("You lost!")
    computer_points += 1
    if not ask_continue():
        break
    clear()

    