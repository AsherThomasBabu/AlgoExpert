# Write a function that takes in a string of lowercase English-alphabet letters and returns the index of the string's first non-repeating character.
# The first non-repeating character is the first character in a string that occurs only once.
# If the input string doesn't have any non-repeating characters, your function should return -1

# Sample Input
# string = "abcdcaf

# Sample Output
# 1 // The first non-repeating character is "b" and is found at index 1.

# <---------- Runs in O(n) Time | O(n) space ---------->

def firstNonRepeatingCharacter(string):
    dict = {}
    for i in string:
        if i not in dict:
            dict[i] = 0
        dict[i] += 1
    
    for i in dict:
        if dict[i] == 1:
            return string.index(i)

    return -1   

print(firstNonRepeatingCharacter("abcdcaf"))