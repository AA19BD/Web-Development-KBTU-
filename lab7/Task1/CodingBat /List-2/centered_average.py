def centered_average(nums):
  sum = 0;
  min1= nums[0];
  max1= nums[0];
  for i in nums:
    sum+=i
    min1=min(min1,i)
    max1=max(max1,i)
  return (sum - min1 - max1)//(len(nums) - 2);