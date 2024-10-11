# Tutorial, jak vandalizovat pocitac vytvorenim X souboru 

# 1.TODO: Zkus nejprve otevrit jeden soubor a neco z nej precist
# HINT 1: staci `file = open("jmeno_souboru")`
# HINT 2: do jmena souboru je potreba zadat cela cesta, pouzij `copy relative path`
# HINT 3: nezapomen na file.close()

file = open("24_10_11/0hadanka.py")
precteno = file.readline()
while precteno != "":
    print(f"Precetl jsem {precteno}")
    precteno = file.readline()
file.close()

# Moznost pouze cist soubory je slaba, nastesti Python umoznuje do nich i neco psat!
# 2. TODO: Pripis k vyplatam, 1000 na zacatek, at mame vice penez
# HINT: Nejlehci bude, vytvorit novy soubor a psat vysledek do nej, ten stary nechame byt

file_in = open("24_10_11/1Soubory/vyplaty.txt","r")
file_out = open("vyplaty.txt","w")
precteno = file_in.readline()
for i in range(10):
    precteno = file_in.readline()
    file_out.write("1000" + precteno)
file_in.close()
file_out.close()

# Nyni uz mas dobre znalosti praci se soubory, abys mohl uspesne vandalizovat cizi pocitac
# 3. TODO: Vytvor 10 souboru a do kazdeho napis neco jako: Vandalizoval jsem ti kompa

for i in range(10):
    file = open(f"file_{i}","w")
    file.write("Vandalizoval jsem ti kompa")
    file.close()