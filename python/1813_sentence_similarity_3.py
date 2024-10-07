def areSentencesSimilar(sentence1,sentence2):
    s1,s2 = sentence1.split(),sentence2.split()
    while s1 and s2 and s1[0]==s2[0]: s1.pop(0),s2.pop(0)
    while s1 and s2 and s1[-1]==s2[-1]: s1.pop(-1),s2.pop(-1)
    return not(s1 and s2)


    


print(areSentencesSimilar("My name is Haley","My Haley"))
print(areSentencesSimilar("of","A lot of words"))
print(areSentencesSimilar("Eating right now","Eating"))
print(areSentencesSimilar("Luky","Lucccky"))