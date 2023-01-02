import time as t
import os as sys

def clear():
    sys.system("cls")

def time():
    t.sleep(2)
day = t.asctime()
    
clear()
print('''
\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
\t*****************************************************************
\t\t\t\t   Welcome
\t\t\t\t     to
\t\t\t\t Money Management
\t\t\t\t    System
\t*****************************************************************
\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
''')
time()
clear()

print('''
Press 1 -> To add items in list
Press 2 -> See the list 
Press 3 -> Exit
''')
total = 0
choice = int(input("Choose an option :- "))
if choice == 1 :
    print("press x for stop writing")
    with open("Money Management.txt","a") as header:
        header.write(f"\t\t\t\t\t{day}\n\n")
    with open("Money Management.txt","a") as d:
        d.write(f"items\t\t  Price\n")
    while True:
        item = input("Enter the name of item :- ")
        if item == "x":
            break
        price = int(input("Enter the price of item :- "))
        with open("Money Management.txt","a") as f:
            f.write(f"{item}\t\t\t{price}\n")
        total += price
    with open("Money Management.txt","a") as t:
        t.write(f"\nTotal\t\t\t{total}\n\n\n\n\n\n")
elif choice == 2:
    with open("Money Management.txt") as r:
        print(r.read())
elif choice == 3 :
    exit()