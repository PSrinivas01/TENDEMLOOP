a=int(input("Enter any number "))

if a%2==0:
    a=a-1
else:
    a=a

num=1
while(a>0):
    if num%2==1:
        print(num,end=",")
        a-=1
    num+=1
    
        
    
