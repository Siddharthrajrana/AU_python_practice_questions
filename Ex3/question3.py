unit=float(input("Enter the unit of bill consumed : "))

bill=0

if((unit>=0)and(unit<=150)):
    bill=3*unit
elif((unit>=151)and(unit<=350)):
    bill=100+unit*3.75
elif((unit>=351)and(unit<=450)):
    bill=250+unit*4
elif((unit>=451)and(unit<=600)):
    bill=300+unit*4.25
else:
    bill=400+unit*5

print("Your Total Bill is : Rs.",bill)

