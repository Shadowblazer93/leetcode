def rotateString(s, goal):
        cases = []
        for i in range(len(s)):
            s = s[-1]+s[:len(s)-1]
            cases.append(s)
        print(cases)
        return goal in cases

print(rotateString("abcde",'cdeab'))