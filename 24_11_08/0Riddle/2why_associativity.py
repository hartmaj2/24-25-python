# Why we have left associativity

vydelek = 1000 + 100 - 100 - 300 - 230 + 30


vydelek2 = 1000 + (100 - (100 - (300 - (230 + 30))))

print(f"Normalni asociativita: {vydelek}")
print(f"Nenormalni asociativita: {vydelek2}")