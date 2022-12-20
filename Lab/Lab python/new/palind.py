s=input('Enter a string ')

print("Pal" if s in s[-1::-1] else "not")