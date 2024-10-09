def minSwaps(s:str):
    c = 0
    for i in s:
        if i=='[': c+=1
        elif c>0 : c-=1
    return (c+1)//2


print(minSwaps("][]["))
print('-'*20)
print(minSwaps("]]][[["))