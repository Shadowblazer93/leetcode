def chalkReplacer(chalk, k):
    x=sum(chalk)
    k=k%x
    total=0
    i=0
    while total<=k:
        total+=chalk[i]
        i+=1
    return i-1