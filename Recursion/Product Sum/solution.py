# Write a function that takes in a a special array and reruns its product sum.

def productSum(array, depth = 1):
    sum = 0
    for i in array:
        if type(i) is list:
            sum += depth*productSum(i,depth+1)
        else:
            sum += depth * i
    return sum