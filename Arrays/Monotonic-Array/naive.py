# """
# An array is monotonic if it is either monotone increasing or monotone decreasing.
# An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].
# Return true if and only if the given array A is monotonic.
# Input: [1,2,2,3]
# Output: true
# Input: [1,3,2]
# Output: false
# """

def isMonotonic(array):
    return asc(array) or desc(array)

def asc(array):
    for i in range(len(array)-1):
        if array[i] <= array[i+1]:
            continue
        else:
            return False
    return True

def desc(array):
    for i in range(len(array)-1):
        if array[i] >= array[i+1]:
            continue
        else:
            return False
    return True

print(isMonotonic([2, 1, 2, 2, 2, 3, 4, 2]))
