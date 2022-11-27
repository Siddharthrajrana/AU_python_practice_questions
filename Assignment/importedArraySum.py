
#import Array
from array import *
a = array("i",[])
n = int(input("Enter the length of array "))
#taking input from user 
for i in range(n):
    print("Enter ",i,"term ",end=" ")
    x = int(input())
    a.append(x)
# print array
print ("The new created array is : ", end =" ")    
print (a)
#sum of array elements 
sum=0
for i in range(0,n):
    sum=sum+a[i]
#print sum
print("Sum is : ",sum)



