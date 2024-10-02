def arrayRankTransform(arr):
    ranks = {i:0 for i in arr}
    arr_sort = sorted(arr)
    rank = 1

    for j,k in enumerate(arr_sort):
        ranks[k] = rank
        if j!=len(arr_sort)-1 and arr_sort[j] != arr_sort[j+1]:
            rank += 1
    
    return [ranks[r] for r in arr]
        
def arrayRankTransform2(arr):
    ranks = {j:i+1 for i,j in enumerate(sorted(set(arr)))}
    return [ranks[i] for i in arr]

print(arrayRankTransform([40,10,20,30]))
print(arrayRankTransform([100,100,100]))