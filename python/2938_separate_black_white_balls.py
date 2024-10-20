def minimumSteps(s:str):
    swaps = b =0
    for i in s:
        if i == '0':swaps += b
        else:b += 1
    return swaps

print(minimumSteps("11000111"))