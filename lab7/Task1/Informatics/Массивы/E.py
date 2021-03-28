a=int(input())
b=list(map(int,input().split()))
check=False
for i in range(1,a):
    elem=b[i]
    index=i
    if (b[i]>0 and b[i-1]>0 ) or (b[i]<0 and b[i-1]<0 ):
        check=True

if check:
    print("YES")
else:
    print("NO")