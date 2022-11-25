x = int(input("Enter the number of books taken: "))
total = 0
while (x!=0):
    ch = input("(O/o) For old and (N/n) for New")
    if((ch=="o") or (ch=="O")):
        total+=50
        x-=1
    elif((ch=="N") or (ch=="n")):
        total+=75
        x-=1
    else:
        print("Wrong Choice ")
print("Total = ",total)	
