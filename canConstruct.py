"""
Write a function 'canConstruct(target, wordBank)' that accepts a target string and an array of strings.
The function should return a boolean indicating whether or not the 'target' can be constructed by concatenating elements of the 'wordBank' array.
You may reuse elements of 'wordBank' as many times as needed.
"""

def canConstruct(target, wordBank, memo):
    if (target in memo): return memo[target]
    if target == '': return True

    for word in wordBank:
        if target.startswith(word):
            suffix = target[len(word):]
            if canConstruct(suffix, wordBank, memo) == True:
                memo[target] = True
                return memo[target]

    memo[target] = False
    return memo[target]

print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"], memo = {})) # True
print(canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"], memo = {})) # False
print(canConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"], memo = {})) # True
print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"], memo = {})) # False

# m: target    n: length of word bank array
# time complexity O(n * m^2) 
# space complexity O(m * m)