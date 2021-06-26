# The Fibonacci sequence is defined as follows: the first number of the sequence is the second number is 1 and the nth number is the sum of the (n-1)th and (n-2)th numbers. Write a function that takes in an integer and returns the nth Fibonacci number.
# Important note: the Fibonacci sequence is often defined with its first two numbers as [Fe = 0 and [F1 = 1. For the purpose of this question, the first Fibonacci number is [FO; therefore, [getNthFib(1) is equal to [Fe getNthFib (2) is equal to F1, etc..

def getNthFib(n):
    arr = [0,1]
    
    if n == 2:
        return 1
    elif n == 1:
        return 0

    for i in range(2,n):
        cur = sum(arr)
        arr[0],arr[1] = arr[1],cur

	return arr[-1]
