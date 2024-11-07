def lengthAfterTransformations(s, t):
    alph = 'abcdefghijklmnopqrstuvwxyz'
    c = 0
    while c<t:
        L = []
        for i in s: L.append('ab' if i=='z' else alph[alph.index(i)+1])
        s = ''.join(L)
        c+=1
    return len(s)


print(lengthAfterTransformations("abcyy",2))
print(lengthAfterTransformations("v",7))