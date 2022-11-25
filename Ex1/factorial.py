x=int(input("Enter an integr : "))
fact = 1
if x<0: 
     print("Factorial of negative number is not possible ")
elif x==1:
      print("Factorial is 1.")
else:
     while(x!=1):
       fact = fact*x
       x = x-1
print("Factorial is : ",fact)

