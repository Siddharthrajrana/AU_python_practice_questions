def cel_to_faren(c):
    return (c*9/5)+32

cel=float(input ("Enter the temp in degree celcius : "))
print("Temp ",cel ,"in Farenheight is " ,cel_to_faren(cel))
