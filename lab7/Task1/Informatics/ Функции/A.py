def Min(b):
    min=1e5
    for i in range(len(b)):
        if b[i]<min:
            min=b[i]
    return min



b=list(map(int,input().split()))
print(Min(b))