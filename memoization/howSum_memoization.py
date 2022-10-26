"""
Write a function 'howSum(targetSum, numbers)' that takes in a targetSum and an array of numbers as arguments.
The function should return an array containing any combination of elements that add up to exactly the targetSum.
If there is no combination that adds up to the targetSum, then return null.
"""

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
# time complexity O(n * m * m)
# space complexity O(m * m)