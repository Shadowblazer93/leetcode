def largestNumber(nums):
    res = [str(num) for num in nums]
    res.sort(key=lambda x:x*10, reverse=True)
    return ('0' if res[0]=='0' else ''.join(res))

print(largestNumber([0,0]))