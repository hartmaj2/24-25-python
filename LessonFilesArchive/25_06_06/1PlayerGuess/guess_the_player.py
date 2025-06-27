import os
import urllib.request
import random
import time
from http.client import HTTPResponse

from typing import Callable

import bs4

class Player:

    def __init__(self, name, team, nationality, position):
        self.name = name
        self.team = team
        self.nationality = nationality
        self.position = position

    def __repr__(self):
        return self.name

    def is_from_nationality(self, country):
        return self.nationality == country
        
    def is_from_team(self, team):
        return self.team == team

    def is_from_position(self, position):    
        return self.position == position

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


def clear():
    os.system("clear")

clear()


# the program should guess a player based on input of the user

# first, it should find out the position
#   find counts of possible positions
#       ask for the most popular one
#   ask until don't know the position exactly

# then find out the team
#   find counts of players based on teams
#       ask for the most popular one
#   have a limit on how many times we ask (maybe ask a random question as well)

# find_most_popular ...

# returns the most popular value for the attribute given by the selector
def find_most_popular_value(selector : Callable[[Player],str], players : list[Player]) -> str:
    counts : dict[str,int] = get_counts_for_attribute(selector,players)
    max_count = 0
    max_val = ""
    for key in counts:
        print(f"{key:20}{counts[key]}")
        if max_count < counts[key]:
            max_count = counts[key]
            max_val = key
    return max_val

def get_counts_for_attribute(selector : Callable[[Player],str], players : list[Player]) -> dict[str,int]:
    counts : dict[str,int] = {}
    for player in players:
        attr_value = selector(player)
        if attr_value not in counts:
            counts[attr_value] = 0
        counts[attr_value] += 1
    return counts

# ask_attribute ...

def ask_nationality(players : list[Player], nationality : str):
    
    new_players = []
    input_lol = input(f"is your player from {nationality}?").lower()

    clear()

    if input_lol == "no":
        for player in players:
            if player.is_from_nationality(nationality) == False:
                new_players.append(player)


    elif input_lol== "yes":
        for player in players:
            if player.is_from_nationality(nationality) == True:
                new_players.append(player)

    players = new_players


def ask_team(team):
    global players
    new_players = []
    input_lol = input(f"does your player play in {team}?").lower()

    clear()


    if input_lol == "no":
        
        for player in players:
            if player.is_from_team(team) == False:
                new_players.append(player)


    elif input_lol== "yes":
        for player in players:
            if player.is_from_team(team) == True:
                new_players.append(player)

    players = new_players


def ask_position(position):
    global players
    new_players = []
    input_lol = input(f"is your player a {position}?").lower()

    clear()


    if input_lol == "no":
        
        for player in players:
            if player.is_from_position(position) == False:
                new_players.append(player)


    elif input_lol== "yes":
        for player in players:
            if player.is_from_position(position) == True:
                new_players.append(player)

    players = new_players


def print_player_names(players : list[Player]):
    for player in players:
        print(player.name)
    print(len(players))








def find_most_helpfull():
    global best_kriterium, best_name, best_number


    nationalities = []
    teams = []
    positions = []

    
    best_number = 0
    best_name = None
    best_kriterium = None

    for player in players:
        nationalities.append(player.nationality)
        teams.append(player.team)
        positions.append(player.position)



    for i in range(len(nationalities)):
        if nationalities.count(nationalities[i]) > best_number and nationalities.count(nationalities[i]) < len(nationalities):
            best_number = nationalities.count(nationalities[i])
            best_name = nationalities[i]
            best_kriterium = "nationality"



    for i in range(len(teams)):
        if teams.count(teams[i]) > best_number and teams.count(teams[i]) < len(teams):
            best_number = teams.count(teams[i])
            best_name = teams[i]
            best_kriterium = "team"


    for i in range(len(positions)):
        if positions.count(positions[i]) > best_number and positions.count(positions[i]) < len(positions):
            best_number = positions.count(positions[i])
            best_name = positions[i]
            best_kriterium = "position"





clear()

# find_most_helpfull()

def ask_best(players : list[Player]):

    find_most_helpfull()

    if best_kriterium == "nationality":
        ask_nationality(best_name)


    if best_kriterium == "team":
        ask_team(best_name)


    if best_kriterium == "position":
        ask_position(best_name)

def my_test():
    players = scrape_players()
    selector : Callable[[Player],str] = lambda player : player.team
    val = find_most_popular_value(selector,players)
    print(val)


players = scrape_players()
print("hello")
for i in range(100):
    if len(players) == 1:
        if input(f"Is your player {players[0].name}?") == "yes":
            clear()
            print("Lets goooo")
            exit()

    ask_best()
