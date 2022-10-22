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
# space complexity O(m) # NOTE: I didn't understand the space complexity of brute force solution (is it the stack?)