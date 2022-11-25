num = int(input("Enter a number : "))
x = num
count = int(len(str(num)))
result = 0
while x>0:
	rem=x%10
	result=result+rem**count
	x//=10
if result==num:
	print("Armstrong Number ")
else:
	print("Not an Armstring Number ")