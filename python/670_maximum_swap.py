def maximumSwap(num):
    s = str(num)
    ss = sorted(s,reverse=True)
    res = []
    c = 0
    
    for i in s:
        if i==ss[0]:
            res += ss[0]
            ss.pop(0)
            c+=1
        else:
            res += ss[0]
            res += s[len(res):]
            l_ind = s.index(ss[0])
            res[l_ind] = s[c]
            break

    return int(''.join(res))


print(maximumSwap(2736))
print(maximumSwap(9973))