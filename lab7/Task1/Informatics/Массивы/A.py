a=int(input())
b=list(map(int,input().split()))
for i in range(len(b)):
    if i%2==0:
        print(b[i],end=" ")
