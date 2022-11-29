import math
x=int(input("Enter the value of x: "))
n=int(input("Enter the nth term : "))
sum=0
i=0
while(n!=0):
    sum=sum+(-x)**i/math.factorial(i)
    n=n-1
    i=i+1

print("The value of Sum is : ",sum)