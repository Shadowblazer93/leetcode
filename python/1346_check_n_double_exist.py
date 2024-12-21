def checkIfExist(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]==2*arr[j] or 2*arr[i]==arr[j]: return True
    return False

print(checkIfExist([7,1,14,11]))