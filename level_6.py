sum_of_squares = []
for i in range(1,101):
  sum_of_squares.append(i**2)
num_1 = sum(sum_of_squares)
square_of_sum = []
for i in range(1,101):
  square_of_sum.append(i)
num_2 = sum(square_of_sum)**2
print(num_2-num_1)