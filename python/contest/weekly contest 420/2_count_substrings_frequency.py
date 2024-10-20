def numberOfSubstrings(s, k):
    #res = 0
    #for i in range(len(s)):
    #    for j in range(i+1,len(s)+1):
    #        substr = s[i:j]
    #        count = {s:substr.count(s) for s in substr if substr.count(s)>=k}
    #        if count: res+=1
    #return res
    res = 0
    l = 0
    char = {}

    for r in range(len(s)):
        char[s[r]] = char.get(s[r],0)+1
        while any(c>=k for c in char.values()):
            res += len(s)-r
            char[s[l]] -= 1
            if char[s[l]] == 0: del char[s[l]]
            l += 1
    return res

print(numberOfSubstrings("abacb",2))
print(numberOfSubstrings("abcde",1))