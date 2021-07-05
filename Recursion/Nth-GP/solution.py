# Write a program to find the Nth term of a GP recursively

def NthGP(n,a,r):
    # a = first term
    # r = common ratio
    if n == 0:
        return a
    return r*NthGP(n-1,a,r)

print(NthGP(5,2,4))