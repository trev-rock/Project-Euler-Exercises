def decimal_to_binary(d):
  total = [] 
  while d > 0:
    dig = d % 2 
    total.append(dig) 
    d = d // 2
  total.reverse() 
  binary_string = ''
  for i in total:
    binary_string += str(i)
  return(binary_string)


nums = []
for i in range(1,1000000):
  if str(i) == str(i)[::-1] and str(decimal_to_binary(i)) == str(decimal_to_binary(i))[::-1] :
      nums.append(i)

print(sum(nums))