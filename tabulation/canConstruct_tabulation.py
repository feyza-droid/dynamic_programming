"""
Write a function 'canConstruct(target, wordBank)' that accepts a target string and an array of strings.
The function should return a boolean indicating whether or not the 'target' can be constructed by concatenating elements of the 'wordBank' array.
You may reuse elements of 'wordBank' as many times as needed.
"""

def canConstruct(target, wordBank):
    table = [False for _ in range(len(target)+1)]
    table[0] = True # empty string can always be generated
    
    for i in range(len(table)):
        if table[i]: # if it is True
            for word in wordBank:
                if target[i:i+len(word)] == word:  # if the word matches the characters starting and position i
                    table[i + len(word)] = True
                    # if table[len(target)]: NOTE: early stopping, you can return when you find at least one can construct
                    #    return table[len(target)]

    return table[len(target)]

print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"])) # True
print(canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])) # False
print(canConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])) # True
print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"])) # False

# m: target    n: length of word bank array
# time complexity O(m^2*n) 
# space complexity O(m)