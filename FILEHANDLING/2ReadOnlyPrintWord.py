with open("file1.txt","r") as file:
    for line in file:
        if "print" in line:
           print(line)


print("Reading Done")
