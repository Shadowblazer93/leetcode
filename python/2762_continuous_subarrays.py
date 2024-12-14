def continuousSubarrays(nums):
    n = len(nums)
    res = n
    
    for width in range(2,n+1):
        for i in range(0,n-width+1):
            sub = nums[i:i+width]
            if abs(max(sub)-min(sub))<=2:res+=1

    return res

print(continuousSubarrays([5,4,2,4]))
print(continuousSubarrays([1,2,3]))