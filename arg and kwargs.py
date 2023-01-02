def name(normal,*Name,**Role): # normal statement must be written first 
    # print(a,b,c,d)# This will give the error for more elements
    print(normal)
    for item in Name:
        print(item)
    print("These Students are :-")
    for key,value in Role.items():
        print(f"{key} is a {value}")

normal = print("These students are absent today ")
Name = ["Ram","Shyam","Mohan","Sohan","Shubham"]
Role = {"Ram":"Moniter","Shyam":"Topper"}
name(normal,*Name,**Role)