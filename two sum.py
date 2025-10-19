# question 1 two sum
#brute force approach ie O(n**2)
nums = [2,7,11,15]
for i in range(len(nums)):
  for j in range(i+1,len(nums)):
    if nums[i]+nums[j]==target:
      print([i,j])
#optimal approach ie O(n)
h = {}
for i,num in enumerate(nums):
  h[num] = i
for i,num in enumerate(nums):
  desired = target-num
  if desired in h and h[desired]!=i:
    print([i,h[desired])
  
