#Program to calculate Body Mass Index 
weight = float(input("Enter the Weight in kg : "))
height=float(input("Enter the height in cm : "))

if(weight==0 or height==0):
    print("Please Enter Valid Information .")
elif((weight<8 or weight>250)or(height<50 or height>220)):
    print("Please Enter valid Details ")
else:
    BMI=(weight/(height/100)**2)
    if(BMI<18.5):
        print("Health Condition = Underweight BMI = %.2f"%BMI)
    elif(BMI>25):
        print("Health Condition = Overweight BMI = %.2f"%BMI)
    else:
        print("Health Condition is Normal BMI = %.2f"%BMI)
