def sumPrefixScores(words):
    res = []
    for word in words:
        c = 0
        for i in range(1,len(word)+1):
            prefix = word[:i]
            c += len([k for k in words if k.startswith(prefix)])
        res.append(c)
    return res

print(sumPrefixScores(['abc','ab','bc','b']))