import math
def happy(x):
    n=math.floor(x)
    p=True
    s=0
    while(p!=False):
        
        while(n>9):
            r=math.floor(n%10)
            s=s+(r*r)
            n=n/10
        n=s
        s=0
        if(n==1):
            p=False
            print("got")
            break
            
        if(n<=9 and n!=1):
            p=False
            print(" not got")
            break
        


            

happy(20)

