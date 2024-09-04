def twoSum(nums, target):
    indexes,found = [], ''
    for i in range(len(nums)):
        if found:break
        for j in range(1,len(nums)):
            if found:break
            if nums[i]+nums[j] == target and i!=j:
                if found:break
                indexes += i,j
                found = True
    return indexes

print(twoSum([0,4,3,0],0))