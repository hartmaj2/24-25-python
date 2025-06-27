import os
import urllib.request
import random
import time
from http.client import HTTPResponse

from typing import Callable

import bs4


# represents a football player
class Player:
    def __init__(self, name, team, nationality, position):
        self.name = name
        self.team = team
        self.nationality = nationality
        self.position = position


    def __repr__(self):
        return self.name


def clear():
    os.system("clear")


# retrieves player data from a particular we page
def scrape_players() -> list[Player]:
    odpoved : HTTPResponse = urllib.request.urlopen("https://www.givemesport.com/ballon-dor-power-rankings/")

    polivka = bs4.BeautifulSoup(odpoved, "html.parser")

    tables = polivka.find_all("table")
    rows = tables[0].find_all("tr")
    sloupce = rows[3].find_all("td")

    players : list[Player] = []
    for row in rows[2:]:

        sloupce = row.find_all("td")
        players.append(Player(sloupce[1].p.text, sloupce[2].p.text, sloupce[3].p.text, sloupce[4].p.text))

    return players
    
clear()

# functions Game_nationalities() and Game_Teams() look very similar
# what are the differences?
#   correct_answer is set based on nationality or team -> would be good to pass that information to the function from the outside
#   different part of thext: Which [country/team] is -||--

# plays a guessing game, takes players
# chooses player attribute to ask for based on selector function
# should provide attr_name for correct attribute text to display
def play_guessing_game(players : list[Player], selector : Callable[[Player],str], attr_name : str):
    points = 0
    wait_time = 2
    max_points = len(players)

    for i in range(len(players)):
        clear()
        random_number = random.randint(0, len(players) - 1)
        correct_answer = selector(players[random_number]).lower()
        if input(f"Hello! What is the {attr_name} of {players[random_number]}? \n").lower() == correct_answer:
            print("Thats correct!!!")
            time.sleep(wait_time)
            points += 1
        else:
            print(f"stupid idiot... Its {correct_answer}")
            time.sleep(wait_time)

        players.pop(random_number)


    print(f"You got {points} points out of {max_points}") 


# functions that take a player and retrieve the attribute of the player which we want
def nationality_selector(player : Player) -> str:
    return player.nationality

def team_selector(player : Player) -> str:
    return player.team

def position_selector(player : Player) -> str:
    return player.position

players = scrape_players()

game_wanted = input("Which game do you want to play? \n 1- Nationallity game \n 2- Team game \n 3- Position game \n")

if game_wanted == "1":
    play_guessing_game(players,nationality_selector,"nationality")

elif game_wanted == "2":
    play_guessing_game(players,team_selector,"team")

elif game_wanted == "3":
    play_guessing_game(players,position_selector,"position")