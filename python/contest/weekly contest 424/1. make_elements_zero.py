def countValidSelections(nums):
    res = 0
    dir = 0 # 0 : left, 1 : right

    for ind,z in enumerate(nums):
        if z != 0: continue
        N = list(nums)
        cur = ind
        print(ind)

        while True:
            cur += (1 if dir == 1 else -1)
            if cur not in range(0,len(nums)): break

            if N[cur] == 0: cur += (1 if dir == 1 else -1)
            elif N[cur] > 0:
                N[cur] -= 1
                dir ^= 1
            
            print(N)
            if N == [0]*len(nums):
                res += 1
                break

    return res

print(countValidSelections([1,0,2,0,3]))