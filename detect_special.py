def special(x):
    for i in range(len(x)):
        if((x[i]>="a" and x[i]<="z")or(x[i]>="A" and x[i]<="Z")):
            pass
        else:
            print(f"this is bad {x[i]}")
special(str(input("enter your name ")))
