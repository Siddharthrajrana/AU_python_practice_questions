# Question: Count total Even and Odd element in array taking input from User 
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
#count even and odd 
even =0
odd =0

for i in range(0,n):
    if a[i]%2==0:
        even=even+1
    else:
        odd=odd+1
#print result
print("Total Even is  : ",even)
print("Total Odd is : ",odd )





