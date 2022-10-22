"""
Write a function 'bestSum(targetSum, numbers)' that takes in a targetSum and an array of numbers as arguments.
The function should return an array containing the shortest combination of numbers that add up to exactly the targetSum.
If there is a tie for the shortest combination, you may return any one of the shortest.
"""

def bestSum(targetSum, numbers, memo):
    if targetSum in memo: return memo[targetSum]
    if targetSum == 0: return []
    if targetSum < 0: return None

    shortestCombination = None

    for num in numbers:
        combination = bestSum(targetSum - num, numbers, memo)
        if combination is not None: # if combination is a list like [] or [num1, num2, ...]
            remainderCombination = combination.copy() # if we directly append the num to the combination without copying combination object, we would be using the same
            remainderCombination.append(num) # O(m) time complexity appending to the list, maximum length of list is m
            if (shortestCombination is None) or (len(remainderCombination) < len(shortestCombination)): # at first update shortestCombination is None then only updated when there is shorter
                shortestCombination = remainderCombination

    memo[targetSum] = shortestCombination
    return memo[targetSum] # returns shortestCombination

print(bestSum(7, [5, 3, 4, 7], memo = {})) # [7]
print(bestSum(8, [2, 3, 5], memo = {})) # [3, 5]
print(bestSum(8, [1, 4, 5], memo = {})) # [4, 4]
print(bestSum(100, [1, 2, 5, 25], memo = {})) # [25, 25, 25, 25]

# m: target sum    n: length of numbers array
# time complexity O(m * n * m) 
# space complexity O(m * m)