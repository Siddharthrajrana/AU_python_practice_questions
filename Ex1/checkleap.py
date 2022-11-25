year = int(input("Enter a Year : "))
if year%400==0:
    if year%4==0:
        print("Leap Year ")
    else:
        print("Not Leap Year ")
elif year%400==0:
    print("Leap Year ")
else:
    print("Not a Leap Year.")