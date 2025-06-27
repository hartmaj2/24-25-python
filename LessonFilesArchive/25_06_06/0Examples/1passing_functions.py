# Example code to show that we can pass functions as parameters as well 

# Function tester, it is a function that takes another function and tests what it does

import random

def tester(function):
    print(50*"-")
    print(f"Testing function: {function}")
    res = function()
    print(f"Result: {res}")
    print(50*"-")
    print()

def greeter():
    print(f"Hello friend!")

def random_numbers_generator():
    return [random.randint(0,100) for _ in range(10)]


tester(random_numbers_generator)

tester(greeter)
