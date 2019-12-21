import random
a = input()

sayi = int(a)
ops = ['+', '*']
def encode(x):
    operation = random.randint(0, 1)
    operationNumber = random.randint(100, 999)
    result = str(operationNumber)
    result += ops[operation]
    if(operation == 0):
        result += str(x + operationNumber)
    if(operation == 1):
        result += str(x * operationNumber)
    return result

def decode(x):
    number = 0
    if('+' in x):
        operationNumber = int(x[0:x.index('+')])
        number = int(x[x.index('+') + 1:])
        number -= operationNumber
    if('*' in x):
        operationNumber = int(x[0:x.index('*')])
        number = int(x[x.index('*') + 1:])
        number //= operationNumber
    return number

encoded = encode(sayi)
print(encoded)

print(decode(encoded))