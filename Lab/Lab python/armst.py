import math
n=int(input("Enter a number "))
c=int(len(str(n)))
x=n
result=0

while(x!=0):
    rem=x%10
    result=result+rem**c
    x=x//10
    
if(result==n):
    print("Armstrong ")
else:
    print("Not ")
    
