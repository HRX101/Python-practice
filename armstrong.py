import math 
import math
def armstrong(p):
    n=math.floor(p)
    s=0
    while(n!=0):
        r=math.floor(n%10)
        s=s+(r*r*r)
        n=math.floor(n/10)
  
    if(s==p):
        return "Armstrong"
    else:
        return "not"

x=int(input("\n Enter your value "))
print(armstrong(x))
