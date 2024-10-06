def checkInclusion(s1,s2):
    c1 = {i:s1.count(i) for i in s1}
    for k in range(len(s2)):
        s2_sub = s2[k:k+len(s1)]
        print(s2_sub)
        c2_sub = {j:s2_sub.count(j) for j in s2_sub}
        if c1 == c2_sub: return True
    
    return False

print(checkInclusion("ab","eidbaooo"))
print('-'*50)
print(checkInclusion("ab","eidboaoo"))