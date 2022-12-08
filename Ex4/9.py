def check_leapYear(y):
    if y%4==0 and y%100!=0 or y%400==0: return 'Leap year'
    else : return 'Not Leap Year'
year=int(input("Enter a year : "))
print(check_leapYear(year))
