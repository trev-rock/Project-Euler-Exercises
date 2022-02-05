primes = []
num = 2
while len(primes) != 10001:
  con = False
  for i in range(2,num+1):
    if num == i:
      con = False
      break
    if num % i == 0:
      con = True
      break
  if con == False:
    primes.append(num)
  num += 1
print(primes[-1])