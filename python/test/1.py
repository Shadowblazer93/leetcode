# 1. create a function to find the frequency of characters in a string and print nth frequency Character.
s = "I think maddy sir is the best teacher of all time he teaches us like a swaggist in the style of maddy sir"
k = s.split(" ")
s_freq = {i:k.count(i) for i in k}
print(s_freq)
n = int(input("n : "))
print([j for j in s_freq if s_freq[j]==n])