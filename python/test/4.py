# 4. palindrome or not
s = input("Enter string : ")

res = True
for i in range(0,len(s)//2):
    if s[i] != s[len(s)-i-1]: res = False

print(res)