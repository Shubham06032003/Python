import time as t

time = t.asctime()
with open("file.txt","a") as t:
    t.write(f"\n {time}")
with open("file.txt","r") as r:
    print(r.read())
