def isZeroArray(nums, queries):
    for s,e in queries:
        for k in range(s,e+1):
            if nums[k] == 0: continue
            nums[k] -= 1
            print(s,e,nums)
    
    return all(x==0 for x in nums)

#print(isZeroArray([1,0,1],[[0,2]]))
print(isZeroArray([4,6],[[0,0],[0,1],[1,1],[0,0],[1,1],[1,1],[0,0],[1,1],[1,1],[1,1],[0,0],[1,1],[0,1],[0,0],[1,1]]))