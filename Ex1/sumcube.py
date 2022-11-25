import math
n =int(input("Enter the nth term : "))
i=1
sum=0
while n!=0:
    sum=sum+math.pow(i,3)
    n=n-1
    i=i+1
print("Sum of cube is : ",sum)
