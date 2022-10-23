"""
Write a function 'countConstruct(target, wordBank)' that accepts a target string and an array of strings.
The function should return the number of ways that the 'target' can be constructed by concatenating elements of the 'wordBank' array.
You may reuse elements of 'wordBank' as many times as needed.
"""

def countConstruct(target, wordBank):
    if target == '': return 1

    totalCount = 0
    for word in wordBank:
        if target.startswith(word):
            suffix = target[len(word):]
            count = countConstruct(suffix, wordBank)
            totalCount += count

    return totalCount

print(countConstruct("purple", ["purp", "p", "ur", "le", "purpl"])) # 2
print(countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"])) # 1
print(countConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])) # 0
print(countConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])) # 4
# print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"])) # 0 # time exceeding

# m: target    n: length of word bank array
# time complexity O(n^m * m) 
# space complexity O(m * m)