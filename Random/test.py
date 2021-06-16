import os

files = folders = 0

path = "./"

f= os.listdir(path)
lis = []
for i in f:
    lis.append(len(os.listdir(path + str(i))))
    
print(sum(lis))