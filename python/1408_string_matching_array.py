def stringMatching(words):
    n = len(words)
    res = []

    for i in range(n):
        for j in range(n):
            if i==j: continue
            if words[i] in words[j] and words[i] not in res:
                res.append(words[i])

    return res