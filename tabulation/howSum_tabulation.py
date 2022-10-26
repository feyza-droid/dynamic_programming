"""
Write a function 'howSum(targetSum, numbers)' that takes in a targetSum and an array of numbers as arguments.
The function should return an array containing any combination of elements that add up to exactly the targetSum.
If there is no combination that adds up to the targetSum, then return null.
If there are multiple combinations possible, you may return any single one.
"""

def howSum(targetSum, numbers):
    table = [None for _ in range(targetSum+1)]
    table[0] = []

    for i in range(len(table)):
        if table[i] is not None:
            for num in numbers:
                if i + num < len(table):
                    table[i + num] = table[i] + [num] # create new list by appending the num value # copying a list takes O(m) time
                    #if i + num == targetSum and table[targetSum]:
                    #    return table[targetSum] # early stopping, found one solution

    return table[targetSum]


print(howSum(7, [2, 3])) # with early stopping [2, 2, 3], without early stopping [3, 2, 2]
print(howSum(7, [5, 3, 4, 7])) # with early stopping [7], without early stopping [4, 3]
print(howSum(7, [2, 4])) # None
print(howSum(8, [2, 3, 5])) # with early stopping [3, 5], without early stopping [2, 2, 2, 2]
print(howSum(300, [7, 14])) # None

# m = targetSum
# n = numbers.length
# time complexity O(m^2*n) # copying a list takes O(m) time