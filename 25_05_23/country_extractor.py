# Program for web scraping data from wikipedia page with capital cities and their populations

import urllib.request as req
from http.client import HTTPResponse # for autocomplete to work (is imported by urllib but then we don't have type hints)

from bs4 import BeautifulSoup
from bs4 import Tag

from country import Country

def get_soup(url : str) -> BeautifulSoup:
    response : HTTPResponse = req.urlopen(url)
    soup : BeautifulSoup = BeautifulSoup(response,"html.parser")
    return soup

def countries_from_table(wikitable : Tag, n : int) -> list[Country]:
    countries : list[Country] = []
    rows = wikitable.find_all("tr")
    for row in rows[1:n+1]:
        if not isinstance(row,Tag):
            break
        country = country_from_table_row(row)
        countries.append(country)
    return countries

def country_from_table_row(row : Tag) -> Country:
    columns = row.find_all("td")
    country = Country()
    country.name = get_cleaned_string(str(columns[0].text).replace("*","").strip())
    country.capital = get_cleaned_string(str(columns[1].text).strip())
    country.population = int(str(columns[2].text).replace(",","").strip())
    return country

def get_cleaned_string(raw : str):
    chars_to_cut = ["(","[",","]
    new_str = raw
    for char in chars_to_cut:
        i = new_str.find(char)
        if i != -1:
            new_str = new_str[:i]
    return new_str


def extract_countries(n : int) -> list[Country]:
    soup = get_soup("https://en.wikipedia.org/wiki/List_of_national_capitals_by_population")
    wikitable = soup.find("table",attrs={"class":"wikitable"})

    if not isinstance(wikitable,Tag):
        exit()

    countries = countries_from_table(wikitable,n)

    return countries


