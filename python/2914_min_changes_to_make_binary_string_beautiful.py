def minChanges(s):
    res = 0
    for i in range(0,len(s),2):
        sub = set(s[i:i+2])
        if len(sub)==2: res += 1

    
    return res

print(minChanges("100100110100"))