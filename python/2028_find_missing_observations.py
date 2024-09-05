def missingRolls(rolls, mean, n):
    sum_of_vars = mean*(len(rolls)+n)-sum(rolls)
    if sum_of_vars>6*n or sum_of_vars<n: return []
    vars = [sum_of_vars//n]*n
    for i in range(sum_of_vars%n):vars[i]+=1
    return vars


print(missingRolls([1,5,6],3,4))