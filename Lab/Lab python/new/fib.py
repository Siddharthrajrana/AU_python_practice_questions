a,b=-1,1

n=int(input('Enter the nth term'))

while n!=0:
    c=a+b
    print(c,end=' ')
    a,b=b,c
    n-=1
