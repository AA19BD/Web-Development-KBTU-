x=int(input())
d=int(input())

score=0
for i in str(x):
    if i==str(d):
        score+=1

print(score,end=" ")

# print(str(x).count(str(d)))--simple solution 