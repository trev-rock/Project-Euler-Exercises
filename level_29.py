sett = set()
# we need 2 to be raised from the 2 power to 100, then 3 raised to the same, and so on
for a in range(2, 101):
    for b in range(2, 101):
        sett.add(a**b)

print(len(sett))
