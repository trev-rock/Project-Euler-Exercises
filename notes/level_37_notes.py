from tools import prime_tester # we want to import this so we don't have to keep redefining it
from collections import deque # we will be using a deque to truncate our number

def deque_to_num(x):
    return int(''.join(x))

def truncate_right(num): # in this method we want to continuously remove numbers from the right
    while True: # we want to keep trying this until we either know it satisfies the condition entirely or exit early if it doesn't
        if len(num) == 0: # we have this check early because otherwise the program will cause an error when there are no numbers left for it to check 
            return True
        num.pop() # removes the rightmost number
        if prime_tester(deque_to_num(num)): # after we remove a number from the deque we want to convert it into a string then an integer to use it as an actual number for prime_tester, the advantage to putting the conversion here is that we are only temporarily converting it just for this check, so we don't have to convert it back to a deque 
            continue # if the truncated number is prime then restart and keep going
        else:
            return False # exit if it fails once

num = deque("3797")

if truncate_right(num):
    print('success')

"""counter = 1
while True:
    if prime_tester(counter):
        print(f"{counter} is prime")
        counter = deque(str(counter))
    else:
        counter = deque(str(counter))
    print(counter)
    counter = int(''.join(counter))
    print(counter)

    counter += 1   """




