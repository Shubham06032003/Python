#  Q1>
a = ['a',2,1.4]
b = ('a',2,1.4)
if type(b) is list:
    print("this is a list")
elif type(b) is tuple:
    print("this is a tuple")
else:
    print("this is a set")

# Q2>
def sortFunc(a):
    return a[1]
a = [('Shubham',2),('Yash',-1),('Abhishek',0)]
sortSecEle= sorted(a,key=sortFunc)
print(sortSecEle)

# Q3>
numList = []
numTuple = ()
num = input("Enter a number :- ")
save = num.split(",")
# ltInput =input("In which do you want to save the numbers either in list or in tuple :-")
for i in save:
    print(i)
    i = int(i)
    numList.append(i)
    numTuple += (i,)
print(numList)
print(numTuple)
# if ltInput == "list":
#     for i in save:
#         print(i)
#         i = int(i)
#         numList.append(i)
#     print(numList)
# elif ltInput == "tuple":
#     for i in save:
#         print(i)
#         i = int(i)
#         numTuple = numTuple+(i,)
#     print(numTuple)


# Q4>
# sum = (1,2,3,4,5)
# add = 0
# for i in sum :
#     add += i
# print(add)

# Q5>
a = [('Shubham','Panwar'),('Yash','Ghalot'),('Abhishek','Pugliya')]
sort = sorted(a)
print(sort)

# Q6>
if 'b' in b:
    print("this is present")
else:
    print("this is not present")