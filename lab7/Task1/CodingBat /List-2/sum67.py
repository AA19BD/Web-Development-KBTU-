def sum67(nums):
  sum=0
  check=False
  for i in nums:
    if i==6:
      check=True
      continue
    if i==7 and check==True:
      check=False
      continue
    if check==False:
      sum+=i
  return sum