def findKthBit(n,k):
    c = 0
    seq = '0'
    while c<n:
        seq_inv = ''
        for i in seq: seq_inv += ('1' if i=='0' else '0')
        seq = seq + '1' + seq_inv[::-1]
        c += 1
    return seq[k-1]
    

print(findKthBit(3,1))