from math import *
n=int(input())
def func(n):
    res=0
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            res+=2-(i*i==n)
    return res+2-(n==1)
print(func(n))