a = int(input("Enter a number : "))
x=1
c=0
b=0
while(x<=a):
	if(a%x==0):
		c+=1
	x+=1
if(c==2):
	print("Prime")
else:
	print("Not Prime")