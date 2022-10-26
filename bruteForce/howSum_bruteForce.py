"""
Write a function 'howSum(targetSum, numbers)' that takes in a targetSum and an array of numbers as arguments.
The function should return an array containing any combination of elements that add up to exactly the targetSum.
If there is no combination that adds up to the targetSum, then return null.
If there are multiple combinations possible, you may return any single one.
"""

def howSum(targetSum, numbers): # you can use the same numbers as much as you want to obtain the target sum
    if targetSum == 0: return []
    if targetSum < 0: return None

    for num in numbers:
        result = howSum(targetSum - num, numbers) # remainder = targetSum - num
        if result is not None:
            result.append(num) # O(m) time complexity appending to the list, maximum length of list is m
            return result

    return None

print(howSum(7, [2, 3])) # [3, 2, 2]
print(howSum(7, [5, 3, 4, 7])) # [4, 3]
print(howSum(7, [2, 4])) # None
print(howSum(8, [2, 3, 5])) # [2, 2, 2, 2]
# print(howSum(300, [7, 14])) # time exceeding

# m: target sum    n: length of numbers array
# time complexity O(n^m * m) 
# space complexity O(m)