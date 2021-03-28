a=int(input())
sum=0
list=" "
for i in str(a):
    list+=i
b=(list[-1::-1])
# print(b)
for i,j in zip(str(b),range(len(str(a)))):
    sum+=(int(i))*(2**j)
    # print(i,j)

print(sum)

