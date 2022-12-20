m1=int(input('Enter Maths marks : '))
m2=int(input('Enter eng marks : '))
m3=int(input('Enter sci marks : '))
m4=int(input('Enter sst marks : '))

total=m1+m2+m3+m4
agg=total/4

print('Total = ',total,'Aggegrate= ',agg)

if agg>=75: print('Distinction ')
elif agg<75 and agg>=60: print('First div.')
elif agg<65 and agg>=50: print('First div.')
elif agg<50 and agg>=45: print('First div.')
else : print('Fail')