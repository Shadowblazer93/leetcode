def shiftingLetters(s, shifts):
    alph = 'abcdefghijklmnopqrstuvwxyz'
    ls = list(s)

    for st,ed,dir in shifts:
        for i in range(st,ed+1):
            v = alph.index(ls[i])
            v += (-1 if dir==0 else 1)
            ls[i] = alph[v%26]
    
    return ''.join(ls)

print(shiftingLetters("abc",[[0,1,0],[1,2,1],[0,2,1]]))