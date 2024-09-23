def findKthNumber(n,k):
    return int( sorted(str(i) for i in range(1,n+1))[k-1] )

print(findKthNumber(99,16))