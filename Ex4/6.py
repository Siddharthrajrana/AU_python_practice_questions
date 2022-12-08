def find_greatest(x,y,z):
    if(x>=y and x>z): return x
    elif(y>=z): return y
    else: return z

x=int(input("Enter the 1 no."))
y=int(input("Enter the 2 no"))
z=int(input("Enter the 3 no "))
print('greatest is :',find_greatest(x,y,z))
