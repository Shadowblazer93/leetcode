def construct2DArray(original, m, n): return [] if m*n != len(original) else [[original[i:i+n] for i in range(0,m*n,n)]]
print(construct2DArray([1,1,1,1],4,1))
