# Write a function that takes in an array of words and returns the smallest array of characters needed to form all of the words. The characters don't need to be in any particular order.
# For example, the characters ["y", "r", "o", "u"] are needed to form the words [["your", "you", "or", "yo"] Note: the input words won't contain any spaces; however, they might contain punctuation and/or special characters.

# ["this", "that", "did", "deed", "them!", "a"]

def minimumCharactersForWords(words):
    seen = {words[0][0]}
    for i in words:
        for j in list(i):
            seen.add(j)
    return list(seen)


print(minimumCharactersForWords(["this", "that", "did", "deed", "them!", "a"]))

