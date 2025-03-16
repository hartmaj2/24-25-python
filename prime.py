# Example of a randomized algorithm
# What does it do?
# Can we be certain about something if it responds False? And when it responds True?

import random

def is_prime(x):
    r = random.randint(2,x-1)
    z = x % r
    if z == 0:
        return False
    else:
        return True
    
x = 10
print(f"{x} is prime: {is_prime(x)}")