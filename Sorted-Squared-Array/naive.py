

def sortedSquaredArray(array):
    # Write your code here.
    new = []
    for i in range (0, len(array)):
        temp= array[i]*array[i]
        new.append(temp)
    new.sort()
    return new
