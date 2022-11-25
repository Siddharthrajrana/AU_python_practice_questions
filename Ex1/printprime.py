x = int(input("Enter the nth term  : "))
i=2
while i!=x:
    j=3
    while j<i:
        if j/i==0:
            break
        else:
            print(i)
        j=j+1
    i=i+1     