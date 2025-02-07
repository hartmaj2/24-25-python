import math
import random

primes = []
start = random.randint(100_000_000,1_000_000_000)
end = start + 100

for suspect in range(start,end+1):
    is_prime = True
    for i in range(2,int(math.sqrt(suspect))+1):
        if suspect % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(suspect)

print(primes)