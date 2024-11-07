import math

def maxScore(nums):
    fs = math.lcm(*nums)*math.gcd(*nums)
    if len(nums)==0: return 0
    elif len(nums)==1: return nums[0]**2
    for i in range(len(nums)):
        sub = nums[:i]+nums[i+1:]
        score = math.lcm(*sub)*math.gcd(*sub)
        fs = max(fs, score)
    return fs

#print(maxScore([2,4,8,16]))
print(maxScore([6,14,20]))