def countFairPairs(nums,lower,upper):
    res = []
    n = len(nums)

    for i in range(n):
        for j in range(1+i,n):
            if i>=j: continue
            ijsum = nums[i] + nums[j]
            if ijsum < lower or ijsum > upper: continue
            res.append([i,j])
    
    return len(res)

print(countFairPairs([0,1,7,4,4,5],3,6))