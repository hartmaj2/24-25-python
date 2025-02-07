# Pri praci s funkcemi se nam casto bude hodit pouzit klicove slovo global
# K cemu vlastne to klicove slovo je?

def calculate_points1():
    points = 2 * kills - 0.5 * deaths + assists  # some weird formula
    print(f"Points: {points}")


points = 0

kills = 10
deaths = 3
assists = 5

print(f"Points: {points}")

calculate_points1()

print(f"Points: {points}")











# calculate_points2()

# def calculate_points2():
#     global points
#     points = 2 * kills - 0.5 * deaths + assists  # some weird formula
#     print(f"Points: {points}")