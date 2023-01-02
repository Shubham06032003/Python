import time

# initial = time.time()
# print(initial)
k=0
while k<=10:
    time.sleep(1)
    print("Hello")
    k +=1
# print("While loop run in :", time.time()-initial)

# initial2 = time.time() 
# for i in range(10):
#     print("Hey")
# print("For loop run in :", time.time()-initial2)

# LocalTime = time.asctime(time.localtime(time.time()))
# LocalTime = time.asctime()
# print(LocalTime)