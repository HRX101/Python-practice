p=list(map(int,input().rstrip().split()))


for i in range(len(p)):
    flag=0
    for j in range(2,p[i]):
        if(p[i]%j==0):
            flag=+1
    if(flag==0):
        print(f"{p[i]} is the prime")
    else:
        print(f"{p[i]} is not prime")

