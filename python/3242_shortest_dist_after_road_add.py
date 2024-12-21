def shortestDistanceAfterQueries(n,queries):
    paths = {i:[i+1] for i in range(0,n)}
    res = []
    for s,e in queries:
        paths[s].append(e)
        turns = city = 0
        while city < n-1:
            city = max(paths[city])
            turns += 1
        res.append(turns)

    return res

#print(shortestDistanceAfterQueries(5,[[2,4],[0,2],[0,4]]))
print(shortestDistanceAfterQueries(6,[[1,4],[0,2]]))