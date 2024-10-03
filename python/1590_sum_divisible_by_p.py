def minSubarray(nums,p):
    res = float('inf')
    subarray_sum = sum(nums)%p

    for i in range(len(nums)):
        for j in range(i+1,len(nums)+1):
            subarray = nums[i:j]
            if sum(subarray)%p==subarray_sum:
                print(subarray)
                res = min( res, len(subarray) )

    if subarray_sum==0: return 0
    elif res==float('inf') or res==len(nums): return -1
    else: return res

#print(minSubarray([1,2,3],7))
print(minSubarray([26,19,11,14,18,4,7,1,30,23,19,8,10,6,26,3],26))