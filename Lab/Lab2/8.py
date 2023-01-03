def cal_bill(unit):
    if unit>=0 and unit<=150 : return (unit*3)
    elif unit >150 and unit<= 300 : return (unit-150)*3.75+100 
    elif unit >300 and unit<= 450 : return (unit-300)*4+250
    elif unit >450 and unit<= 600 : return (unit-450)*4.25+300
    else: return (unit-600)*5 + 400

unit = float(input("Enter the unit of consumption : " ))
print("Total Bill is  : Rs.",cal_bill(unit))
