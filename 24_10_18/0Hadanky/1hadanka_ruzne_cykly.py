# Jaky je rozdil mezi tremi nasledujicimi cykly?
# vizualizovat v [python tutor](https://pythontutor.com/)

seznam = ["kocka","vlocka","cocka","ocka"]

print("0.")
i = 0
while i < 4:
    print(i)
    i = i + 1


print("1.")
i = 0
while i < 4:
    print(seznam[i])
    i = i + 1


print("2.")
# 2.
for i in range(4):
    print(seznam[i])


print("3.")
# 3.
for prvek in seznam:
    print(prvek)

