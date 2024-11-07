def makeFancyString(s):
    res = s[0]
    c = 0

    for i in range(1,len(s)):
        if s[i]==s[i-1]: c += 1
        else: c = 0
        if c<2: res += s[i]
    
    return res

print(makeFancyString("leeetcode"))