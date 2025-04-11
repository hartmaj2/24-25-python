# First explain how html works

# We need to be able to get the html content of the webpage first

import requests

from bs4 import BeautifulSoup

url = "https://hartmaj2.github.io/"
url = "https://en.wikipedia.org/wiki/List_of_national_capitals"
response : requests.Response = requests.get(url)
# print(response.text)

soup = BeautifulSoup(response.text,"html.parser")

table = soup.find("table",{"class":"wikitable"})

print(table)