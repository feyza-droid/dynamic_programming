"""
Write a function 'bestSum(targetSum, numbers)' that takes in a targetSum and an array of numbers as arguments.
The function should return an array containing the shortest combination of numbers that add up to exactly the targetSum.
If there is a tie for the shortest combination, you may return any one of the shortest.
"""

def bestSum(targetSum, numbers):
    table = [None for _ in range(targetSum + 1)]
    table[0] = []

    for i in range(len(table)):
        if table[i] is not None:
            for num in numbers:
                if i + num < len(table):
                    if (table[i + num] is None) or (len(table[i]) + 1 < len(table[i + num])): # only update when there is better, len(table[i]) + 1 is the length of table[i] + [num]
                        table[i + num] = table[i] + [num]

    #print(table)
    return table[targetSum]

print(bestSum(7, [2, 3])) # [2, 2, 3]
print(bestSum(7, [5, 3, 4, 7])) # [7]
print(bestSum(7, [2, 4])) # None
print(bestSum(8, [2, 3, 5])) # [3, 5]
print(bestSum(8, [1, 4, 5])) # [4, 4]
print(bestSum(100, [1, 2, 5, 25])) # [25, 25, 25, 25]
print(bestSum(100, [25, 1, 5, 2])) # [25, 25, 25, 25]
print(bestSum(300, [7, 14])) # None

# m = targetSum
# n = numbers.length
# time complexity O(m^2*n) # copying a list takes O(m) time
# space complexity O(m^2)