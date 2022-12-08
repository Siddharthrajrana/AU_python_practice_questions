def fun():
    '''Write a function called printStatus that is passed status code
    ‘S’, ‘M’, ‘D’, or ‘U’ and returns the string ‘Separated’, ‘Married’,
    ‘Divorced’ or ‘Unmarried’ respectively. In case an inappropriate
    letter is passed, print an appropriate message. Also include a
    docstring with your invitation'''
    code =input("Enter the any of the code S M D U " )
    if(code=='S'):print("Seperated")
    elif(code=='M'):print("Married")
    elif(code=='D'):print("Divorsed")
    elif(code=='U'):print("Unmarried")
    else:print("Please Enter one of the Mentioned code ")

print(fun.__doc__)
fun()
