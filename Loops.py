num = int(input("Enter a number :- ")) 
Num = int(2*num)
# count = 0
# for i in range(2,num+1):
#     if(num%i == 0):
#         count+=1
# if(count==1):
#     print(str(num)+" is a Prime Number")
# else:
#     print(str(num)+" is not a Prime Number") 

# Q
# for i in range(num):
#     for j in range(num-i):
#         print(" ",end=" ")

#     for j in range(i+1):
#         print("*",end=" ")

#     for j in range(1,i+1):
#         print("*",end=" ")    
#     print()

# for i in range(num):
#     for j in range(i+2):
#         print(" ",end=" ")

#     for j in range(num-i-1):
#         print("*",end=" ")

#     for j in range(1,num-i-1):
#         print("*",end=" ")    

#     print()

# Q2
for i in range(num):
    for j in range(num-i):
        print(" ",end=" ")

    for j in range(i+1):
        print("*",end=" ")

    for j in range(1,i+1):
        print("*",end=" ")    
    
    for j in range(num-i):
        print(" ",end=" ")

    for j in range(1,num-i):
        print(" ",end=" ")    
   
    for j in range(i+1):
        print("*",end=" ")

    for j in range(1,i+1):
        print("*",end=" ")    
    print()

for i in range(Num):
    for j in range(i+1):
        print(" ",end=" ")

    for j in range(Num-i):
        print("*",end=" ")

    for j in range(1,Num-i):
        print("*",end=" ")    
    print()