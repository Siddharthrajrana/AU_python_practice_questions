#Write a program to read month of the year as an integer. Then display the name of the 
#month
import datetime

month=int(input("Enter month in integer : "))
x=datetime.datetime(2022,month,1)

print(x.strftime("%B"))