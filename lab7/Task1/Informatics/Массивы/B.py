a=int(input())
b=list(map(int,input().split()))
for i in range(a):
    elem=b[i]
    index=i
    if elem%2==0:
        print(elem,end=" ")