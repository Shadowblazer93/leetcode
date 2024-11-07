def isCircularSentence(s):
    if s[0]!=s[-1]: return False
    S = s.split()
    
    for i in range(1,len(S)):
        if S[i][0]!=S[i-1][-1]: return False

    return True

print(isCircularSentence("leetcode exercises sound delightful"))