from collections import deque

def isValid(self,s):
    stk = deque()
    brackets = ['(','[','{',')',']','}']

    for b in s:
        if not stk: stk.append(b)
        else:
            ind = brackets.index(b)
            pair = brackets[(ind+3)%6]

            if stk[-1]==pair: stk.pop()
            else: stk.append(b)