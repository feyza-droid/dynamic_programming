"""
Write a function 'canSum(targetSum, numbers)' that takes in a targetSum and an array of numbers as arguments.
The function should return a boolean indicating whether or not it is possible to generate the targetSum using numbers from the array.
"""

def canSum(targetSum, numbers):
    table = [False for _ in range(targetSum + 1)]
    table[0] = True

    # NOTE: if table[targetSum] becomes True, you can do early stopping, since finding one possible solution is enough
    for i in range(len(table)):
        if table[i]: # if it is True
            for num in numbers:
                if i+num < len(table): table[i + num] = True

    return table[targetSum]

print(canSum(7, [2, 3])) # True
print(canSum(7, [5, 3, 4, 7])) # True
print(canSum(7, [2, 4])) # False
print(canSum(8, [2, 3, 5])) # True
print(canSum(300, [7, 14])) # False

# m = targetSum
# n = numbers.length
# time complexity O(m*n)
# space complexity O(m)