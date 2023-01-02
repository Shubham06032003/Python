# 0 1 1 2 3 5 8 

def rec(num):
    if(num==0):
        return 0
    if(num==1):
        return 1
    for i in range(num):
        fun = rec(num - 1)
        return num + fun
num = int(input("Enter a number :- "))
print("Fabonacci :- ",str(rec(num)))