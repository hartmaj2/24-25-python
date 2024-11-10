# Explain how is prime decomposition used in cryptography

number = int(input("Enter a number: "))
divisor = 2
rozklad = []

while number != 1:
    remainder = number % divisor
    if remainder == 0:
        number = number // divisor # the // is important here!
        rozklad.append(divisor)
    else:
        divisor += 1

print(rozklad)