def is_prime(n):
    for i in range(2,n):
        return 0 if n%i==0 else  1
num=int(input("Enter a number "))
print(is_prime(num))
