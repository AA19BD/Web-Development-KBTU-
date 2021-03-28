def Xor(x,y):
    return (1 if x==1 and  y==0  or x==0 and y==1 else 0)
a,b=list(map(int,input().split()))
print(Xor(a,b))