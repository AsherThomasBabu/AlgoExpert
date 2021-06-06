# Write a function that takes in two strings: a main string and a potential substring of the main string. The function should return a version of the main string with every instance of the substring in it wrapped between underscores.
# If two or more instances of the substring in the main string overlap each other or sit side by side, the underscores relevant to these substrings should only appear on the far left of the leftmost substring and on the far right of the rightmost substring. If the main string
# doesn't contain the other string at all, the function should return the main string intact.

# string = " testthis is a testtest to see if testestest it works"
# substring = "test"

# _test_this is a _testtest_ to see if _testestest_ it works

def underscorifySubstring(string, substring):
    res = [[i,i+len(substring)] for i in range(len(string)) if string.startswith(substring,i)]
    if not res:
        return string
    return removeDuplicates(res,string)

def removeDuplicates(array,string):
    result = []
    currentElement = array[0]
    result.append(currentElement)

    for nextElement in array:
        _, currentEnd = currentElement
        nextBegining, nextEnd = nextElement

        if currentEnd >= nextBegining:
           currentElement[1] = max(currentEnd,nextEnd)
        else:
            currentElement = nextElement
            result.append(currentElement)
    return underScorify(result,string)

def underScorify(array,string):
    lstr = list(string)
    count = 0
    for i in array:
        lstr.insert(i[0] + count,'_')
        count += 1
        lstr.insert(i[1] + count, "_")
        count += 1
    return ("".join(lstr))




print(underscorifySubstring("testthis is a testtest to see if testestest it works","test"))