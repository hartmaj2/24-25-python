# Functions can have a return value (they poop it out so we can use it right away)

def get_number_input():
    choice = ""
    while True:
        choice = input("Enter a number: ")
        if choice.isnumeric():
            break
        print("Not a number!")
    choice = int(choice)
    return choice

print()
cislo1 = get_number_input()
cislo2 = get_number_input()

print(f"Result {cislo1 + cislo2}")

# built-in examples of parameterless functions with return value
# 1. input()
# 2. time.time()