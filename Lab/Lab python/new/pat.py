n=7

for i in range(1,n):
    for j in range(i):
        print('*',end=' ')
    print()
print()
for i in range(1,n):
    for j in range(1,i+1):
        print(j ,end=' ')
    print()
print()
for i in range(1,n):
    for j in range(n,i,-1):
        print('*',end=' ')
    print()

print()
for i in range(1,n):
    for j in range(n,i,-1):
        print(' ',end=' ')
    for k in range(1,i+1):
        print('*  ',end=' ')
    print()