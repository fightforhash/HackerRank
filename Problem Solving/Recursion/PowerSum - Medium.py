def countways(current_num, target_sum, power):
    if current_num ** power > target_sum:
        return 0
    elif current_num ** power < target_sum:
        include_current = countways(current_num + 1, target_sum - current_num ** power, power)
        exclude_current = countways(current_num + 1, target_sum, power)
    
        return include_current + exclude_current
    else:
        return 1
    
def powerSum(X, N):
    return countways(1, X, N)

X = int(input().strip())
N = int(input().strip())
print(powerSum(X, N))
