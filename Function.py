def recursive(n):
    if(n<=0):
        return 1
    
    func = recursive(n-1)
    return n*func

n = int(input("Enter a number :- "))
print("Factorial :- " + str(recursive(n)))