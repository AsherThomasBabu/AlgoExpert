# Write a function that takes in a string of words separated by one or more whitespaces and returns a string that has these words in reverse order. For example, given the string "tim is great" your function should return "great is tim"
# For this problem, a word can contain special characters, punctuation, and numbers. The words in the string will be separated by one or
# more whitespaces, and the reversed string must contain the same whitespaces as the original string. "whitespaces 4" you would be expected to return "4 whitespaces"
# For example, given the string
# Note that you're not allowed to to use any built-in split or reverse methods/functions. However, you are allowed to use a built-in
# join method/function.
# Also note that the input string isn't guaranteed to always contain words.

# string = "AlgoExpert is the best!"
# "best! the is AlgoExpert"


def reverseWordsInString(string):
    charecters = [char for char in string]
    reverseListRange(charecters, 0, len(charecters)-1)

    startOfWord = 0

    while startOfWord < len(charecters):
        endOfWord = startOfWord
        while endOfWord < len(charecters) and charecters[endOfWord] != " ":
            endOfWord += 1

        reverseListRange(charecters, startOfWord, endOfWord - 1)
        startOfWord = endOfWord + 1

    return "".join(charecters)

def reverseListRange(list,start,end):
    while start < end:
        list[start], list[end] = list[end], list[start]
        start += 1
        end -= 1

print(reverseWordsInString("AlgoExpert  is the best!"))
