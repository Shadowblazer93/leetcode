def maximumSubarraySum(nums,k):
    res = 0
    n = len(nums)

    for i in range(n-k+1):
        sub = nums[i:i+k]
        if len(set(sub))!=k: continue
        res = max(res,sum(sub))

    return res

print(maximumSubarraySum(nums=[1,5,4,2,9,9,9],k=3))