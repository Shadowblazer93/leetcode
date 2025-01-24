def countPrefixSuffixPairs(words):
    n = len(words)
    res = 0

    for i in range(n):
        for j in range(i+1,n):
            if i==j: continue
            a,b = words[i], words[j]
            if b.startswith(a) and b.endswith(a): res += 1
    
    return res

print(countPrefixSuffixPairs(["a","aba","ababa","aa"]))