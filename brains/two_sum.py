def twoSum(nums, target):
    get_key = {}
    for i in range(len(nums)):
        another_num = target - nums[i]
        if another_num in get_key:
            return get_key[another_num], i
        if nums[i] not in get_key:
            get_key[nums[i]] = i


a = twoSum([2, 7, 14, 15], 17)
