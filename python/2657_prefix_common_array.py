def findThePrefixCommonArray(A, B):
    n = len(A)
    res = []

    for i in range(n):
        cmn = 0
        suba, subb = A[:i+1], B[:i+1]
        for j in suba:
            if j in subb: cmn += 1
        res.append(cmn)
    
    return res