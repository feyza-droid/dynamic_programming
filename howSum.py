def howSum(targetSum, numbers, memo): # you can use the same numbers as much as you want to obtain the target sum
    if (targetSum in memo): return memo[targetSum] # if targetSum key exists in memo
    if targetSum == 0: return []
    if targetSum < 0: return None

    for num in numbers:
        result = howSum(targetSum - num, numbers, memo) # remainder = targetSum - num
        if result is not None: # if result is a list like [] or [num1, num2, ...]
            result.append(num) # O(m) time complexity appending to the list, maximum length of list is m
            memo[targetSum] = result
            return memo[targetSum]

    memo[targetSum] = None
    return memo[targetSum]

print(howSum(7, [2, 3], memo = {})) # [3, 2, 2]
print(howSum(7, [5, 3, 4, 7], memo = {})) # [4, 3]
print(howSum(7, [2, 4], memo = {})) # None
print(howSum(8, [2, 3, 5], memo = {})) # [2, 2, 2, 2]
print(howSum(300, [7, 14], memo = {})) # None

# m: target sum    n: length of numbers array
# time complexity O(n * m * m)  # NOTE: I didn't understand the time complexity of memoization (the n * m part)
# space complexity O(m * m) # # NOTE: I didn't understand the space complexity of memoization