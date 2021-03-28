from math import *
a=int(input())
b=int(input())
for i in range(a,b+1):
    if i%sqrt(i)==0:
        print(i)