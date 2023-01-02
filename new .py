fnum = int(input("Enter a number :- "))
snum = int(input("Enter a number :- "))
tnum = int(input("Enter a number :- "))
mx = 0
smax=0
if fnum>snum:
    smax=snum
    mx = fnum
else:
    smax=fnum
    mx = snum
if tnum>mx:
    smax = mx
    mx = tnum
elif tnum>smax:
    smax = tnum
print(f"{mx} is max")
print(f"{smax} is Second max")


