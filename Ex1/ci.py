p = float(input("Enter the principal amount : "))
t = int(input("Enter time in year : "))
r = float(input("Enter rate percent in year : "))
CI = float(p*((1+(r/100))**t))-p
print("Compound intrest is :  ",CI)




