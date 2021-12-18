def fibonaaci(p):
    a=0
    b=1
    print(a)
    for i in range(2,p):
        print(b,end=" ")
        c=a+b
        a=b
        b=c
        

fibonaaci(8)
