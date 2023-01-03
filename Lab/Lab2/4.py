def check_armstrong(num):
    x = num
    result = 0
    while(x!=0):
        rem = x%10
        result = result + rem**3
        x = x//10
    print("Armstrong " )  if(result == num ) else print("Not Armstrong ")

num=int(input("Enter a number " ))
check_armstrong(num)
        
   
