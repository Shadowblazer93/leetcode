def firstCompleteIndex(arr, mat):
    m = len(mat) #rows
    n = len(mat[0]) #columns
    mfreq = [0]*m*n
    mflat = [j for i in mat for j in i]
    
    for i in range(len(arr)):
        k = mflat.index(arr[i])
        mfreq[k] |= 1

        for r in range(0,m*n,n):
            row = mfreq[r:r+n]
            if all(row): return i
        
        for c in range(0,n):
            col = mfreq[c:(c+n)*m:n]
            if all(col): return i