n=int(input("enter the no  of rows"))
for i in range(1,n+1):
    p=1
    for j in range(i):
        print(p,end=" ")
        p+=1
    print()