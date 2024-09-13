def xorQueries(arr,queries):
    xors = []
    for query in queries:
        start,stop = query[0],query[1]
        n=arr[start:stop+1]
        x = n[0]
        for i in n[1::]: x=x^i
        xors.append(x)
    return xors   

print(xorQueries([1,3,4,8],[[0,1],[1,2],[0,3],[3,3]]))