# Write a function that takes in an array of strings and groups anagrams together.

# Anagrams are strings made up of exactly the same letters, where order doesn't matter. For example, "cinema" and "iceman" are anagrams; similarly. "foo" and "ofo" are anagrams. Your function should return a list of anagram groups in no particular order.

# sample = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]

# Output = [
    # ["yo", "oy"],
    # ["act", "tac", "cat"],
    # ["flop", "olfp"],
    # ["foo"]
# ]
# 

def groupAnagrams(words):
    dict = {}
    for word in words:
        sortedWords = tuple(sorted(word))
        if sortedWords not in dict:
            dict[sortedWords] = []
        dict[sortedWords].append(word)
    return list(dict.values())

sample = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
print(groupAnagrams(sample))