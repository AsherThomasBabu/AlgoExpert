# Write a function that takes in a non-empty string and that returns a boolean representing whether the string is a palindrome.
# A palindrome is defined as a string that's written the same forward and backward. Note that single-character strings are palindromes.

def isPalindrome(string):
    left = 0
    right = len(string) - 1
    count = 0
    while left < right:
        if string[left] == string[right]:
            count += 2
        left += 1
        right -= 1
        if len(string) % 2 == 0 and count == len(string):
            return True
        elif len(string) % 2 != 0 and count + 1 == len(string):
            return True
        return False
