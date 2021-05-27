# Given a non-empty string of lowercase letters and a non-negative integer representing a key, write a function that returns a new string obtained by shifting every letter in the input string by k positions in the alphabet, where k is the key.

# Note that letters should "wrap" around the alphabet; in other words, the letter 2 shifted by one returns the letter a

def caesarCipherEncryptor(string, key):
    result = []
    txt = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    alphabet = list(txt)
    for i in string:
        result.append(alphabet[alphabet.index(i)+2])
    return "".join(result)
        
print(caesarCipherEncryptor('xyz',2))
