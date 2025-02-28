# We want to pass through the crypt
# Our hero has power n
# The enemy rolls three dice 
# We decrease the enemys roll by our power, if still enemy has nonzero power left, we lose

# The following program will calculate the probability exactly

def calc_distribution():
    distrib = [0 for x in range(19)]
    for i in range(1,7):
        for j in range(1,7):
            for k in range(1,7):
                outcome = i + j + k
                distrib[outcome] += 1
    return distrib

# def sum(distrib : list[int]):
#     sum = 0
#     for num in distrib:
#         sum += num
#     return sum

def sum(distrib : list[int]):
    return sum_up_to(distrib,len(distrib)-1)

def sum_up_to(distrib: list[int], limit : int):
    sum = 0
    for i in range(limit + 1):
        sum += distrib[i]
    return sum

print(f"Distribution is {calc_distribution()}")

hero_power = 5
distrib = calc_distribution()
prob = sum_up_to(distrib,hero_power)/sum(distrib)
print(f"Prob that hero passes is {prob}")