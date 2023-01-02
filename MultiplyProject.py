import time as t , random as rd

num = int(input("Enter a number :- "))

storeNum = []
for i in range(1,num+1):
    storeNum.append(i)

print(storeNum)

compNum = []
for i in range(1,10):
    compNum.append(i)
step =0
point = 0
while step<5:
    randNum1 = rd.choice(storeNum)
    randNum2 = rd.choice(compNum)

    multiply = randNum1*randNum2
    start = t.time()
    user = int(input(f"{randNum1} x {randNum2} = "))
    end = t.time()

    takeTime = end - start
    print(takeTime) 
    if takeTime > 10:
        print("time ends")
        point-=2
        # exit()
    elif user == multiply:
        # print("you won")
        point+=10
    else:
        print("you lose")
        point -= 1
        # exit()
    step+=1
print(f"you got {point} points")