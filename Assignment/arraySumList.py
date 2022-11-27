# Q : To find the sum of element in array using list
numlist=[]

n=int(input("Enter the number of Elements : "))

for i in range(0,n):
    ele=int(input())

    numlist.append(ele)

print(numlist)

numsum=0

for i in range(0,n):
    numsum=numsum+numlist[i]



print("Sum of Element in list is : ",numsum)
