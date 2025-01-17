# What will the following code do

def magic(number):
    if number == 3:
        return
    else:
        print("baaaaah")
        magic(number+1)

magic(0)