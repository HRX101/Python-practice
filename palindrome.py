import math as m
def palindorme(p):
    n=p
    s=0
    while(n!=0):
        r=m.floor(n%10)
        s=(s*10)+r
        n=m.floor(n/10)
    if(p==s):
        return "Palindorme"
    else:
        return "not palindrome"

x=int(input("Enter your value "))
print(f"this is {palindorme(x)}")