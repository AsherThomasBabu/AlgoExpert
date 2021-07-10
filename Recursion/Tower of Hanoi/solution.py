# Write a recursive solution to print all the steps in teh tower of hanoi problem.

def towerOfHanoi(n, from_rod, to_rod, aux):
    if n == 1:
        print("Move disk 1 from rod {} to {}".format(from_rod,to_rod))
        return
    towerOfHanoi(n-1,from_rod, aux, to_rod)
    print("Move disk {} from rod {} to {}".format(n,from_rod,to_rod))
    towerOfHanoi(n-1,aux,to_rod,from_rod)

towerOfHanoi(4,'A','C','B')