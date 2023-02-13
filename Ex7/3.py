l=[v for v in range(1,10)]
print("Original List " , l)
def is_even(x): return x%2==0
lis2=list(filter(is_even,l))
print(lis2)
