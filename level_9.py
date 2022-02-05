nums = []
answer = []
for a in range(1,332):
  for b in range(a+1,501):
    for c in range(1,501):
      if a**2 + b**2 == c**2 and a+b+c == 1000:
        print(a*b*c)