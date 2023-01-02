import time as t
import os 

# 5 = int(input("Enter an odd 5ber :- "))

# for print I
os.system("cls")

for i in range(5):
    for j in range(5-1):
        if i== 0 or i == 5-1:
            print("*",end=" ")
        if j == 5-2:
            print(" ",end=" ")
        if j == (5+1)/2:
            print("*",end="")
        else:
            print(" ",end=" ")

        t.sleep(0.2)


    print(end="\n\n\n")
t.sleep(1)
os.system("cls")

# for print heart
for i in range(5):
    for j in range(5-i):
        print(" ",end=" ")

    for j in range(i+1):
        print("*",end=" ")

    for j in range(1,i+1):
        print("*",end=" ")    
    
    for j in range(5-i):
        print(" ",end=" ")

    for j in range(1,5-i):
        print(" ",end=" ")    
   
    for j in range(i+1):
        print("*",end=" ")

    for j in range(1,i+1):
        print("*",end=" ")    
    t.sleep(0.5)
    print()

for i in range(10):
    for j in range(i+1):
        print(" ",end=" ")

    for j in range(10-i):
        print("*",end=" ")

    for j in range(1,10-i):
        print("*",end=" ")    
    t.sleep(0.2)
    print()
t.sleep(1)
os.system("cls")

# for print U

for i in range(5):  
    for j in range(5):
        if i== 4:
            print("*      ",end="")
        elif j == 0 or j==3:
            print("*\t\t\t",end="")
        else:
            print(" ",end=" ")
    t.sleep(0.5)
    print(end="\n\n\n")        