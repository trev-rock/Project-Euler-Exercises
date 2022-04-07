from math import sqrt


def prime_checker(x):  # this is to check if the number produced by the formula is prime
    # we only need to check up until the sqrt of the number, for every term under the square root there is one above it
    if x == 1:
        return False
    for y in range(2, int(sqrt(x) + 1)):
        if x % y == 0:
            return False
    return True


def formula(n, a, b):
    num = (n**2) + (a * n) + b
    return num


num_of_primes = 0
max_prime = 0
n = 0
while True:
    for a in range(1, 5):
        for b in range(1, 6):
            num = formula(n, a, b)
            if prime_checker(num) == False:
                break
            else:
                print(f"a={a}, b={b}, n={n}")
                num_of_primes += 1
        if num_of_primes > max_prime:
            max_prime = num_of_primes
        num_of_primes = 0
    n += 1

# a counter that keeps track of number of primes per iteration
# something that saves the coefficients
# double for loop