def lexicalOrder(n): return [int(i) for i in sorted([str(j) for j in range(1,n+1)])]

    #s = [str(i) for i in range(1,n+1)]
    #s.sort()
    #ans = [int(i) for i in s]
    #return ans

print(lexicalOrder(13))