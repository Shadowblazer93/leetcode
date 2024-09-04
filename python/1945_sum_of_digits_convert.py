def getLucky(s,k):
    alphabet=[i for i in 'abcdefghijklmnopqrstuvwxyz']
    converted_num=''.join([str(alphabet.index(i)+1) for i in s])
    result = sum(int(i) for i in converted_num)
    for n in range(k-1): result = sum([int(i) for i in str(result)])
    return result

print(getLucky('leetcode',2))