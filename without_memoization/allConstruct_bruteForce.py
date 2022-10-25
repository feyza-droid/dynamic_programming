"""
Write a function 'allConstruct(target, wordBank)' that accepts a target string and an array of strings.
The function should return a 2D array containing all of the ways that the 'target' can be constructed by concatenating elements of the 'wordBank' array.
Each element of the 2D array should represent one combination that constructs the 'target'.
You may reuse elements of 'wordBank' as many times as needed.
"""



def allConstruct(target, wordBank):
    if target == '': return [[]]

    result = []
    for word in wordBank:
        if target.startswith(word):
            suffix = target[len(word):]
            suffixWays = allConstruct(suffix, wordBank) # returns [[]] from desired leaves
            targetWays = list(map(lambda suffixWay: [word] + suffixWay, suffixWays))
            result += targetWays

    return result

print(allConstruct(target="purple", wordBank = ["purp", "p", "ur", "le", "purpl"]))
print(allConstruct(target="abcdef", wordBank = ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))
print(allConstruct(target="skateboard", wordBank = ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
# print(allConstruct(target="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaz", wordBank = ["a", "aa", "aaa", "aaaa", "aaaaa"])) # time exceeding

# m: target    n: length of word bank array
# time complexity O(n^m) 
# space complexity O(m)