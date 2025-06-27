# Example: how to make the code shorter when returning True or False from if statement
# to show in thonny

num1 = 10
num2 = 14

def are_same1(a,b):
    if a == b:
        return True
    else:
        return False
    
def are_same2(a,b):
    return a == b

res1 = are_same1(num1,num2)

res2 = are_same2(num1,num2)