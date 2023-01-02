# with open("file.txt") as f:
#     a = f.read()
#     print(a)

name = input("Enter Your name :- ")
with open("file2.txt","a") as f:
    a = f.write(f"\n{name}")

with open("file2.txt","r") as f:
    print(f.read())