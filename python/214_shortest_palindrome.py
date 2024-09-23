def shortestPalindrome(s):
    r = s[::-1]
    for i in range(len(r)):
        if r[i:]==s[:len(r)-i]: return r[:i]+s
    return r+s

print(shortestPalindrome("amimadam"))