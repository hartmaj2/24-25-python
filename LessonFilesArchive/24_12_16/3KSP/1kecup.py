file = open("01.in","r") # otevrit soubor

line = file.readline() # precte radek
numbers = line.split() # rozdeli radek

pocet_lidi = int(numbers[0])

output_file = open("res.txt","w")

for i in range(pocet_lidi):
    # 
    output_file.write("hello\n")
# pocet_lidi = 
# print(numbers)