Max = 0
Smax = 0

print("Press 0 to Stop")
while True :
    num2 = int(input("Enter a Number :- "))
    if num2 ==0 :
        break
    if num2>Max :
        Smax = Max
        Max = num2
    if num2>Smax and num2 != Max :
        Smax = num2

print("Max :- ",Max)
print("Second Max :- ",Smax)