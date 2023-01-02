# Q2> convert String into a list
# Method -> 1
# name = input("Enter your name : ")
# list = name.split()
# print(list)

#  Method -> 2

# list2 = []
# for i in range(len(name)):
#     list2.append(name[i])
# print(list2)

# Q3> Append element to the list

# num = [1,2,3,4]
# print(num)
# num.append(5)
# print(num)
# numbers = []
# print("Press s to Stop the program")
# while True:

#     num = input("Enter a number : ")
#     if(num == 's'or num == 'S'):
#         break
#     else:
#         num = int(num)  
#         print(type(num))
#         numbers.append(num)
# print(numbers)
# print(type(num))


# Q4> Compare two list 

# list1 = []
# list2 = [2]

# for i in range(9):
#     list1.append(i)
#     list2.append(i)

# print(list1)
# print(list2)
# if list1 == list2:
#     print("both lists are Same")
# else:
#     print("both lists are different")

# Q5> convert integer to string
# num = 12
# num = int(input("Enter a number : "))
# print(f"{num} is of {type(num)}")
# num = str(num)
# print(f"{num} is of {type(num)}")

# Q6> concatenate two strings

# a = 'hello'
# b = 'world'
# c = a + " "+ b
# print(c)

# Q7> Reverse a number

# num = int(input("Enter a number : "))
# revnum = 0
# while num != 0:
#     lastDig = num%10
#     revnum = (revnum*10)+lastDig
#     num//=10

# print(revnum)

# Q8> Draw the Pattern

# # Pyramid
# for i in range(5):
#     print(" "*(5-i),end = " ")
#     print("*"*i,end ="")
#     print("*"*(i-1))

# # Diamomd
# for i in range(4):
#     print(" "*(4-i),end =" ")
#     print("*"*i,end ="")
#     print("*"*(i-1))
# for j in range(4,0,-1) :
#     print(" "*(4-j),end =" ")
#     print("*"*j,end ="")
#     print("*"*(j-1))

# Star

for i in range(6):
        print(" "*(5-i),end =" ")
        print("* "*i)

# Q9> Second Largest number of list

# smax = -1234235
# num = [2,5,8,26,31,17]
# mx = max(num)
# # print(mx)
# for i in num:
#     if i>smax and i<mx:
#         smax = i
# print(smax)

# Q10> Fibonacci Series till nth number

# num = int(input("Enter a number : "))
# a = 0 
# b = 1
# a,b = 0,1
# for i in range(num):
#     print(a)
#     temp = a+b
#     a = b
#     b = temp