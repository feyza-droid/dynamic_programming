"""
Write a function 'countConstruct(target, wordBank)' that accepts a target string and an array of strings.
The function should return the number of ways that the 'target' can be constructed by concatenating elements of the 'wordBank' array.
You may reuse elements of 'wordBank' as many times as needed.
"""

def countConstruct(target, wordBank):
    table = [0 for _ in range(len(target)+1)]
    table[0] = 1

    for i in range(len(table)):
        if table[i] != 0: # it table[i] matched with the correct prefix, it gives a value other than 0
            for word in wordBank:
                if target[i: i+len(word)] == word:
                    table[i+len(word)] += table[i]

    return table[len(target)]

print(countConstruct("purple", ["purp", "p", "ur", "le", "purpl"])) # 2
print(countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"])) # 1
print(countConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])) # 0
print(countConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])) # 4
print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"])) # 0

# m: target    n: length of word bank array
# time complexity O(m^2*n)
# space complexity O(m)