def maximumBeauty(items,queries):
    res = []
    items.sort()
    print(items)

    for q in queries:
        items_budget = [k for k in items if k[0]<=q]
        beauty = max(b[1] for b in items_budget)
        res.append(beauty)
    
    return res
    # return [max(b[1] for b in [k for k in items if k[0]<=q]) for q in queries]


print(maximumBeauty([[1,2],[3,2],[2,4],[5,6],[3,5]],[1,2,3,4,5,6]))