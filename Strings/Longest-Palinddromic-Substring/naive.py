# Write a function that, given a string, returns its longest palindromic substring.
# A palindrome is defined as a string that's written the same forward and backward. Note that single-character strings are palindromes.
# You can assume that there will only be one longest palindromic substring.

# Sample Input
# string = "abaxyzzyxf"

# Sample Output
# "xyzzyx"

def longestPalindromicSubstring(string):
    right = len(string) - 1
    count = 0
    answer = ""

    if len(string) < 2:
        return string

    for i in range(len(string)):
        while i < right:
            if string[i] == string[right] and isPalindrome(string[i:right+1]):
                if len(string[i:right+1]) > count:
                    count = len(string[i:right+1])
                    answer = string[i:right+1]
            right -= 1
        right = len(string) - 1
    return answer


def isPalindrome(string):
    leftIdx = 0
    rightIdx = len(string) - 1

    while leftIdx < rightIdx:
        if string[leftIdx] != string[rightIdx]:
            return False
        leftIdx += 1
        rightIdx -= 1
    return True


print(longestPalindromicSubstring("abaxyzzyxf"))
