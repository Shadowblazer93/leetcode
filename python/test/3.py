# 3. Given a list , print two list such that array1 contains range of the list [min,max] array2 contains all missing elements from the range in Input list
L = [4,5,2,8,9,10]
a,b = min(L),max(L)
array1 = [a,b]
array2 = [i for i in range(a,b) if i not in L]
print(array1)
print(array2)