import os , random

os.system("cls")
print('''

 --- Welcome to the Snake Water Gun Game ---

*** INSTRUCTIONS ***
1 -> Choose a character
2 -> " Snake --win--> Water --win--> Gun --win--> Snake "
3 -> if Your choosen character is Bigger then the Computer character then you win and get a point otherwise you lose in that chance game.
4 -> You have only 10 chances
5 -> Which one have more points it become the Winner of the Game
''')

name = input("Enter your Name :- ")

UserList = ["s","w","g"]
UserPoint = 0
ComputerPoint = 0
Chance = 0
while Chance <=9:
    Characters = ["Gun","Snake","Water"] 
    Computer = random.choice(Characters)
    print(f"Chance :- {Chance+1}")
    if Chance == 10 :
        print("-- Game Over --")
        print()
        break
    user = input(''' --- Choose a Character ---
    Click "s" for "Snake"
    Click "w" for "Water"
    Click "g" for "Gun"
    Enter here :- ''')

    if user not in UserList:
        print(" -- Please enter the correct letter -- ")
        Chance -=1

    if user == "s":
        if Computer == "Water":
            UserPoint += 1
            print(" -- You get one point -- ")
        elif Computer == "Gun":
            ComputerPoint += 1
            print("--- Sorry ---")
        else:
            print("Both are Same")
    elif user == "w":
        if Computer == "Gun":
            UserPoint += 1
            print(" -- You get one point -- ")
        elif Computer == "Snake":
            ComputerPoint += 1
            print("-- Sorry --")
        else:
            print("Both are Same")
    elif user == "g":
        if Computer == "Snake":
            UserPoint += 1
            print(" -- You get one point -- ")
        elif Computer == "Water":
            ComputerPoint += 1
            print("-- Sorry --")
        else:
            print("Both are Same")
    Chance += 1

print(f"{name} :- {UserPoint}              Computer :- {ComputerPoint}")
if UserPoint > ComputerPoint:
    print(f" -- {name} won the Game -- ")
elif UserPoint == ComputerPoint:
    print(" -- Match Draw -- ")
else :
    print(f" -- {name} lose the Game -- ") 