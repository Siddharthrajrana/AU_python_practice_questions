import os
file1=open("file1.txt","r")
file3=open("file3.txt","w")

while 1:
    char=file1.read(1)
    #print(char)
    if not char:
        break
    file3.write(char)

file3.close()
file1.close()
file2=open("file2.txt","r")
file1=open("file1.txt","w")

while 1:
    char=file2.read(1)
    #print(char)
    if not char:
        break
    file1.write(char)

file2.close()
file1.close()

file3=open("file3.txt","r")
file2=open("file2.txt","w")

while 1:
    char=file3.read(1)
    #print(char)
    if not char:
        break
    file2.write(char)

file3.close()
os.remove("file3.txt")
print("DOne")
#
file2.close()
