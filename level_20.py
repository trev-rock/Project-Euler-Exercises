total = 1
for x in range(100,1,-1):
  total *= x
total = list(str(total))
for y in range(len(total)):
  total[y] = int(total[y])
print(sum(total))