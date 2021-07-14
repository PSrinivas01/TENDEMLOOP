n=int(input("enter some number"))
for x in range(1,n+1):
    if x%2 !=0:
        for y in range(1,x+1):
            print(y,end=",")
    else:
        for k in range(x,0,-1):
            print(k,end=",")
    print()

for x in range(n-1,0,-1):
    if x%2 ==0:
        for y in range(x,0,-1):
            print(y,end= ",")
    else:
        for k in range(1,x+1):
            print(k,end=",")
    print()
    
