seqs = []
for n in range(1, 1000000):
    count = 1
    # put in the starting value of n first as a key with no value then update its count at the end
    while True:
        if n == 1:
            seqs.append(count)
            break
        if n % 2 == 0:
            n /= 2
            count += 1
        else:
            n = 3*n + 1
            count += 1


print(f"{seqs.index(max(seqs))}, {max(seqs)}")
