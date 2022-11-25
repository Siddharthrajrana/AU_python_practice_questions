import math
n = int(input("Enter the nth term : "))
i=1  
z=0
while n!=0:
    z=z+math.pow(i,2)
    i = i+1
    n=n-1
print("Sum of Square is : ",z)


