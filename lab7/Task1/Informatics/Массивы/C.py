a=int(input())
b=list(map(int,input().split()))
score=0
for i in range(a):
    elem=b[i]
    index=i
    if elem>0:
        score+=1
print(score,end=" ")