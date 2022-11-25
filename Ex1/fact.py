num=int(input("Enter a number : "))

if num<0 :
    print("factorial of negative number is not possible ")
elif num==0:
    print("Factorial is 1")
elif num>0:
    fact=1
    while(num!=0):
        fact=fact*num
        num=num-1
    print("Factorial is : ",fact)
else:
    print("It's not a number .")


























