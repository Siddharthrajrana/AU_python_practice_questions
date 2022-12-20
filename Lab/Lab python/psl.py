
s=input("Enter a string ")
l=int(len(s))
count =0
s=s.lower()
for i in range(l):
    if s[i] == 'a'or s[i] =='e'or s[i] =='i'or s[i] == 'o'or s[i] =='u':
        count+=1

print("Total vowel = ",count)
        
