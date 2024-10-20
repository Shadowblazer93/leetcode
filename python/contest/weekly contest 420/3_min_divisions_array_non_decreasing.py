def minOperations(nums):
    div = 0
    for i in range(len(nums)-1,0,-1):
        while nums[i-1] > nums[i]:
            max_divisor = 1
            for k in range(2, int(nums[i - 1]**0.5+1)):
                if nums[i-1] % k==0: max_divisor = max(max_divisor, k, nums[i - 1] // k)
            
            if max_divisor == 1: return -1
            nums[i-1] //= max_divisor
            div += 1

    if nums!=sorted(nums): return -1
    return div


#print(minOperations([9,27,81,27,3]))
print(minOperations([9,2]))