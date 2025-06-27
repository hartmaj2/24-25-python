import urllib.request 
from http.client import HTTPResponse

import bs4

class Player:

    def __init__(self,jmeno):
        self.name = jmeno

odpoved : HTTPResponse = urllib.request.urlopen(r"https://en.wikipedia.org/wiki/The_World%27s_Billionaires")


polivka = bs4.BeautifulSoup(odpoved,"html.parser")

# print(polivka.html.head.title.text)

tables = polivka.find_all("table",{"class":"sortable"})

first = tables[0]

rows = first.find_all("tr")

for row in rows:
    columns = row.find_all("td")

    for col in columns:
        print(50 * "-")
        print(col.span)

    print(100 * "X")



