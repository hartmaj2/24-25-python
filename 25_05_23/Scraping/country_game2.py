# This is a game which lets you guess what is the capital city of the given country

# This game uses the country_extractor to get the list of countries
# Country is an object described in country module (name,capital,population)

import country_extractor as ce
import random
from country import Country

import os

def run_round(country : Country):

    correct = country.capital

    response = input(f"What is the capital city of {country.name}? ")
    if response == correct:
        print("Correct!")
    else:
        print("Wrong!")
    
    print(f"The capital city is {correct}")

countries = ce.extract_countries(150)

random.shuffle(countries)

magic_word = "no"
response = ""
while response != magic_word:
    os.system("clear")
    country = countries.pop()
    run_round(country)
    response = input("Do you wish to continue?")