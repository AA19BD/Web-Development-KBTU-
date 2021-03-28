def has22(nums):
  if len(nums)==2:
    if nums[0]==nums[1]==2:
      return True
  for i in range(1,len(nums)-1):
    if nums[i-1]==nums[i]==2 or nums[i]==nums[i+1]==2:
      return True
  return False
