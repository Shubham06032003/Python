import os as os

print('''Welcome! to the guess a number game
** Instruction ** : 
1> You want to guess a number between 1 and 20
2> You have only 5 chance to guess a number
3> If your number is match with hidden number then you win the game
''')

hidNum = 14
guess = 1
while(guess <= 5):
    print("chance : " + str(guess) )
    num = int(input("Enter a number between 1 and 20 :- "))
    if guess > 4:
        if hidNum == num :
            print("Hurry !!! You won the game ")
            break 
        print("Sorry !! You lose the game ")
        break
        os.system("cls")
    elif hidNum == num :
        print("Hurrah !!! You won the game ")
        break
    elif num > 20 :
        print("This number is out of range")
        os.system("cls")
        print("Please , Give the number between 1 and 20")
    elif num < hidNum :
        os.system("cls")
        print("It is too small. Try Again ... ")
    elif num > hidNum:
        os.system("cls")
        print("It is too large. Try Again ... ")
    guess +=1