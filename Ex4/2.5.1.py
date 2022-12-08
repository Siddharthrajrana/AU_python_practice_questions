
a=-1
b=1
def fib(a,b,n):
    while n!=0:
        c=a+b
        print(c,end=" ")
        a=b
        b=c
        n-=1

n=int(input("Enter the nth term of fibonacci : "))
fib(a,b,n)

