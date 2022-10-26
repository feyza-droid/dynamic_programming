"""
Write a function 'allConstruct(target, wordBank)' that accepts a target string and an array of strings.
The function should return a 2D array containing all of the ways that the 'target' can be constructed by concatenating elements of the 'wordBank' array.
Each element of the 2D array should represent one combination that constructs the 'target'.
You may reuse elements of 'wordBank' as many times as needed.
"""



def allConstruct(target, wordBank, memo):
    if target in memo: return memo[target]
    if target == '': return [[]]

    result = []
    for word in wordBank:
        if target.startswith(word):
            suffix = target[len(word):]
            suffixWays = allConstruct(suffix, wordBank, memo) # returns [[]] from desired leaves
            targetWays = list(map(lambda suffixWay: [word] + suffixWay, suffixWays))
            result += targetWays

    memo[target] = result
    return memo[target]

print(allConstruct(target="purple", wordBank = ["purp", "p", "ur", "le", "purpl"], memo = {}))
print(allConstruct(target="abcdef", wordBank = ["ab", "abc", "cd", "def", "abcd", "ef", "c"], memo = {}))
print(allConstruct(target="skateboard", wordBank = ["bo", "rd", "ate", "t", "ska", "sk", "boar"], memo = {}))
print(allConstruct(target="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaz", wordBank = ["a", "aa", "aaa", "aaaa", "aaaaa"], memo = {}))

# m: target    n: length of word bank array
# time complexity O(n^m) 
# space complexity O(m)