"""
Write a function 'canConstruct(target, wordBank)' that accepts a target string and an array of strings.
The function should return a boolean indicating whether or not the 'target' can be constructed by concatenating elements of the 'wordBank' array.
You may reuse elements of 'wordBank' as many times as needed.
"""

def canConstruct(target, wordBank):
    if target == '': return True

    for word in wordBank:
        if target.startswith(word):
            suffix = target[len(word):]
            if canConstruct(suffix, wordBank) == True:
                return True

    return False

print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"])) # True
print(canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])) # False
print(canConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])) # True
# print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"])) # False # time exceeding

# m: target    n: length of word bank array
# time complexity O(n^m * m) 
# space complexity O(m * m)