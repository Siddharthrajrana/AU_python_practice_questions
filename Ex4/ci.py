def CI(p,r,t):
    return p*(1+r/100)**t

p=float(input("Enter principal : "))
r=float(input("Enter Rate percent :"))
t=float(input("Enter Time in year : "))
print('Compound intrest is ' ,format(CI(p,r,t)))
