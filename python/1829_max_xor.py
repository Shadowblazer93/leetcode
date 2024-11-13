def getMaximumXor(nums,maximumBit):
    #t = 2**maximumBit-1
    #xor = 0
    #res = []
    #for i in range(len(nums),0,-1):
    #    sub = nums[0:i]
    #    xor = 0
    #    for j in sub: xor = xor^j
    #    for k in range(t+1):
    #        if xor^k == t:
    #            res.append(k)
    #            continue
    #return res

    t = 2**maximumBit-1
    xor, res = 0, []
    for i in nums:
        xor = xor^i
        res.append(t-xor)
    return res[::-1]

print(getMaximumXor([0,1,1,3],2))