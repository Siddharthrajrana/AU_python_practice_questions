n=int(input("Enter a no. "))
t=0
while(n!=0):
    r=n%10
    t=r+t*10
    n=n//10
print("Reverse is : ",t)
    
    
