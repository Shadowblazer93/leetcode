import os
def longestCommonPrefix(arr1,arr2):
    arr1 = set(map(lambda x: str(x),arr1))
    arr2 = set(map(lambda y: str(y),arr2))
    cartesian = set((i,j) for i in arr1 for j in arr2 if i[0]==j[0])
    ans = 0
    
    for i in cartesian:
        prefix = os.path.commonprefix(i)
        ans = max(ans,len(prefix))
    
    return ans

print(longestCommonPrefix([1,10,100],[1000]))