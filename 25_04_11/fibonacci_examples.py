import math
import time

# Story
# Fibonacci was counting how rabbit population grows and it can be simulated using fibonacci sequence
# one catch: it assumes that we have invincible rabbits

# Using list

# Useful indexing
def useful_indexing():
    l = [1,2,3,4]
    print(l[-1]) # indexes from the end but starts at -1 !!!

# TODO: create a list which will contain the amount of rabbits at year i at position i

def fibonacci_list(years : int):
    rabbits = [0,1]
    for i in range(years):
        new_population = rabbits[-1] + rabbits[-2]
        rabbits.append(new_population)
    # print(rabbits)
    return rabbits[-1]



# Example of a recursive function
def fibonacci_recursive(n : int):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# TODO: challenge: try using just three variables 
# Using just two variables
def fibonacci_vars(years : int):
    last_year = 0
    now = 1
    for i in range(years):
        save = now
        now = now + last_year
        last_year = save
    return now

# Example of calculating fibonacci numbers using explicit formula 
# Will that be faster or slower than the previous versions?
def fibonacci_formula(n : int):
    phi = (math.sqrt(5) + 1) / 2
    return int((phi**(n+1) - (-1/phi)**(n+1)) / math.sqrt(5))

n = 100_000

start = time.time()
fib1 = fibonacci_list(n)
# print(fib1)
print(f"time: {time.time()-start}")

# fib2 = fibonacci_recursive(n)
# print(f"{fib2=}")
# print(f"time: {time.time()-start}")

fib3 = fibonacci_vars(n)
# print(fib3)
print(f"time: {time.time()-start}")

# fib4 = fibonacci_formula(n)
# print(f"{fib4=}")
# print(f"time: {time.time()-start}")