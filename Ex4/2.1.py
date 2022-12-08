def rev(n):
    if n<10:
        print(n,end="")
        return 
    else:
        print(n%10,end="")
        rev(n//10)
        
num =int(input('Enter a number :'))
print('Reverse is ')
rev(num)














    
