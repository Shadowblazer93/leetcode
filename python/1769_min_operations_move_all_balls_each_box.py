def minOperations(boxes):
    n = len(boxes)
    res = []

    for box in range(n):
        path = 0
        for ball in range(n):
            # if box==ball or boxes[ball]=='0': continue
            if boxes[ball]=='1': path += abs(ball-box)
        res.append(path)
    
    return res

print(minOperations("110"))