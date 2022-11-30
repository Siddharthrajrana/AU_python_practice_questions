x=input("Enter first string : ")
y=input("Enter second String : ")

#method1
print("String Cocatenation using + operator ",x+y)
#method2
print("String Concatenation Using join()" , " ------------  ".join([x,y]))
#method3
print("String Concatenation using place holder operator %s %s"%(x,y))
#method4
print("String conxcatenation Using format() ","{}*****************************************{}".format(x,y))
#method%
print("String Concatination using f-string ", f'{x}########################################{y}')