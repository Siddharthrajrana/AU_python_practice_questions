x=int(input("Enter the value of x : "))
n=int(input("Enter the nth term : "))

i=1
sum=0
while(n!=0):
    sum =sum+(-x)**i
    i=i+1
    n=n-1
print("The value of Sum of the Series is : ",sum)