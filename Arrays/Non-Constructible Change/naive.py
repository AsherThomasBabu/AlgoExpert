# Given an array of positive integers representing the values of coins in your possession, write a function that returns the minimum amount of change (the minimum sum of money) that you cannot create. The given coins can have any positive integer value and aren't necessarily unique (.e., you can have multiple coins of the same value). 

# For example, if you're given coins = [1, 2, 5], the minimum amount of change that you can't create is 4. If you're given no coins, the minimum amount of change that you can't create is 1.

def nonConstructibleChange(array):
    sumChange = []
    array.append(0)
    for i in range(len(array)):
        for j in range(len(array)):
            if i <= j:
                continue
            else:
                sumChange.append(array[j]+array[i])
    sumChange.sort()
    checkArray = [i for i in range(1,max(sumChange))]
    for i in range(1,max(checkArray)):
        if i not in sumChange:
            return i
