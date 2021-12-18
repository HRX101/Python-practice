if __name__=="__main__":
    for i in range(5):
        for j in range(i+1):
            print("*",end=" ")
        print("")
    for i in range(5,0,-1):
        for j in range(i,0,-1):
            print("*",end=" ")
        print("")