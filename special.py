import math
def special(p):
    s=0
    n=math.floor(p)
    while(n!=0):
        r=math.floor(n%10)
        r=fact(r)
        s=s+r
        n=math.floor(n/10)

    if(p==s):
        print("yes")
    else:
        print("no")
        

def fact(z):
    s=1
    for i in range(z):
        s=s*(i+1)
    return s
x=int(input("enter "))
special(x)