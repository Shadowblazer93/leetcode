def uncommonFromSentences(s1,s2):
    s = s1.split()+s2.split()
    return [k for k in s if s.count(k)==1]
print(uncommonFromSentences("apple apple","banana"))