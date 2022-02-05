nums = list(str(2**1000))
for i in range(len(nums)):
  nums[i] = int(nums[i])
print(sum(nums))