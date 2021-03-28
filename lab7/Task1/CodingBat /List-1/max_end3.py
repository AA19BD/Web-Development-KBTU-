def max_end3(nums):
    max = -1e5
    list1 = []
    if nums[0] < nums[2]:
        list1.append(nums[2])
    elif nums[0] > nums[2]:
        list1.append(nums[0])
    else:
        list1.append(nums[0])

    return list1 * 3
