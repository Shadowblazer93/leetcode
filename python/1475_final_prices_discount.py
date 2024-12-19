def finalPrices(prices):
    #res = []
    #for i,j in enumerate(prices[:-1]):
    #    sub_items = [k for k in prices[i+1:] if k<=j]
    #    if sub_items: j -= sub_items[0]
    #    res.append(j)
    #res.append(prices[-1])
    #return res

    res = []
    n = len(prices)

    for i in range(n):
        k = i+1
        j = 0
        while k<n:
            if prices[k] <= prices[i] :
                j = prices[k]
                break
            k += 1
        res.append(prices[i]-j)
    return res