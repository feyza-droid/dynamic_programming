"""
Write a function 'bestSum(targetSum, numbers)' that takes in a targetSum and an array of numbers as arguments.
The function should return an array containing the shortest combination of numbers that add up to exactly the targetSum.
If there is a tie for the shortest combination, you may return any one of the shortest.
"""

def bestSum(targetSum, numbers):
    if targetSum == 0: return []
    if targetSum < 0: return None

    shortestCombination = None

    for num in numbers:
        combination = bestSum(targetSum - num, numbers)
        if combination is not None: # if combination is a list like [] or [num1, num2, ...]
            combination.append(num) # O(m) time complexity appending to the list, maximum length of list is m
            if (shortestCombination is None) or (len(combination) < len(shortestCombination)): # at first update shortestCombination is None then only updated when there is shorter
                shortestCombination = combination

    return shortestCombination

print(bestSum(7, [5, 3, 4, 7])) # [7]
print(bestSum(8, [2, 3, 5])) # [3, 5]
print(bestSum(8, [1, 4, 5])) # [4, 4]
# print(bestSum(100, [1, 2, 5, 25])) # [25, 25, 25, 25] #  # time exceeding

# m: target sum    n: length of numbers array
# time complexity O(n^m * m) 
# space complexity O(m * m)