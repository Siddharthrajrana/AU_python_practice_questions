def take_input():
    n1 = int(input("Enter first integer : "))
    n2 = int(input("Enter Second integer : "))
    n3 = int(input("Enter third integer : "))
    check_sorted(n1,n2,n3)

def check_sorted(n1,n2,n3):
    if(n1<=n2<=n3) or (n1>=n2>=n3):
        print("True  ")
    else:
        print("False " )

take_input()

