# 2. Take a array input, return an array such that ith element is product of every element of the list except itself
L = eval(input("Enter array : "))
m = 1
for i in L: m *= i
res = [int(m/k) for k in L]
print(res)