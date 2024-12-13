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

def find_unique_names(filename):
    names = []
    file = open(filename,"r")
    file.readline()
    for line in file:
        line = line.strip()
        if line not in names:
            names.append(line)
    file.close()
    return names

# TODO: Load unique names and then calculate occurences, after that, find a maximum

def calculate_name_frequencies(filename):

    names = find_unique_names(filename)

    counts = len(names) * [0]
    file = open(filename,"r")
    file.readline()
    for line in file:
        line = line.strip()
        index = names.index(line)
        counts[index] += 1
    file.close()
    
    return names, counts
        
# TODO: Find index of maximum count name -> print the name and the count

def find_maximum(filename):

    names, count = calculate_name_frequencies(filename)

    maximum_index = 0

    for i in range(len(names)):
        if count[i] > count[maximum_index]:
            maximum_index = i
        
    print(names[maximum_index],count[maximum_index])

find_maximum("05.in")