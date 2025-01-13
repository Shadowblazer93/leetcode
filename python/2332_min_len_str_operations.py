def minimumLength(s):
    res = len(s)
    for i in set(s):
        k = s.count(i)
        if k>=3:
            k -= 1 if k%2==1 else 2
            res -= k
    return res