# Mame seznam jmen:

# 7
# Novak
# Hroch
# Novak
# Kos
# Vrabec
# Hroch
# Hroch

# TODO: Read all the lines of the input and print them

def print_names():
    file = open("input.txt","r")

    file.readline()
    line = file.readline()
    while line != "":
        print(f"Input: {line}")
        line = file.readline()
    file.close()

# TODO: How to find all unique names and accumulate them in a list

def find_unique_names():
    names = []
    file = open("input.txt","r")
    file.readline()
    for line in file:
        line = line.strip()
        if line not in names:
            names.append(line)
    file.close()
    print(names)

# TODO: Load unique names and then calculate occurences, after that, find a maximum

def calculate_name_frequencies():

    names = []
    file = open("input.txt","r")
    file.readline()
    for line in file:
        line = line.strip()
        if line not in names:
            names.append(line)
    file.close()

    counts = len(names) * [0]
    file = open("input.txt","r")
    file.readline()
    for line in file:
        line = line.strip()
        index = names.index(line)
        counts[index] += 1
    file.close()
    print(names)
    print(counts)
        
# TODO: Find index of maximum count name -> print the name and the count

calculate_name_frequencies()