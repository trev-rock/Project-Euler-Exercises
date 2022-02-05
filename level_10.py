import math
prime = 2


def prime_tester(x):
    for y in range(2, int(math.sqrt(x)+1)):
        if x % y == 0:
            return False
    return True


for x in range(3, 2000000, 2):
    if prime_tester(x) == True:
        prime += x
print(prime)
