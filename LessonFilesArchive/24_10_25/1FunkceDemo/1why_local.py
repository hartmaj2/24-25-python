# Proc by python byl udelany tak, aby promenne uvnitr funkci nemohli byt videne odjinud?
# Promenna proste po skonceni funkce zahyne, pokud neni global (jinak je takzvane local)

# TODO: Zamyslet se, proc existuji lokalni/globalni promenne?

helpers = ["Legolas","Gimli","Aragorn"]
helper_powers = [30,20,50]

def calculate_hero_power():
    # global count
    count = base_power
    for power in helper_powers:
        count += power
    print(f"Hero power is {count}")
    return count

base_power = 14
count = 0 # pocet killu (uz zabil 10 orku)

orc_power = 20
hero_power = calculate_hero_power()
if hero_power > orc_power:
    print(f"Hero just killed one orc.")
    count += 1 # killed an ork

print(f"Hero killed {count} orcs in total.")

# POUCENI:
# 1. kdyby vsechny promenne byly global, tak bude ve vetsim projektu ohromny zmatek
# 2. je dobre, ze nas python nuti tam psat global, protoze pak aspon vime, ktere promenne menime a nezapomeneme na to
# 3. lepsi je, aby funkce co nejvice komunikovaly pouze pomoci parametru a navratovych hodnot
#   (kdyz je totiz funkce izolovana, tak muzeme hezky s klidnou mysli kontrolovat, co dela a nemusime litat ocima mimo kod samotne funkce) 