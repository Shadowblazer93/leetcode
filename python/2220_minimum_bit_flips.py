def minBitFlips(start, goal):return bin(start^goal).count('1')
print(minBitFlips(10,7))