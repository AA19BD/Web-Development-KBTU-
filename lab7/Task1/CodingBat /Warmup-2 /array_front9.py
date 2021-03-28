def array_front9(nums):
    c = len(nums)
    if c > 4:
        c = 4

    for i in range(c):
        if nums[i] == 9:
            return True
    return False
