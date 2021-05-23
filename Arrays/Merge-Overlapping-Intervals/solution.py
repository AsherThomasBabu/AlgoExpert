# Write a function that takes in a non-empty array of arbitrary intervals, merges any overlapping intervals, and returns the new Intervals in 4
# no particular order.
# Each interval interval is an array of two integers, with interval [0] as the start of the interval and interval [1] as the end of
# the interval.
# Note that back-to-back intervals aren't considered to be overlapping. For example, [[1, 5] and [6, 7] aren't overlapping; however,
# [1, 6] and [6, 7] are indeed overlapping.
# Also note that the start of any particular interval will always be less than or equal to the end of that interval.

# intervals = [[1, 2], [3, 5], [4, 7], [6, 8], [9, 18]]

# Sample Output
# [[1, 2], [3, 8], [9, 18]]


def mergeOverlappingIntervals(intervals):
    sortedArray = sorted(intervals,key=lambda x: x[0])
    result = []
    currentElement = sortedArray[0]
    result.append(currentElement)

    for nextElement in sortedArray:
        _, currentEnd = currentElement
        nextBegining, nextEnd = nextElement
        print(currentEnd,nextBegining,nextEnd)

        if currentEnd >= nextBegining:
           currentElement[1] = max(currentEnd,nextEnd)
        else:
            currentElement = nextElement
            result.append(currentElement)
    return result 

print(mergeOverlappingIntervals([
    [2, 3],
    [4, 5],
    [6, 7],
    [8, 9],
    [1, 10]
]))

print(mergeOverlappingIntervals([
    [1, 22],
    [-20, 30]
]))
