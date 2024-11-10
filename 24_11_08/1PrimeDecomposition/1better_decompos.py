# Explain how is prime decomposition used in cryptography

import time

number = int(input("Enter a number: "))
divisor = 2
rozklad = []

start_time = time.time()

while number != 1:
    if number % divisor == 0:
        number = number // divisor # the // is important here!
        rozklad.append(divisor)
    else:
        divisor += 1


print(f"Elapsed time: {time.time()-start_time}")
print(rozklad)

# CASE 1:
# prime 1: 75024347
# prime 2: 46271341
# product: 3471477143339327

# CASE 1:
# prime 1: 113815369
# prime 2: 367251953
# product: 41798916546665657
# (took 31.84630584716797 seconds in Python)
# (took 25.508955240249634 seconds in Python)
# (460 miliseconds in C++)

# Composition vs decomposition is an example of one way function
# it is easy to compose but the other way is not possible/hard

# This could be used to test if computer is not cheating on us
# He would send us his public key: prime number
# Then he would have to  