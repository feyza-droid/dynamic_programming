"""
Write a function 'countConstruct(target, wordBank)' that accepts a target string and an array of strings.
The function should return the number of ways that the 'target' can be constructed by concatenating elements of the 'wordBank' array.
You may reuse elements of 'wordBank' as many times as needed.
"""

def countConstruct(target, wordBank, memo):
    if target in memo: return memo[target]
    if target == '': return 1

    totalCount = 0
    for word in wordBank:
        if target.startswith(word):
            suffix = target[len(word):]
            count = countConstruct(suffix, wordBank, memo)
            totalCount += count

    memo[target] = totalCount
    return memo[target]

print(countConstruct("purple", ["purp", "p", "ur", "le", "purpl"], memo = {})) # 2
print(countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"], memo = {})) # 1
print(countConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"], memo = {})) # 0
print(countConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"], memo = {})) # 4
print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"], memo = {})) # 0

# m: target    n: length of word bank array
# time complexity O(n * m^2) 
# space complexity O(m * m)