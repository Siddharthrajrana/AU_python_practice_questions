file1=open("file1.txt","r")
file3=open("file3.txt","w")
str=file1.read();
s1=""
for i in str:
    s1=i+s1

file3.write(s1)
file3.close()
