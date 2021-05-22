# Write a function that takes in an array of integers and returns the length of the longest peak in the array.
# A peak is defined as adjacent integers in the array that are strictly increasing until they reach a tip (the highest value in the peak), at which point they become strictly decreasing. At least three integers are required to form a peak.
# For example, the integers 1, 4, 10,
# Similarly, the integers 1, 2, 3

def longestPeak(array):
    count = 0
    reservecount = 0
    i = 0
    while i < len(array) - 1:
        if array[i] < array[i+1]:
            count += 1
        elif count >= 1 and array[i] == array[i+1]:
            count = 0
            continue
        elif count >= 1 and array[i] > array[i+1]:
            count += 1
            for j in range(i, len(array) - 1):
                if array[j] > array[j+1]:
                    count += 1
                else:
                    i = j-1
                    break
            if count > reservecount:
                reservecount = count
                count = 0
        i+=1
    return reservecount


print(longestPeak([2, 1, 4, 7, 3, 2, 5]))