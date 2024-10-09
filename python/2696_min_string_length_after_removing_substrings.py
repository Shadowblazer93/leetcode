def minLength(s):
    while "AB" in s or "CD" in s: s = s.replace("AB" if "AB" in s else "CD",'')
    return len(s)

def minLength2(s:str):
    while True:
        print(s)
        ab = s.find("AB")
        cd = s.find("CD")
        if ab==-1 and cd==-1: break

        if ab!=-1:
            s = s[:ab] + s[ab+2:]
            continue

        if cd!=-1:
            s = s[:cd] + s[cd+2:]
            continue
    
    return len(s)

print(minLength("ABFCACDB"))
print(minLength("CCCCDDDD"))