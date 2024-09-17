def findTheLongestSubstring(s):
    vowels = ['a','e','i','o','u']
    res = [0]
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            substr = s[i:j]
            if [substr.count(k) for k in vowels if substr.count(k)%2]: continue
            else: res.append(len(substr))
    return max(res)

print(findTheLongestSubstring("a"))