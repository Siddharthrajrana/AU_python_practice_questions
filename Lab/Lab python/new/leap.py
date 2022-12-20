y=int(input('Enter year'))

print('leap year') if (y%4==0 and y%100!=0) or y%400==0 else print("Not leap year")