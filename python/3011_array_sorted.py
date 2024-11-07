def canSortArray(nums):
    seg = []
    segment = [nums[0]]

    for i in range(1,len(nums)):
        sb = bin(nums[i]).count('1')
        sb_prev = bin(nums[i-1]).count('1')

        if sb == sb_prev: segment.append(nums[i])
        else:
            seg.append(segment)
            segment = [nums[i]]
    seg.append(segment)

    for s in range(1,len(seg)):
        if min(seg[s]) < max(seg[s-1]): return False
    
    return True

print(canSortArray([3,16,8,4,2]))