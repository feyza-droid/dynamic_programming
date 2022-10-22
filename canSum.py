"""
Dynamic Programming - Learn to Solve Algorithmic Problems & Coding Challenges
https://www.youtube.com/watch?v=oBt53YbR9Kk&t=4216s&ab_channel=freeCodeCamp.org
"""

def canSum(targetSum, numbers, memo): # you can use the same numbers as much as you want to obtain the target sum
    if (targetSum in memo): return memo[targetSum] # if targetSum key exists in memo
    if targetSum == 0: return True
    if targetSum < 0: return False

    for num in numbers:
        if canSum(targetSum - num, numbers, memo): # if it is True # remainder = targetSum - num
            memo[targetSum] = True
            return memo[targetSum]

    memo[targetSum] = False
    return memo[targetSum]

# dict objects are call by reference, so they are changed inside of a function
print(canSum(7, [2, 3], memo = {})) # True
print(canSum(7, [5, 3, 4, 7], memo = {})) # True
print(canSum(7, [2, 4], memo= {})) # False
print(canSum(8, [2, 3, 5], memo= {})) # True
print(canSum(300, [7, 14], memo= {})) # False

# m: target sum    n: length of numbers array
# time complexity O(m * n) # NOTE: I didn't understand the time complexity of memoization
# space complexity O(m) # NOTE: I didn't understand the space complexity of memoization