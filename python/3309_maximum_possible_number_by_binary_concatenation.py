import itertools
def maxGoodNumber(nums):
    nums = [bin(i)[2:] for i in nums]
    return max([int(''.join(k),2) for k in itertools.permutations(nums)])

print(maxGoodNumber([1,2,3]))
print(maxGoodNumber([2,8,16]))