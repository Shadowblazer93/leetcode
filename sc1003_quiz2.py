words = ['beachball','evaluate','arrive']
rating = {}

for w in words:rating[w] = len(set(i for i in w if w.count(i)==1))
res = [k for k in rating if rating[k]==max(rating.values())]
print(sorted(res)[0])

list1,list2 = [],[]
good = [i for i in list1 if str(i)==str(i)[::-1] or str(i).count('2')==1]
odd = [j for j in list2 if j%2==1]
res = 1
for k in good+odd: res *= k
print(res)