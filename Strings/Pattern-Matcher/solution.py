# You're given two non-empty strings. The first one is a pattern consisting of only "x"s and/or "y" s; the other one is a normal string of alphanumeric characters. Write a function that checks whether the normal string matches the pattern.

# A string S0 is said to match a pattern if replacing all "x"s in the pattern with some non-empty substring S1 of S0 and replacing all "y" s in the pattern with some non-empty substring $2 of 50 yields the same string S0

# If the input string doesn't match the input pattern, the function should return an empty array; otherwise, it should return an array holding the strings S1 and $2 that represent "x" and "y" in the normal string, in that order. If the pattern doesn't contain any "x" s or "y" s, the respective letter should be represented by an empty string in the final array that you return.

# You can assume that there will never be more than one pair of strings S1 and S2 that appropriately represent "x" and "y" the normal string.
# 
# pattern = "xxyxxy",
# string = "gogopowerrangergogopowerranger"
# 
# # Output = ["go", "powerranger"]

def patternMatcher(pattern, string):
    pattern,foo = getNewPattern(pattern)
    dict,yPos = countPattern(pattern)
    strLength = len(string)
    x,y = "",""
    if dict["y"] == 0:
        xLen = int(strLength/dict["x"])
        x = string[:xLen]
        if foo:
                return [y,x]
        return [x,y]
    for i in range(1,strLength):
        x = string[:i]
        yLen = int((strLength - i * dict["x"])/dict["y"])
        yIdx = int(yPos * i) 
        y = string[yIdx:yIdx+yLen]
        tempString = []
        for i in pattern:
            if i == "x":
                tempString.append(x)
            else:
                tempString.append(y)

        if "".join(tempString) == string:
            if foo:
                return [y,x]
            return [x,y] 
    return []

def getNewPattern(string):
    foo = True
    stringList = list(string)
    if stringList[0] == "x":
        foo =  False
        return stringList,foo
    for i in range(len(stringList)):
        if stringList[i] == "x":
            stringList[i] = "y"
        else:
            stringList[i] = "x"
    return stringList,foo

def countPattern(array):
    yPos = 0
    dict = {"x":0,"y":0}
    for i in array:
        if i == "x":
            dict["x"] += 1
        else:
            dict["y"] += 1
    for i in range(len(array)):
        if array[i] == "y":
            yPos = i
            break
    return dict,yPos
            
print(patternMatcher("xxyxxy","gogopowerrangergogopowerranger"))