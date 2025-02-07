# Why multiplication before addition?

produkt = ["jablko","banan","rohlik"]
pocet = [3,4,3]
cena = [10,5,2]

ucet = pocet[0] * cena[0] + pocet[1] * cena[1] + pocet[2] * cena[2]

ucet2 = pocet[0] * (cena[0] + pocet[1]) * (cena[1] + pocet[2]) * cena[2]

print(f"Normalni precedence: {ucet}")
print(f"Obracena precedence: {ucet2}")