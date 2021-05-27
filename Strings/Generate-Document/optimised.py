# You're given a string of available characters and a string representing a document that you need to generate. Write a function that determines if you can generate the document using the available characters. If you can generate the document, your function should return true; otherwise, It should return false.
# You're only able to generate the document if the frequency of unique characters in the characters string is greater than or equal to the frequency of unique characters in the document string. For example, if you're given characters = "abcabc" and document = "aabbccc" you cannot generate the document because you're missing
# one c.
# The document that you need to create may contain any characters, including special characters, capital letters, numbers,
# and spaces.
# Note: you can always generate the empty string("")

# <---------- Runs in O(m+n) Time | O(mn) space ---------->

def generateDocument(characters, document):
    if document == "":
        return True

    dict = {}
    for i in characters:
        if i not in dict:
            dict[i] = 0
        dict[i] += 1

    for i in document:
        if i not in dict or dict[i] == 0:
            return False
        dict -= 1
    
    return True

print(generateDocument("Bste!hetsi ogEAxpelrt x ", "AlgoExpert is the Best!"))
