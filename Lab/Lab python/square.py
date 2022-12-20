n = int(input("Enter the nth term : "))
sum = 0
while n!=0:
    sum=sum+n**2
    n-=1
print(sum)
