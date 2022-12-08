a,b=-1,1
def fib(a,b,n):
    c =a+b
    a=b
    b=c
    if n==0: return
    print(c,end=' ')
    fib(a,b,n-1)

n=int(input('Enter the nth term : '))
fib(a,b,n)
