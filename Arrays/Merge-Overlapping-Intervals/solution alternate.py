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
    intervals.sort(key=lambda x: x[0])
    result = []
    result.append(intervals[0])
    for i in range(1, len(intervals)):
        if intervals[i][0] <= result[-1][1]:
            result[-1][1] = max(intervals[i][1],result[-1][1])
        else:
            result.append(intervals[i])
    return result  
