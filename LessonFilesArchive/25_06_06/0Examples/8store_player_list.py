# Example of how we can store players using json

import urllib.request

import bs4

import json

# represents a football player
class Player:
    def __init__(self, name, team, nationality, position):
        self.name = name
        self.team = team
        self.nationality = nationality
        self.position = position

    def to_dict(self):
        return {
            "name": self.name,
            "team": self.team,
            "nationality": self.nationality,
            "position": self.position
            }

    def __repr__(self):
        return self.name
    

# retrieves player data from a particular we page
def scrape_players() -> list[Player]:
    odpoved = urllib.request.urlopen("https://www.givemesport.com/ballon-dor-power-rankings/")

    polivka = bs4.BeautifulSoup(odpoved, "html.parser")

    tables = polivka.find_all("table")
    rows = tables[0].find_all("tr")
    sloupce = rows[3].find_all("td")

    players : list[Player] = []
    for row in rows[2:]:

        sloupce = row.find_all("td")
        players.append(Player(sloupce[1].p.text, sloupce[2].p.text, sloupce[3].p.text, sloupce[4].p.text))

    return players


players = scrape_players()
with open("25_06_06/players.json","w") as file:
    json.dump([player.to_dict() for player in players],file,indent=2)
