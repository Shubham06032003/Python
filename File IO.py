# File IO Basics

'''
"r" :-  Open file for reading 
"w" :-  Open file for writing
"x" :-  Create file if not exists
"a" :-  Add more content to a file
"t" :-  text mode
"b" :- Binary mode
"+" :- Read and Write
'''
f = open("file.txt")
# content = f.read()
# print(content)
print(f.readlines())
# print(f.readline())
# print(f.readline())
# for line in content:
    # print(line, end = "")
f.close()