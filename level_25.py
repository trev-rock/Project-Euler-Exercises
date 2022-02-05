a = 0
b = 1
char = []
counter = 1
while len(char) != 1000:
  temp_a = a 
  a = b 
  b = temp_a + b 
  char = list(str(b))
  counter += 1
print(counter)