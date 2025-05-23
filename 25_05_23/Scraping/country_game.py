import country_extractor as ce
import random
from country import Country

import os

def run_round(country1 : Country, country2 : Country):
    correct = country2
    if country1.population > country2.population:
        correct = country1

    print(f"{country1.capital:20} X {country2.capital:>20}")
    selection = input("Which city has bigger population? :").strip()

    if selection == correct.capital:
        print("Correct!")
    else:
        print("Wrong!")

    print(f"{country1}")
    print(f"{country2}")

countries = ce.extract_countries(150)

random.shuffle(countries)

magic_word = "no"
response = ""
while response != magic_word:
    os.system("clear")
    country1, country2  = countries.pop(), countries.pop()
    run_round(country1,country2)
    response = input("Do you wish to continue?")
