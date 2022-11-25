l = int(input("Enter the Lower limit : "))
u = int(input("Enter the upper limit : "))

l=list(range(l,u+1,1))
print(l)
print("Checking")
for i in l:
	x=1
	c=0
	while(x<=i):
		if(i%x==0):
			c+=1
		x+=1
	if(c==2):
		print("prime"+str(i))
	else:
		print("not prime"+str(i))

			