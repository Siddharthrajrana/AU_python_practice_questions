x=int(input('Enter no'))

n=x

count=len(str(x))

result=0

while n!=0:
    rem=n%10
    result=result+rem**count
    n=n//10
print('Armst') if x==result else print('not ')