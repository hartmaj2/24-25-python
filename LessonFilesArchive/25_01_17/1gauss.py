def recursive_gauss(x):
    if x == 0:
        return 0
    else:
        return x + recursive_gauss(x-1)
    
def smart_gauss(x):
    return ((x+1)*x) // 2

result = recursive_gauss(100)
print(result)