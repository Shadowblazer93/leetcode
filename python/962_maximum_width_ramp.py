def maxWidthRamp_old(nums):
    res = 0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]<=nums[j]:
                res = max(res, j-i)
    return res

def maxWidthRamp(nums):
    n = len(nums)
    indices = [i for i in range(n)]
    indices.sort(key = lambda k: nums[k])
    minIndex = n
    maxWidth = 0

    for x in indices:
        maxWidth = max(maxWidth, x-minIndex)
        minIndex = min(minIndex, x)
    
    return maxWidth

print(maxWidthRamp([6,0,8,2,1,5]))
print(maxWidthRamp([9,8,1,0,1,9,4,0,4,1]))