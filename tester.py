from collections import deque
def deque_to_num(x):
    x = ''.join(x)
    print(x)
    x = int(x)
    print(x)
    return x

def num_to_deque(x):
    return deque(str(x))

num = deque("3797")

while True: 
    if len(num) == 0: 
        print('len is 0')
        break

    num.pop() 
    print('num has been popped')

    num = deque_to_num(num)
    print(f'it is now number: {num}')

    if isinstance(num, int): 
        print('yes')
        
    else:
        print('uh oh')
        break

    num = num_to_deque(num)
    print(f'it is a deque again: {num}')



