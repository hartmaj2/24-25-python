# vraceni vysledku pomoci return
def odpoved_na_otazku_vseho():
    print("Hmmm... premyslim nad odpovedi.")
    print("Uz to mam!")
    return 42

# kontrola vraceneho vysledku
if odpoved_na_otazku_vseho() == 42:
    print("To je spravna odpoved")

# ulozit vysledek do prom.
odpoved = odpoved_na_otazku_vseho()
print("Odpoved je " + str(odpoved))

# vice param. + vraceni hodnoty
# komplikovany vypocet -> schovat do funkce
# (!) na poradi parametru zalezi
# TODO: zkontroluj zda promenna damage existuje i mimo funkci spocitej_damage nebo ne
def spocitej_damage(defense_obrance,attack_utocnika):
    damage = ((attack_utocnika + 10) * 1.5 - defense_obrance * 0.5) / 2
    return damage

skret_attack = 10
hero_defense = 9
hero_health = 15
print("Skret utoci")
input()
hero_health = hero_health - spocitej_damage(hero_defense,skret_attack)
print("Hrdina utpel",spocitej_damage(hero_defense,skret_attack),"damage!")

print("Konec")