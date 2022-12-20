u=float(input("Enter the unit : " ))
bill=0
if u>=0 and u<=150:
    print("Bill = ", u*3)
elif u>=151 and u<=300:
    print("Bill = ", 100+u*3.75)
elif u>=301 and u<=450:
    print("Bill = ", 250+u*4)
elif u>=451 and u<600:
    print("Bill = ", u*4.25+300)
elif u>=600:
    print("Bill = ", u*5+400)
else:
    print("Invalid ")
