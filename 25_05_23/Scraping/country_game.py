# This is a game which lets you guess, which capital city has a higher population

# This game uses the country_extractor to get the list of countries
# Country is an object described in country module (name,capital,population)

import country_extractor as ce
import random
from country import Country

import os

def print_result_row(country : Country):
    print(f"{country.capital:<30}{country.population:,}{"capital of ":>20}{country.name}")

def get_more_populous_country(country1 : Country, country2 : Country):
    correct = country2
    if country1.population > country2.population:
        correct = country1
    return correct

def run_round(country1 : Country, country2 : Country):

    correct  = get_more_populous_country(country1,country2)

    print(f"{country1.capital:20} X {country2.capital:>20}")
    selection = input("Which city has bigger population? :").strip()

    if selection == correct.capital:
        print("Correct!")
    else:
        print("Wrong!")

    print_result_row(country1)
    print_result_row(country2)

countries = ce.extract_countries(150)

random.shuffle(countries)

magic_word = "no"
response = ""
while response != magic_word:
    os.system("clear")
    country1, country2  = countries.pop(), countries.pop()
    run_round(country1,country2)
    response = input("Do you wish to continue?")
