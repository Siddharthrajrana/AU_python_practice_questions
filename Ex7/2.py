import functools
nums= [v for v in range(1,11)]
ans = functools.reduce(lambda x,y:x+y, nums)
print(ans)
