import math
def maxKelements(nums,k):
    c = res = 0
    while c<k:
        m = max(sorted(nums))
        res += m
        m_ind = nums.index(m)
        nums[m_ind] = math.ceil(m/3)
        c+=1
    return res

print(maxKelements([1,10,3,3,3],3))