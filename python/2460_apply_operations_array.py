def applyOperations(nums):
    new_nums = []
    zeroes = 0
    n = len(nums)
    dupl = False

    for i in range(n-1):
        if dupl==True:
            dupl = False
            zeroes+=1
            continue

        if nums[i]==0: zeroes+=1

        elif nums[i]==nums[i+1]:
            new_nums.append(nums[i]*2)
            dupl = True

        else: new_nums.append(nums[i])
    
    if nums[-1]!=nums[-2]: new_nums.append(nums[-1])
    else: new_nums.append(0)

    new_nums.extend([0]*zeroes)
    return new_nums