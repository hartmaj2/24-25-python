# Example showing, that we can store functions in a variable and call them later

# Function tester, it is a function that takes another function and tests what it does

import random

def greeter():
    print(f"Hello friend!")

def random_numbers_generator():
    return [random.randint(0,100) for _ in range(10)]

# CHOOSE FUNCTION HERE:
func = random_numbers_generator

print(50*"-")
print(f"Testing function: {func}")
res = func()
print(f"Result: {res}")
print(50*"-")
print()