Num1 = int(input("Enter a Number :- "))
Num2 = int(input("Enter another Number :- "))
Num3 = int(input("Enter another Number :- "))

# to find Minimum Value
# if Num1<Num2:
#     if Num1<Num3:
#         Min = Num1
#     else:
#         Min = Num3
    
# elif Num2<Num1:
#     if Num2 < Num3:
#         Min = Num2
#     else:
#         Min = Num3
# else:
#     Min = Num3
#     # Smin = min(Num1, Num2)

# print("Min Value :- " , Min)
# # print("Second Minimum Value :- ",Smin)

if Num1 < Num2:
    if Num1>Num3:
        Smin = Num1
elif Num2< Num1:
    if Num2>Num3:
        Smin = Num2
elif Num3<Num2 :
    if Num3>Num1:
        Smin = Num3
elif Num3<Num1 :
    if Num3>Num2:
        Smin = Num3
    
print("Second Minimum Value :- ",Smin)