"""
Write a function 'allConstruct(target, wordBank)' that accepts a target string and an array of strings.
The function should return a 2D array containing all of the ways that the 'target' can be constructed by concatenating elements of the 'wordBank' array.
Each element of the 2D array should represent one combination that constructs the 'target'.
You may reuse elements of 'wordBank' as many times as needed.
"""

def allConstruct(target, wordBank):
    table = [[] for _ in range(len(target) + 1)]
    table[0] = [[]]

    for i in range(len(table)):
        for word in wordBank:
            if target[i: i + len(word)] == word:
                newCombinations = list(map(lambda way: way + [word], table[i]))
                table[i + len(word)] += newCombinations

    return table[len(target)]

print(allConstruct(target="purple", wordBank = ["purp", "p", "ur", "le", "purpl"]))
print(allConstruct(target="abcdef", wordBank = ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))
print(allConstruct(target="skateboard", wordBank = ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(allConstruct(target="aaaaaaaaaaz", wordBank = ["a", "aa", "aaa", "aaaa", "aaaaa"]))
# print(allConstruct(target="aaaaaaaaaaaaaaaaaaaaa", wordBank = ["a", "aa", "aaa", "aaaa", "aaaaa"]))

# m: target    n: length of word bank array
# time complexity O(n^m)
# space complexity O(n^m)