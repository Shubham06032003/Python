# Dictionary is nothing but a key value pairs

# d = {}
# d = []
# d = ()
# print(type(d))
# dict = {"Shubham":"Rice","Yash":"Soyachanks","Mohit":"Egg","Pankaj":{"B":"milk","L":"Roti","D":"rice"}}
# print(dict)
# print(dict["Mohit"])
# print(dict["Pankaj"])
# dict["Ankit"] = "Burger" #or
# dict.update({"Ankit":"Buger"})
# dict[6] = "Momos"
# del dict[6]
# dict2 = dict.copy()
# del dict2["Mohit"]
# print(dict)
# print(dict.keys())
# print(dict.items())

# Question
#Make a dictionary and take input from user in it

name = input("Enter your name :- ")
item = input("Enter your item name :- ")
dict = {name:item}
ask = input("Do you want to check which item you add (y/n) :- ")
if(ask == "y"):
        print(dict.items())
else:
    exit()
    
# print(dict)