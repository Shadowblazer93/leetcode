def maxUniqueSplit(s):
    res = []
    lind = 0
    rind = lind+1

    while rind<=len(s):
        if s[lind:rind] in res: rind+=1
        else:
            res.append(s[lind:rind])
            lind = rind
            rind = lind+1
    
    return len(res)


print(maxUniqueSplit("wwwzfvedwfvhsww"))