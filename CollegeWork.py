# Q1>

# Max = 0
# Smax = 0

# print("Press 0 to Stop")
# while True :
#     num2 = int(input("Enter a Number :- "))
#     if num2 ==0 :
#         break
#     if num2>Max :
#         Smax = Max
#         Max = num2
#     if num2>Smax and num2 != Max :
#         Smax = num2

# print("Max :- ",Max)
# print("Second Max :- ",Smax)

# Q2>
Max = 0
pos =0
print("Press 0 to Stop")
while True :
    num2 = int(input("Enter a Number :- "))
    if num2 ==0 :
        break
    if num2>Max :
        Max = num2
        pos += 1
 

print("Max :- ",Max)
print("Position of Max Number :- ",pos)
    
# Q3>

# Num = int(input("Enter a Number :- "))
# mx = 0
# td = 0
# saveNum = Num
# pos = 0
# while(Num != 0):
#     lastDig = Num%10
#     if(lastDig > mx):
#         mx = lastDig
#         pos += 1
#     td += 1
#     Num //=10

# pos = td - pos+1
# print("Maximum Number in ",saveNum, " is :- ",mx ," And its position is :- ", pos)  

# Q4>

# fixAmount = 300
# preUnit = int(input("Enter your Previous Unit :- "))
# currUnit = int(input("Enter your Current Unit :- "))
# unit = currUnit - preUnit
# amt = 0.0
# while unit != 0:
#     if unit>= 200:
#         amt += 0.75
#     elif unit>= 100 and unit < 200:
#         amt +=0.6
#     elif unit >= 50 and unit < 100:
#         amt +=0.5
#     unit -= 1
# bill = amt + fixAmount
# print("Amount of Your Electricity :- Rs " ,bill)

# Q5>

# num = int(input("Enter a Number :- "))
# Save = num  
# revNum = 0
# while num != 0:
#     lastDig = num%10
#     revNum = (revNum*10)+lastDig
#     num//=10

# print("Reverse of ",Save ," is :- " ,revNum)

                    # or
# it works only on Strings
# rev = num[::-1]
# print(rev)