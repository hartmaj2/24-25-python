
soucet = 0

def funkce(i,nejvetsi):
    global soucet
    soucet += i
    if i != nejvetsi:
        funkce(i+1,nejvetsi)
    else:
        print(soucet)

funkce(0,3)

