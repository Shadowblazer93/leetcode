def removeDigit(number,digit):
    number = str(number)
    cases = []
    for i in range(len(number)):
        if number[i]==str(digit): cases.append(int(number[0:i]+number[i+1:]))
    return str(max(cases))

print(removeDigit(123,3))