num = 2
num_list = []
while num < 1000000:
  temp_list = list(str(num))
  for i in range(len(temp_list)):
    temp_list[i] = int(temp_list[i]) ** 5
  if sum(temp_list) == num:
    num_list.append(num)
  num += 1

#print(temp_list)
print(sum(num_list))