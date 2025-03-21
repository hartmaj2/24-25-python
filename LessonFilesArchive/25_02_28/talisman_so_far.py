import random

seznam = []
repetitions = 1_000_000
hero_power = 10

for i in range(19):
    seznam.append(0)

for i in range(repetitions):
    vysledek = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
    seznam[vysledek] += 1

sum = 0
for i in range(hero_power+1):
    if i >= len(seznam):
        break
    sum += seznam[i]

print(f"Result: {sum/repetitions}")
    


print(seznam)
print(vysledek)