# Explain how is prime decomposition used in cryptography

import sys

number = int(input("Enter a number: "))
divisor = 2
rozklad = []

while number != 1:
    remainder = number % divisor
    if remainder == 0:
        number = number // divisor
        rozklad.append(divisor)
    else:
        divisor += 1

print(rozklad)