def countConsistentStrings(allowed, words):
    "modifies input, low readability, inefficient, high runtime"
    #for alphabet in allowed: words=[i.replace(alphabet,'') for i in words]
    #return len([i for i in words if not i])

    count=0
    for word in words:
        for letter in word:
            if letter not in allowed:
                count+=1
                break
    return len(words)-count

print(countConsistentStrings('ab',["ad","bd","aaab","baa","badab"]))