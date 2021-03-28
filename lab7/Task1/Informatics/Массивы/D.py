a=int(input())
b=list(map(int,input().split()))
score=0
for i in range(1,a):
    elem=b[i]
    index=i
    if b[i]>b[i-1]:
        score+=1
print(score)