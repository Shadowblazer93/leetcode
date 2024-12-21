def isPrefixOfWord(sentence,searchWord):
    sent = sentence.split()
    for k in range(len(sent)):
        if sent[k].startswith(searchWord): return k+1
    return -1

print(isPrefixOfWord("i love eating burger","burg"))