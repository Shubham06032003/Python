import datetime as dt

name = input("Enter your name :- ")

Date = dt.date.today()
# print(Date)
    

print('''
press 1 if you like workout
press 2 if you like junk food 
''')
num = int(input())
if num == 1 :
    with open("health Management.txt","a") as f:
        f.write(f"\t\t\t\t{Date}\n\n")
        f.write(f"{name}  likes   workout  Therefore  Your Health is Good \n\n")
elif num == 2 :
    with open("health Management.txt","a")as f:
        f.write(f"\t\t\t\t{Date}\n\n")
        f.write(f"{name}  likes   Junk food  so  Please focus on your health \n\n")