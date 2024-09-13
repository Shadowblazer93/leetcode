# code doesn't work, program has linked lists

def addTwoNumbers(l1,l2):
    l1 = int(''.join([str(i) for i in l1[::-1]]))
    l2 = int(''.join([str(i) for i in l2[::-1]]))
    return [int(i) for i in str(l1+l2)[::-1]]

print(addTwoNumbers([2],[5,6,4]))