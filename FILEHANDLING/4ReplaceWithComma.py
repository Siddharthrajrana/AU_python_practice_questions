file1=open("file1.txt","r")
file2=open("file2.txt","w")
while 1:
    char=file1.read(1)
    #print(char)
    if not char:
        break
    if char=='.':
      file2.write(',')
    else:
       file2.write(char)


file1.close()
file2.close()
