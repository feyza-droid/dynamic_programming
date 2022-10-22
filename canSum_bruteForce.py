def canSum(targetSum, numbers): # you can use the same numbers as much as you want to obtain the target sum
    if targetSum == 0: return True
    if targetSum < 0: return False

    for num in numbers:
        if canSum(targetSum - num, numbers) == True: # remainder = targetSum - num
            return True

    return False

print(canSum(7, [2, 3])) # True
print(canSum(7, [5, 3, 4, 7])) # True
print(canSum(7, [2, 4])) # False
print(canSum(8, [2, 3, 5])) # True
# print(canSum(300, [7, 14])) # time exceeding

# m: target sum    n: length of numbers array
# time complexity O(n^m) 
# space complexity O(n) # NOTE: I didn't understand the space complexity of brute force solution