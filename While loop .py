num = int(input("Enter a number :- "))

Num = num
rev = 0
while(num > 0):
    lastNum = num%10
    rev = (rev*10)+int(lastNum)
    num//=10
# print(rev)
if(rev == Num):
    print(str(Num) + " is a palindrome number" )
else:
    print(str(Num) + " is not a palindrome number" )