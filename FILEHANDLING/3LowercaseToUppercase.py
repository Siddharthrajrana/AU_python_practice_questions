file1=open("file1.txt","r")
file3=open("file3.txt","w")
s=""
while 1:
  char=file1.read(10)
  if not char:
       break

  s=char.upper()
  file3.write(s)

print("Done")
file1.close()
file3.close()
