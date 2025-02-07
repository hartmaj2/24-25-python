# Zkus si nasledujici kody spustit v debuggeru s breakpointem (cervenou teckou)
# na prikazu print("Zacatek"). Hodne ti to pomuze v pochopeni funkci.
import os

print("Zacatek")


# funkce tisknouci pravidla
def tiskni_pravidla_hry():
    print(20 * "-")
    print("Pravidla hry:")
    print("1. Úkolem je porazit bosse.")
    print("2. Abys porazil bosse, tak musíš trénovat.")
    print("3. Pokud ti dojde zdraví, hra končí.")
    print(20 * "-")

def vytiskni_menu():
    print("0 - ukonci hru")
    print("1 - vypis pravidla hry")
    print("2 - jsi trenovat")


os.system("clear")
tiskni_pravidla_hry()
choice = "-1"
while choice != "0":
    vytiskni_menu()
    choice = input("Enter choice: ")
    if choice == "0":
        print("Goodbye")
    if choice == "1":
        tiskni_pravidla_hry()
    if choice == "2":
        print("Hrac trenuje")
    input()
    os.system("clear")

# Pro a proti toho mit funkci nebo funkci nemit
# Pro: upravime li kod ve funkci, zmeni se chovani na vsech mistech
# Proti: musime se zamyslet, jak cast kodu pojmenujeme (jak tu funkci pojmenujeme)

### VERZE 2 ###

# os.system("clear")
# print(20 * "-")
# print("Pravidla hry:")
# print("1. Úkolem je porazit bosse.")
# print("2. Abys porazil bosse, tak musíš trénovat.")
# print("3. Pokud ti dojde zdraví, hra končí.")
# print(20 * "-")
# choice = "-1"
# while choice != "0":
#     vytiskni_menu()
#     choice = input("Enter choice: ")
#     if choice == "0":
#         print("Goodbye")
#     if choice == "1":
#         print(20 * "-")
#         print("Pravidla hry:")
#         print("1. Úkolem je porazit bosse.")
#         print("2. Abys porazil bosse, tak musíš trénovat.")
#         print("3. Pokud ti dojde zdraví, hra končí.")
#         print(20 * "-")
#     if choice == "2":
#         print("Hrac trenuje")
#     input()
#     os.system("clear")