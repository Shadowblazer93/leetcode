tree = [[[7],1,[9]],3,[[8],2,[4]]]

def numOfNodes(t):
    if len(t)==1: return 1
    return numOfNodes(t[0]) + numOfNodes(t[2])+1

print(numOfNodes(tree))

def sumNodes(t):
    if len(t)==1: return t[0]
    return sumNodes(t[0])+sumNodes(t[2])+t[1]

def maxNode(t):
    if len(t)==1: return t[0]
    return max( maxNode(t[0]),1,maxNode(t[2]) )

print(sumNodes(tree))
print(maxNode(tree))