# 1. create a function to find the frequency of characters in a string and print nth frequency Character.
s = "I think maddy sir is the best teacher of all time he teaches us like a swaggist in the style of maddy sir"
k = s.split(" ")
s_freq = {i:k.count(i) for i in k}
print(s_freq)
n = int(input("n : "))
print([j for j in s_freq if s_freq[j]==n])

# 2. Take a array input, return an array such that ith element is product of every element of the list except itself
L = eval(input("Enter array : "))
m = 1
for i in L: m *= i
res = [int(m/k) for k in L]
print(res)

# 3. Given a list , print two list such that array1 contains range of the list [min,max] array2 contains all missing elements from the range in Input list