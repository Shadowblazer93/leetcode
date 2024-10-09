def minAddToMakeValid(s):
    s = s.replace("()","")
    return len(s)

print(minAddToMakeValid("())"))
print(minAddToMakeValid("((("))