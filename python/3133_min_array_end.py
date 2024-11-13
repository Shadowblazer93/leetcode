def minEnd(n,x):
    res = x

    while n>1:
        res = (res+1)|x
        n -= 1

    return res

print(minEnd(2,7))