def addSpaces(s,spaces):
    #res = ''
    #for i in range(len(s)):
    #    if i in spaces: res+= ' '
    #    res+=s[i]
    #return res

    S = list(s)
    for i in spaces: S[i] = ' '+S[i]
    return ''.join(S)


print(addSpaces(s="LeetcodeHelpsMeLearn",spaces=[8,13,15]))