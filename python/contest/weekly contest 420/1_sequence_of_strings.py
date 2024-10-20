def stringSequence(target):
    alph = 'abcdefghijklmnopqrstuvwxyz'
    str = ['a']
    ind = 0
    while ind<len(target):
        if str[-1][-1]==target[ind]:
            str.append(str[-1]+'a')
            ind+=1
        else:
            rstr = str[-1][-1]
            rstr_ind = alph.index(rstr)
            str.append(str[-1][:-1]+alph[rstr_ind+1])
    
    return str[:-1]
print(stringSequence('abc'))