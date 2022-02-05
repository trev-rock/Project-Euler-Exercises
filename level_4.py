palindrome = []
for a in range(999, 99, -1):  # these two loops let us iterate from 999 down to 100 while keeping a at 999 while b goes down to 100, then 998 while b goes down, etc
    for b in range(999, 99, -1):
        product = str(a * b)  # make it a string so we can reverse it
        r_product = product[::-1]  # reverse the string
        if product == r_product:  # if they're the same then the nunber is a palindrome
            # make it an int again so we can find the max
            palindrome.append(int(product))
print(max(palindrome))
