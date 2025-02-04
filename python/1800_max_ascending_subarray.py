def maxAscendingSum(nums):
        subs = []
        sub = [nums[0]]
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                sub.append(nums[i])
                continue
            else:
                subs.append(sub)
                sub = []
                sub.append(nums[i])
        else:
            if sub: subs.append(sub)
        
        # print(subs)
        return max([sum(i) for i in subs])